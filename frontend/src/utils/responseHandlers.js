export function handleSuccessResponse(res) {
  let obj = {};
  if (Array.isArray(res.data)) {
    obj = res.data.data;
    // console.log("is array");
  } else {
    obj = res.data;
    // console.log("is not array");
  }
  return obj;
}

export function handleErrorResponse(err) {
  let obj = {};
  obj.errors = err.response.data;
  return obj;
}
