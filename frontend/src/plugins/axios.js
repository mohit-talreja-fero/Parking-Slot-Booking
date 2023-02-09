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
    // Invalid Token redirect to login
    if (error.response.status == 401) {
      // Vue.prototype.router.push({ name: "login" });
      router.push({ name: "login" });
    }
    return Promise.reject(error); // Require to forceful reject as per Axios Documentation
  }
);

export default axiosObj;
