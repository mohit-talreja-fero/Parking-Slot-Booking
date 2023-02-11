export function handleSuccessResponse(res) {
  let obj = res.data;
  return obj;
}

export function handleErrorResponse(err) {
  let obj = {};
  obj.errors = err.response.data;
  return obj;
}
