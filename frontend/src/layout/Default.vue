<template>
  <div>
    <v-app-bar app color="blue lighten-5" class="mb-5" dark>
      <v-row no-gutters class="d-flex justify-start align-center">
        <v-img :src="imgPath" max-height="230" max-width="180"></v-img>
        <v-btn
          to="/space_list"
          class="mx-4 blue lighten-5 text-color blue--text"
          >Spaces</v-btn
        >
        <v-btn to="/slot_list" class="mx-4 blue lighten-5 text-color blue--text"
          >Slots</v-btn
        >
        <v-btn to="/book" class="mx-4 blue lighten-5 text-color blue--text"
          >Book My Slot</v-btn
        >
        <v-spacer></v-spacer>
        <v-btn class="mx-4 blue lighten-5 text-color blue--text" @click="logout"
          >Log Out</v-btn
        >
      </v-row>
    </v-app-bar>
    <v-main>
      <router-view />
    </v-main>
  </div>
</template>

<script>
import logoPng from "@/assets/logo.png";
export default {
  name: "Default",
  data() {
    return {
      imgPath: logoPng,
    };
  },
  methods: {
    logout() {
      this.$api.account
        .logout()
        .then(() => {
          // Clearing localstorage and redirect user to login
          localStorage.clear();
          this.$router.push("/login");
        })
        .catch((err) => console.log(err));
    },
  },
};
</script>
