import Image from "next/image";
import Link from "next/link";
import ScheduleItem from "./components/ScheduleItem";
import FullSchedule from "./components/FullSchedule";

async function getScheduleData() {
  const response = await fetch("http://127.0.0.1:8000/scheduleTest", {
    cache: "no-store",
  });

  const scheduleData = await response.json();

  return scheduleData;
}

export default async function Home() {
  const scheduleData = await getScheduleData();
  console.log(scheduleData);
  // console.log(Object.keys(scheduleData));
  // console.log(scheduleData.schedule_result);

  const { schedule_result } = scheduleData;

  // Object.keys(scheduleResult).map((dateTime) => {
  //   console.log("日時:", dateTime);
  //   const performances = scheduleResult[dateTime];
  //   // console.log(performances);
  //   performances.forEach((performance: any) => {
  //     console.log("演目ID:", performance.id);
  //     console.log("演目名:", performance.name);
  //     console.log("参加メンバー:", performance.members);
  //     console.log("優先度:", performance.priority);
  //   });
  // });

  return (
    <main className="flex-col px-5">
      <div>スケジュール作成アプリ</div>
      <Link href={"/schedule"} className="text-blue-500">
        スケジュール確認テスト
      </Link>
      <Link href={"/schedule/response"} className="text-blue-500">
        回答内容確認テスト
      </Link>

      <FullSchedule scheduleResult={schedule_result} />
    </main>
  );
}
