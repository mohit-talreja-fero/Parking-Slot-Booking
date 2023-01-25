import axios from "axios";

let baseUrl = "http://127.0.0.1:8000/";

const axiosObj = axios.create({
  baseURL: baseUrl,
});

export default axiosObj;
