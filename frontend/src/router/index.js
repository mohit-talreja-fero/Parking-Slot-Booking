import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import SlotList from "../views/SlotList.vue";
import Login from "@/components/Common/Login.vue";
// import BookSlot from "@/views/BookSlot";
import SpaceList from "@/views/SpaceList.vue";
import PageNotFound from "@/components/Common/PageNotFound";
import BookingPage from "@/views/BookingPage";

// import Registration from "@/components/Common/Registeration.vue";

Vue.use(VueRouter);

const routes = [
  {
    path: "/login",
    name: "login",
    component: Login,
  },
  // {
  //   path: "/register",
  //   name: "register",
  //   component: Registration,
  // },
  {
    path: "/",
    name: "home",
    component: HomeView,
    // children: [
    //   {
    //     path: "book/",
    //     name: "book",
    //     component: BookSlot,
    //   },
    // ],
  },
  {
    path: "/space_list",
    name: "space_list",
    component: SpaceList,
  },
  {
    path: "/slot_list",
    name: "slot_list",
    component: SlotList,
  },
  {
    path: "/book",
    name: "BookingPage",
    component: BookingPage,
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
