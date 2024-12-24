import React from "react";
import ScheduleItem from "./ScheduleItem";

const FullSchedule = ({ scheduleResult }: any) => {
  return (
    <div>
      <h1>スケジュール</h1>
      {Object.keys(scheduleResult).map((dateTime: any) => {
        const performances = scheduleResult[dateTime];
        return (
          <div key={dateTime} className="px-5 py-2 border">
            <h2>{dateTime}</h2>
            {performances.map((performance: any) => (
              <ScheduleItem key={performance.id} performance={performance} />
            ))}
          </div>
        );
      })}
    </div>
  );
};

export default FullSchedule;
