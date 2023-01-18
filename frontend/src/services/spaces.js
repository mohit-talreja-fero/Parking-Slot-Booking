import { space } from "../utils/constants";
import { handleErrorResponse, handleSuccessResponse } from "../utils/responseHandlers";

export default (axios) => ({
    getSpaceList() {
        return new Promise((resolve, reject) => {
            axios.get(space.base)
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
            axios.get(`${space.base}/${id}/`,)
                .then((res) => {
                    resolve(handleSuccessResponse(res));
                })
                .catch((err) => {
                    reject(handleErrorResponse(err));
                });
        })
    }
})