import React from "react";
import FullSchedule from "../components/FullSchedule";
import FullScheduleConflict from "../components/FullScheduleConflict";

async function getScheduleData() {
  const response = await fetch("http://127.0.0.1:8000/schedule/test", {
    cache: "no-store",
  });

  const scheduleData = await response.json();

  return scheduleData;
}

const SchedulePage = async () => {
  const scheduleData = await getScheduleData();
  const { input_data, schedule_result, statistics } = scheduleData;
  const { conflicts_by_timeslot } = statistics;
  console.log(scheduleData);
  // console.log(Object.keys(scheduleData));
  // console.log(scheduleData.schedule_result);

  return (
    <div className="px-5">
      <FullSchedule scheduleResult={schedule_result} />
      <FullScheduleConflict conflicts_by_timeslot={conflicts_by_timeslot} />
    </div>
  );
};

export default SchedulePage;
