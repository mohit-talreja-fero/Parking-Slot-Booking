export function handleSuccessResponse(res) {
  let obj = res.data;
  return obj;
}

export function handleErrorResponse(err) {
  console.log(err.response.data);
  let obj = {};
  obj = err.response.data;
  return obj;
}
