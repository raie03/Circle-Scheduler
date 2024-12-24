async function getResponseData() {
  const response = await fetch("http://127.0.0.1:8000/schedule/test", {
    cache: "no-store",
  });

  const responseData = await response.json();

  return responseData;
}

const Response = async () => {
  const responseData = await getResponseData();
  const { input_data } = responseData;
  const member_availability = input_data.member_availability;
  console.log(member_availability);

  return (
    <div>
      {Object.entries(member_availability).map((member: any) => {
        // console.log(member);
        const availability = member[1];
        return (
          <div key={member[0]} className="px-5 py-2 border">
            <h2>名前:{member[0]}</h2>
            {availability.map((time: any, index: number) => {
              return <div key={index}>{time}</div>;
            })}
          </div>
        );
      })}
    </div>
  );
};

export default Response;
