export function handleSuccessResponse(res) {
    let obj = {};
    // console.log(res.data);
    if (Array.isArray(res.data)) {
        obj = res.data;
    } else {
        obj = res.data.data;
    }
    // console.log(obj);
    return obj;
}

export function handleErrorResponse(err) {
    let obj = {};
    console.error(err);
    return obj;
}
