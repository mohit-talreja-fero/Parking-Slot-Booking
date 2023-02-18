import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import axiosObj from "../src/plugins/axios";
import api from "../src/plugins/api";
import VueRouter from "vue-router";

Vue.prototype.$axios = axiosObj;
Vue.prototype.$api = api;
Vue.use(VueRouter);
Vue.config.productionTip = false;

new Vue({
  router,
  vuetify,
  render: (h) => h(App),
}).$mount("#app");
