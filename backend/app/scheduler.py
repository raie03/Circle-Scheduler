# import numpy as np

# スケジュール作成アルゴリズム

import random
from datetime import datetime, timedelta
from typing import List, Dict, Set, Tuple
from dataclasses import dataclass
import json
from collections import defaultdict

@dataclass
class Performance:
    id: int
    name: str
    members: Set[int]
    priority: float = 0.0

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'members': list(self.members),
            'priority': self.priority
        }

class EfficientScheduler:
    def __init__(self, performances: List[Performance], member_availability: Dict[int, List[datetime]]):
        self.performances = performances
        self.member_availability = member_availability
        self.schedule = defaultdict(list)  # 時間帯ごとの演目リスト
        
    def calculate_performance_priorities(self):
        """演目の優先度を計算"""
        for perf in self.performances:
            # メンバー数が多い演目ほど優先度を高く
            member_factor = len(perf.members) / 100
            # 予定の制約が厳しい演目ほど優先度を高く
            availability_constraints = self._calculate_availability_constraints(perf)
            perf.priority = member_factor + availability_constraints
    
    def _calculate_availability_constraints(self, performance: Performance) -> float:
        """メンバーの予定の制約度を計算"""
        available_slots = set()
        for member_id in performance.members:
            member_slots = set(self.member_availability.get(member_id, []))
            if not available_slots:
                available_slots = member_slots
            else:
                available_slots &= member_slots
        return 1.0 - (len(available_slots) / 50)  # 利用可能な時間枠が少ないほど高優先度
    
    def find_best_time_slot(self, performance: Performance) -> datetime:
        """演目に最適な時間枠を探索"""
        # メンバー全員が参加可能な時間枠を見つける
        common_slots = set()
        for member_id in performance.members:
            member_slots = set(self.member_availability.get(member_id, []))
            if not common_slots:
                common_slots = member_slots
            else:
                common_slots &= member_slots
        
        best_slot = None
        min_conflicts = float('inf')
        
        for slot in common_slots:
            conflicts = self._count_conflicts(performance, slot)
            if conflicts < min_conflicts:
                min_conflicts = conflicts
                best_slot = slot
                
        return best_slot
    
    def _count_conflicts(self, performance: Performance, time_slot: datetime) -> int:
        """特定の時間枠での競合数をカウント"""
        conflicts = 0
        for existing_perf in self.schedule[time_slot]:
            conflicts += len(performance.members & existing_perf.members)
        return conflicts
    
    def optimize(self) -> Dict[datetime, List[Performance]]:
        """スケジュールの最適化"""
        # 優先度の計算
        self.calculate_performance_priorities()
        
        # 優先度順に演目をソート
        prioritized_performances = sorted(
            self.performances,
            key=lambda x: x.priority,
            reverse=True
        )
        
        # 優先度の高い演目から順にスケジューリング
        for performance in prioritized_performances:
            best_slot = self.find_best_time_slot(performance)
            if best_slot:
                self.schedule[best_slot].append(performance)
        
        return self.schedule

class EnhancedScheduler(EfficientScheduler):
    def __init__(self, performances: List[Performance], member_availability: Dict[int, List[datetime]]):
        super().__init__(performances, member_availability)
        self.debug_info = {
            'input_data': {},
            'schedule_result': {},
            'statistics': {}
        }

    def optimize(self) -> Dict[datetime, List[Performance]]:
        # 入力データを記録
        self.debug_info['input_data'] = {
            'performances': [p.to_dict() for p in self.performances],
            'member_availability': {
                str(member_id): [t.strftime('%Y-%m-%d %H:%M') for t in times]
                for member_id, times in self.member_availability.items()
            }
        }

        # スケジューリング実行
        schedule = super().optimize()

        # スケジュール結果を記録 
        self.debug_info['schedule_result'] = {
            time_slot.strftime('%Y-%m-%d %H:%M'): [
                {
                    'id': p.id,
                    'name': p.name,
                    'members': list(p.members),
                    'priority': p.priority
                } for p in perfs
            ]
            for time_slot, perfs in sorted(schedule.items())
        }

        # 統計情報を計算
        self._calculate_statistics(schedule)

        return schedule

    def _calculate_statistics(self, schedule: Dict[datetime, List[Performance]]):
        stats = {
            'total_performances_scheduled': 0,
            'conflicts_by_timeslot': {},
            'member_participation': defaultdict(int),
            'performance_details': []
        }

        for time_slot, performances in sorted(schedule.items()):
            time_str = time_slot.strftime('%Y-%m-%d %H:%M')
            stats['total_performances_scheduled'] += len(performances)
            
            # 時間枠ごとの競合
            conflicts = 0
            conflict_details = []
            for i, perf1 in enumerate(performances):
                for perf2 in performances[i+1:]:
                    overlapping = len(perf1.members & perf2.members)
                    if overlapping > 0:
                        conflicts += overlapping
                        conflict_details.append({
                            'performance1': perf1.name,
                            'performance2': perf2.name,
                            'overlapping_members': overlapping
                        })
            
            stats['conflicts_by_timeslot'][time_str] = {
                'total_conflicts': conflicts,
                'conflict_details': conflict_details
            }

            # メンバーごとの参加回数
            for perf in performances:
                for member in perf.members:
                    stats['member_participation'][str(member)] += 1

            # 演目ごとの詳細
            for perf in performances:
                stats['performance_details'].append({
                    'time': time_str,
                    'performance': perf.name,
                    'member_count': len(perf.members)
                })

        self.debug_info['statistics'] = stats

def generate_test_data(num_members: int, num_performances: int) -> Tuple[List[Performance], Dict[int, List[datetime]]]:
    # メンバーデータ生成
    performances = []
    for i in range(num_performances):
        members = set(random.sample(range(num_members), random.randint(5, 15)))
        performances.append(Performance(i, f"演目{i}", members))
    
    # 利用可能時間生成
    base_time = datetime(2024, 1, 1, 10, 0)  # 10:00から
    member_availability = {}
    for i in range(num_members):
        available_times = [
            base_time + timedelta(hours=h)
            for h in random.sample(range(0, 24, 2), random.randint(5, 10))
        ]
        member_availability[i] = available_times
    
    return performances, member_availability

def run_detailed_test():
    # テストデータ生成
    print("テストデータ生成中...")
    performances, availability = generate_test_data(100, 20)
    
    # スケジューリング実行
    print("スケジューリング実行中...")
    # start_time = time.time()
    scheduler = EnhancedScheduler(performances, availability)
    schedule = scheduler.optimize()
    # execution_time = time.time() - start_time
    
    # 結果の出力
    # print(f"\n実行時間: {execution_time:.3f}秒")
    print("\n=== スケジュール結果 ===")
    for time_slot, perfs in sorted(schedule.items()):
        print(f"\n{time_slot.strftime('%H:%M')}:")
        for perf in perfs:
            print(f"  - {perf.name} (メンバー{len(perf.members)}名)")
    
    stats = scheduler.debug_info['statistics']
    print("\n=== 統計情報 ===")
    print(f"スケジュール済み演目数: {stats['total_performances_scheduled']}")
    
    print("\n時間枠ごとの競合:")
    for time, conflicts in stats['conflicts_by_timeslot'].items():
        if conflicts['total_conflicts'] > 0:
            print(f"{time}: {conflicts['total_conflicts']}件の競合")
    
    print("\nメンバーの参加回数TOP10:")
    sorted_participation = sorted(
        stats['member_participation'].items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]
    for member_id, count in sorted_participation:
        print(f"メンバー{member_id}: {count}回")
    
    return scheduler.debug_info
    # 詳細データの保存
    # with open('schedule_debug.json', 'w', encoding='utf-8') as f:
    #     json.dump(scheduler.debug_info, f, ensure_ascii=False, indent=2)
    
    # print("\n詳細なデバッグ情報は'schedule_debug.json'に保存されました")

def get_detail_data(performances: int, availability: int):
    # スケジューリング実行
    print("スケジューリング実行中...")
    # start_time = time.time()
    scheduler = EnhancedScheduler(performances, availability)
    schedule = scheduler.optimize()
    # execution_time = time.time() - start_time
    
    # 結果の出力
    # print(f"\n実行時間: {execution_time:.3f}秒")
    print("\n=== スケジュール結果 ===")
    for time_slot, perfs in sorted(schedule.items()):
        print(f"\n{time_slot.strftime('%H:%M')}:")
        for perf in perfs:
            print(f"  - {perf.name} (メンバー{len(perf.members)}名)")
    
    stats = scheduler.debug_info['statistics']
    print("\n=== 統計情報 ===")
    print(f"スケジュール済み演目数: {stats['total_performances_scheduled']}")
    
    print("\n時間枠ごとの競合:")
    for time, conflicts in stats['conflicts_by_timeslot'].items():
        if conflicts['total_conflicts'] > 0:
            print(f"{time}: {conflicts['total_conflicts']}件の競合")
    
    print("\nメンバーの参加回数TOP10:")
    sorted_participation = sorted(
        stats['member_participation'].items(),
        key=lambda x: x[1],
        reverse=True
    )[:10]
    for member_id, count in sorted_participation:
        print(f"メンバー{member_id}: {count}回")
    
    return scheduler.debug_info


# if __name__ == "__main__":
#     run_detailed_test()
