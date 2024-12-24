import React from "react";

const ScheduleItem = ({ performance }: any) => {
  return (
    <div key={performance.id}>
      <strong>{performance.name}</strong> (優先度: {performance.priority})
      <br />
      参加メンバー: {performance.members.join(", ")}
    </div>
  );
};

export default ScheduleItem;
