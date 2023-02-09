<template>
  <v-app>
    <v-main>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Login form</v-toolbar-title>
              </v-toolbar>
              <v-card-text>
                <div v-for="err in non_field_errors" :key="err.id">
                  <v-alert border="top" color="red" dark v-if="showToast">
                    <v-row class="ma-1">
                      {{ err[0] }}
                      <v-spacer></v-spacer>
                      <v-icon @click="showToast = false"
                        >mdi-close</v-icon
                      ></v-row
                    >
                  </v-alert>
                </div>
                <form ref="form" @submit.prevent="login()">
                  <v-text-field
                    v-model="username"
                    name="username"
                    label="Username"
                    type="text"
                    placeholder="username"
                    required
                  ></v-text-field>

                  <v-text-field
                    v-model="password"
                    name="password"
                    label="Password"
                    type="password"
                    placeholder="password"
                    required
                  ></v-text-field>
                  <v-btn
                    type="submit"
                    class="mt-4 mr-5"
                    color="primary"
                    value="log in"
                    >Login</v-btn
                  >
                  <v-btn
                    type="submit"
                    class="mt-4"
                    color="primary"
                    value="log in"
                    >Register</v-btn
                  >
                </form>
              </v-card-text>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      username: "",
      password: "",
      showToast: true,
      non_field_errors: [],
    };
  },
  methods: {
    async login() {
      await this.$api.account
        .login({
          username: this.username,
          password: this.password,
        })
        .then((res) => {
          localStorage.setItem("token", res.token);
          localStorage.setItem("user_type", res.user_type);
          let user_type = res.user_type;
          if (user_type == "NORMAL") {
            this.$router.push({ name: "admin_app_bar" });
          } else {
            this.$router.push({ name: "space_list" });
          }
        })
        .catch((err) => {
          console.log("BBBBL ", err);
          this.showToast = true;
          this.non_field_errors = err.errors;
        });
    },
  },
};
</script>
