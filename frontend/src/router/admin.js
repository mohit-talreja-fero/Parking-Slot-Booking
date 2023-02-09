import slotRoute from "./slot";

export const admin = [
  {
    path: "/admin",
    name: "login",
    children: [...slotRoute],
  },
];
