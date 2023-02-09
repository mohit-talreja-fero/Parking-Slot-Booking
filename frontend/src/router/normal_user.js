import BookSlot from "@/views/BookSlot";
import Account from "@/views/Account";
// import BookingHistory from "@/views/BookingHistory";

export const normal_user = [
  //   {
  //     path: "/",
  //     name: "booking_history",
  //     component: BookingHistory,
  //   },
  {
    path: "book/",
    name: "book",
    component: BookSlot,
  },
  {
    path: "account/",
    name: "account",
    component: Account,
  },
];
