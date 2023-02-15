<template>
  <v-app>
    <v-app-bar app color="blue lighten-5" dark>
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
      </v-row>
      <!-- <template v-slot:extension>
        <v-tabs v-model="tab" align-with-title dark>
          <v-tabs-slider color="indigo accent-4"></v-tabs-slider>
          <v-tab to="/slot_list" class="text-color blue--text">
            Slot List
          </v-tab>
          <v-tab to="/space_list"> Space List </v-tab>
        </v-tabs>
      </template> -->
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
    tab: null,
    hover1: false,
    hover2: false,
    hover3: false,
    items: ["A", "B"],
  }),
};
</script>
