async function getPerformanceData(performanceId: any) {
  const response = await fetch(
    `http://127.0.0.1:8000/scheduleTest/${performanceId}`,
    {
      cache: "no-store",
    }
  );

  const performanceData = await response.json();

  return performanceData;
}

const PerformanceData = async ({ params }: any) => {
  const { performanceId } = await params;
  const performanceData = await getPerformanceData(performanceId);
  const { performance_data } = performanceData;
  //   console.log(performanceId);
  //   console.log(performance_data);
  return (
    <div className="container p-4">
      <div>
        <h2 className="">
          演目名:{performance_data.name} (優先度:{performance_data.priority})
        </h2>
        <div>
          <h2>メンバー</h2>
          {performance_data.members.map((member: any) => {
            return <div key={member}>{member}</div>;
          })}
        </div>
        <div>
          <h2>練習日</h2>
          {performance_data.time_slots.map((time_slot: any) => {
            return <div key={time_slot}>{time_slot}</div>;
          })}
        </div>
      </div>
    </div>
  );
};

export default PerformanceData;
