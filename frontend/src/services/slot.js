import { slot } from "../utils/constants";
import { handleErrorResponse, handleSuccessResponse } from "../utils/responseHandlers";

export default (axios) => ({
    getSlotList() {
        return new Promise((resolve, reject) => {
            axios.get(slot.list)
                .then((res) => {
                    resolve(handleSuccessResponse(res));
                })
                .catch((err) => {
                    reject(handleErrorResponse(err));
                });
        })
    },
    getSpaceDetails(id) {
        return new Promise((resolve, reject) => {
            axios.get(`${slot.base}/${id}/`,)
                .then((res) => {
                    resolve(handleSuccessResponse(res));
                })
                .catch((err) => {
                    reject(handleErrorResponse(err));
                });
        })
    }
})