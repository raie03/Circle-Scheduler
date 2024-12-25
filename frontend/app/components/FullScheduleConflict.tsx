import React from "react";
import ConflictDetail from "./ConflictDetail";

const FullScheduleConflict = ({ statistics }: any) => {
  const { conflicts_by_timeslot } = statistics;
  // const performances = Object.values(conflicts_by_timeslot);
  // const conflicts = performances.filter((date: any) => {
  //   //   console.log(date.total_conflicts);
  //   return date.total_conflicts > 0;
  // });
  const performances = Object.entries(conflicts_by_timeslot);
  const conflicts = performances.filter((date: any) => {
    // console.log(date[1]);
    return date[1].total_conflicts > 0;
  });
  // console.log(conflicts);
  return (
    <div>
      <h1>被り</h1>

      {conflicts.map((conflict: any, index: number) => {
        // const performances = conflicts_by_timeslot[dateTime].total_conflicts;
        // console.log(Object.values(conflict)[1]);
        const conflict_data: any = Object.values(conflict)[1];
        const conflict_date: any = Object.values(conflict)[0];
        const conflict_details = conflict_data.conflict_details;
        return (
          <div key={index}>
            <div>{conflict_date}</div>
            <div className="py-2 border">
              {Object.values(conflict_details).map(
                (detail: any, index: number) => {
                  console.log(detail);
                  return <ConflictDetail detail={detail} key={index} />;
                }
              )}
            </div>
          </div>
        );
      })}
    </div>
  );
};

export default FullScheduleConflict;
