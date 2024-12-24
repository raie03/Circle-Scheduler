import React from "react";

const ConflictDetail = ({ detail }: any) => {
  return (
    <div>
      <h2>被り演目: {detail.performance1}</h2>
      <h2>被り演目: {detail.performance2}</h2>
      <p>被りメンバー数: {detail.overlapping_members}</p>
      <div></div>
    </div>
  );
};

export default ConflictDetail;
