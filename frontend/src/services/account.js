import { account } from "@/utils/constant";
import {
  handleErrorResponse,
  handleSuccessResponse,
} from "@/utils/responseHandlers";

export default (axios) => ({
  login(payload) {
    return new Promise((resolve, reject) => {
      axios
        .post(account.login, payload)
        .then((res) => {
          resolve(handleSuccessResponse(res));
        })
        .catch((err) => {
          reject(handleErrorResponse(err));
        });
    });
  },
  logout(payload) {
    return new Promise((resolve, reject) => {
      axios
        .post(account.logout, payload)
        .then((res) => {
          resolve(handleSuccessResponse(res));
        })
        .catch((err) => {
          reject(handleErrorResponse(err));
        });
    });
  },
  profile() {},
  register(payload) {
    return new Promise((resolve, reject) => {
      axios
        .post(account.register, payload)
        .then((res) => {
          resolve(handleSuccessResponse(res));
        })
        .catch((err) => {
          reject(handleErrorResponse(err));
        });
    });
  },
});
