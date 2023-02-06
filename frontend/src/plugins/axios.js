import axios from "axios";
// import Vue from "vue";
import router from "@/router";

let baseUrl = "http://127.0.0.1:6969/";

const axiosObj = axios.create({
  baseURL: baseUrl,
});

axiosObj.interceptors.request.use(
  (config) => {
    let url = config.url;
    if (!url.includes("login")) {
      let token = localStorage.getItem("token");
      config.headers["Authorization"] = `Token ${token}`;
    }
    return config;
  },
  (error) => {
    return error;
  }
);

axiosObj.interceptors.response.use(
  (config) => {
    return config;
  },
  (error) => {
    console.log(error.response);
    if (error.response.status == 401) {
      router.push({ name: "login" });
    }
    return error;
  }
);

export default axiosObj;
