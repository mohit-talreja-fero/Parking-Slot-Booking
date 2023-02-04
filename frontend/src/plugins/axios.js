import axios from "axios";

let baseUrl = "http://127.0.0.1:6969/";

const axiosObj = axios.create({
  baseURL: baseUrl,
});

export default axiosObj;
