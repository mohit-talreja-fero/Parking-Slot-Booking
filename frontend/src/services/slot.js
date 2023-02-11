import { slot } from "@/utils/constant";
import {
  handleErrorResponse,
  handleSuccessResponse,
} from "@/utils/responseHandlers";

export default (axios) => ({
  getSlotList() {
    return new Promise((resolve, reject) => {
      axios
        .get(slot.list)
        .then((res) => {
          resolve(handleSuccessResponse(res));
        })
        .catch((err) => {
          reject(handleErrorResponse(err));
        });
    });
  },
  getSpaceDetails(id) {
    return new Promise((resolve, reject) => {
      axios
        .get(`${slot.base}/${id}/`)
        .then((res) => {
          resolve(handleSuccessResponse(res));
        })
        .catch((err) => {
          reject(handleErrorResponse(err));
        });
    });
  },
  showAvailableSlots(params) {
    return new Promise((resolve, reject) => {
      axios
        .get(slot.show_available_slots, params)
        .then((res) => {
          resolve(handleSuccessResponse(res));
        })
        .catch((err) => {
          reject(handleErrorResponse(err));
        });
    });
  },
});
