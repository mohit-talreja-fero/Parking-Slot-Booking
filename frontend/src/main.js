import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axiosObj from "../src/plugins/axios";
import api from "../src/plugins/api";


Vue.prototype.$axios = axiosObj;
Vue.prototype.$api = api;

Vue.config.productionTip = false

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')
