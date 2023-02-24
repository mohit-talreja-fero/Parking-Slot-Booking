export const slotBase = "/parking/slot";
export const accountBase = "account";

export const space = {
  base: "/parking/space",
};

export const slot = {
  list: `${space.base}/1/slot_list`, // remove the constant "1"
  show_available_slots: `${slotBase}/show_available_slots`,
  // book_my_slot: `${slotBase}/${id}/book_my_slou`,
};

export const account = {
  login: `${accountBase}/login/`,
  logout: `${accountBase}/logout/`,
  register: `${accountBase}/create/`,
};
