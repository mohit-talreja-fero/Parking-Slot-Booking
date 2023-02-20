import VueRouter from "vue-router";
import Login from "@/views/login/Login.vue";
import Default from "@/layout/Default.vue";
import PageNotFound from "@/components/Common/PageNotFound";
import HomeView from "../views/admin/HomeView.vue";
import BookingPage from "@/views/admin/BookingPage";

const routes = [
  {
    path: "/login",
    name: "login",
    component: Login,
  },
  {
    path: "/app",
    component: Default,
    children: [
      {
        path: "",
        name: "home",
        component: HomeView,
      },
      {
        path: "book",
        name: "BookingPage",
        component: BookingPage,
      },
    ],
  },
  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    component: PageNotFound,
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

// Use navigation guard for preventing access of non-super users router.beforeEach

export default router;
