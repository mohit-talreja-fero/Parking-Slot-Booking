import space from "../services/space";
import slot from "../services/slot";
import axiosObj from "./axios";

export default {
  space: space(axiosObj),
  slot: slot(axiosObj),
};
