import AdminDashboard from "@/views/admin/HomeView.vue";

export const admin = [
  {
    path: "/",
    name: "login",
    component: AdminDashboard,
  },
  {
    path: "slot_list/",
    name: "slot-list",
    component: AdminDashboard,
  },
];
