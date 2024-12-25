from fastapi import APIRouter, HTTPException
from app import scheduler
from typing import Dict, List
from pydantic import BaseModel
from datetime import datetime
import json

router = APIRouter()

# Pydanticモデルの定義
class MemberAvailability(BaseModel):
    member_id: int
    available_times: List[str]  # ISO形式の日時文字列

class PerformanceInput(BaseModel):
    id: int
    name: str
    members: List[int]

class ScheduleRequest(BaseModel):
    performances: List[PerformanceInput]
    member_availability: Dict[str, List[str]]  # member_id: available_times

class ScheduleResponse(BaseModel):
    schedule_result: Dict[str, List[Dict]]
    statistics: Dict
    execution_time: float

# スケジュールAPI

# @router.post("/schedule")
# def create_schedule(data: dict):
#     # フロントエンドから送られたデータを処理
#     result = generate_schedule(data)
#     return {"schedule": result}

@router.post("/schedule")
async def create_schedule(request: ScheduleRequest):
    try:
        # 入力データの変換
        performances = [
            scheduler.Performance(
                id=p.id,
                name=p.name,
                members=set(p.members)
            ) for p in request.performances
        ]
        
        # datetime文字列をdatetimeオブジェクトに変換
        member_availability = {
            int(member_id): [
                datetime.fromisoformat(time_str)
                for time_str in times
            ]
            for member_id, times in request.member_availability.items()
        }
        
        # スケジューリング実行
        scheduler = scheduler.EnhancedScheduler(performances, member_availability)
        schedule = scheduler.optimize()
        
        # レスポンスの作成
        # return ScheduleResponse(
        #     schedule_result=scheduler.debug_info['schedule_result'],
        #     statistics=scheduler.debug_info['statistics'],
        #     # execution_time=scheduler.debug_info.get('execution_time', 0.0)
        # )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/GetSchedule")
async def get_schedule():
    scheduleData = scheduler.run_detailed_test()
    return scheduleData

@router.get("/scheduleTest")
async def get_schedule_test():
    try:
        # テストデータの生成とスケジューリング
        performances, availability = scheduler.generate_test_data(100, 20)
        scheduler_Data = scheduler.get_detail_data(performances, availability)
        # schedule = scheduler.optimize()
        
        # JSONシリアライズ可能な形式に変換
        # response_data = {
        #     "schedule_result": scheduler.debug_info['schedule_result'],
        #     "statistics": scheduler.debug_info['statistics'],
        #     # "input_data": {
        #     #     "num_members": 100,
        #     #     "num_performances": 20
        #     # }
        # }
        return scheduler_Data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/scheduleTest/{performance_id}")
async def get_performance_data(performance_id: int):
    try:
        perfoemance_data = scheduler.get_performanceData(performance_id)
        
        return perfoemance_data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
