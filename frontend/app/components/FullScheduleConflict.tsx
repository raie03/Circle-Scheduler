import React from "react";
import ConflictDetail from "./ConflictDetail";

const FullScheduleConflict = ({ conflicts_by_timeslot }: any) => {
  const performances = Object.values(conflicts_by_timeslot);
  const conflicts = performances.filter((date: any) => {
    //   console.log(date.total_conflicts);
    return date.total_conflicts > 0;
  });
  //console.log(conflict);
  return (
    <div>
      <h1>被り</h1>

      {conflicts.map((conflict: any, index: number) => {
        // const performances = conflicts_by_timeslot[dateTime].total_conflicts;
        // console.log(Object.values(conflict.conflict_details));
        const conflict_details = conflict.conflict_details;
        return (
          <div key={index} className="py-2 border">
            {Object.values(conflict_details).map(
              (detail: any, index: number) => {
                console.log(detail);
                return <ConflictDetail detail={detail} key={index} />;
              }
            )}
          </div>
        );
      })}
    </div>
  );
};

export default FullScheduleConflict;
