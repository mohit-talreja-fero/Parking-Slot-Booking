<template>
  <v-app>
    <v-app-bar app color="blue lighten-5" dark>
      <div>
        <router-link to="/" class="ma-5">Home</router-link>
        <router-link to="/about" class="mr-5">About</router-link>
        <router-link to="/slot_list">Slot List</router-link>
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
