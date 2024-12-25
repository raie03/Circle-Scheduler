import ResponseDisplay from "@/app/components/ResponseDisplay";

async function getResponseData() {
  const response = await fetch("http://127.0.0.1:8000/scheduleTest", {
    cache: "no-store",
  });

  const responseData = await response.json();

  return responseData;
}

const Response = async () => {
  const responseData = await getResponseData();
  const { input_data } = responseData;
  // const member_availability = input_data.member_availability;
  // console.log(member_availability);

  return <ResponseDisplay input_data={input_data} />;
};

export default Response;
