import Link from "next/link";
import React from "react";

const ScheduleItem = ({ performance }: any) => {
  // console.log(performance.id);
  return (
    <div key={performance.id}>
      <Link href={`/schedule/${performance.id}`} className="text-blue-500">
        {performance.name}
      </Link>
      (優先度: {performance.priority})
      <br />
      参加メンバー: {performance.members.join(", ")}
    </div>
  );
};

export default ScheduleItem;
