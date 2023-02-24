<template>
  <v-app>
    <v-main>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <v-flex xs12 sm8 md4>
            <v-card class="elevation-12">
              <v-toolbar dark color="primary">
                <v-toolbar-title>Registration form</v-toolbar-title>
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
                <form
                  class="px-3 py-4"
                  ref="form"
                  @submit.prevent="redirectToHome()"
                >
                  <v-text-field
                    v-model="first_name"
                    name="first_name"
                    label="First Name"
                    type="text"
                    :error-messages="error && error.first_name"
                    placeholder="First Name"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="last_name"
                    name="last_name"
                    :error-messages="error && error.last_name"
                    label="Last Name"
                    type="text"
                    placeholder="Last Name"
                    required
                  ></v-text-field>
                  <v-text-field
                    v-model="username"
                    :error-messages="error && error.username"
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

                  <v-checkbox
                    v-model="has_premium"
                    label="Activate Premium member ship ?"
                  ></v-checkbox>

                  <v-row class="mt-3"
                    ><v-btn
                      type="submit"
                      class="mt-4"
                      color="primary"
                      value="log in"
                      @click="register"
                      :disabled="!(first_name && last_name && username)"
                      >Register</v-btn
                    >
                    <v-spacer></v-spacer>
                    <v-btn
                      type="submit"
                      class="mt-4 mr-5"
                      color="white blue--text"
                      value="log in"
                      @click="redirectToLogin()"
                      >Go to Login Page</v-btn
                    ></v-row
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
  name: "App",
  data() {
    return {
      username: "",
      first_name: "",
      last_name: "",
      password: "",
      has_premium: false,
      non_field_errors: [],
      error: "",
    };
  },
  methods: {
    redirectToHome() {
      const { username } = this;
      console.log(username + "logged in");
    },
    redirectToLogin() {
      this.$router.push("/login");
    },
    async register() {
      await this.$api.account
        .register({
          first_name: this.first_name,
          last_name: this.last_name,
          username: this.username,
          password: this.password,
          has_premium: this.has_premium,
        })
        .then((res) => {
          console.log(res);
          this.$router.push("/home");
        })
        .catch((err) => {
          this.error = err;
        });
    },
  },
};
</script>
