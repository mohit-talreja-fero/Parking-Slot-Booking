<template>
  <v-app>
    <v-app-bar app>
      <h1>PARKING SLOT BOOKING</h1>

      <div class="ml-3 flex">
      <router-link class="mr-5" to="/">Home</router-link>
      <router-link class="mr-5" to="/about">About</router-link>
      <router-link class="mr-5" to="/slot_list">Slot List</router-link>
      </div>
    </v-app-bar>

    <v-main>
      <router-view />
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: "App",

  data: () => ({
    //
  }),
};
</script>
