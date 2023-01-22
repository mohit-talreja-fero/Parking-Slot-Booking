import space from "../services/spaces";
import slot from "../services/slot";
import axiosObj from "./axios";


export default {
    // space: space(axiosObj),
    space: space(axiosObj),
    slot: slot(axiosObj),
}
