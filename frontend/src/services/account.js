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
  register() {
    return new Promise((resolve, reject) => {
      axios
        .get(account.register)
        .then((res) => {
          resolve(handleSuccessResponse(res));
        })
        .catch((err) => {
          reject(handleErrorResponse(err));
        });
    });
  },
});
