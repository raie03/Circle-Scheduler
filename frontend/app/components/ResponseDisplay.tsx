import React from "react";

const ResponseDisplay = ({ input_data }: any) => {
  const member_availability = input_data.member_availability;
  return (
    <div>
      <div>回答情報</div>

      {Object.entries(member_availability).map((member: any) => {
        // console.log(member);
        const [memberName, availability] = member;
        return (
          <div key={memberName} className="px-5 py-2 border">
            <h2>名前:{memberName}</h2>
            {availability.map((time: any, index: number) => {
              return <div key={index}>{time}</div>;
            })}
          </div>
        );
      })}
    </div>
  );
};

export default ResponseDisplay;
