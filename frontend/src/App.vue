<template>
  <v-app>
    <v-app-bar app color="blue lighten-5" dark>
      <v-row no-gutters class="d-flex justify-start align-center">
        <v-img :src="imgPath" max-height="230" max-width="180"></v-img>
        <v-hover v-slot="{ hover1 }">
          <v-btn
            to="/space_list"
            class="mx-4 blue lighten-5 text-color blue--text"
            :text="!hover1"
            >Spaces</v-btn
          >
        </v-hover>
        <v-hover v-slot="{ hover2 }">
          <v-btn
            to="/slot_list"
            class="mx-4 blue lighten-5 text-color blue--text"
            :text="!hover2"
            >Slots</v-btn
          >
        </v-hover>
      </v-row>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
import logoPng from "@/assets/logo.png";
export default {
  name: "App",

  data: () => ({
    imgPath: logoPng,
    hover1: false,
    hover2: false,
  }),
};
</script>
