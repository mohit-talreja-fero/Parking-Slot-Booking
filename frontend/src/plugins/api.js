import space from "../services/space";
import slot from "../services/slot";
import axiosObj from "./axios";
import account from "@/services/account";

export default {
  space: space(axiosObj),
  slot: slot(axiosObj),
  account: account(axiosObj),
};
