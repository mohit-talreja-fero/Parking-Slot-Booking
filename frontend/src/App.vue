<template>
  <v-app>
    <v-app-bar app color="blue lighten-5" dark>
      <v-row no-gutters class="d-flex justify-start align-center">
        <v-col cols="3" class="yellow">
          <v-row no-gutters>
            <v-col class="d-flex justify-start" cols="2">
              <router-link to="/" class="">Home</router-link>
            </v-col>

            <v-col class="d-flex justify-start" cols="2">
              <router-link to="/about" class="">About</router-link></v-col
            >
            <v-col class="d-flex justify-start" cols="2">
              <router-link to="/slot_list">Slot List</router-link>
            </v-col>
            <v-col class="d-flex justify-start" cols="2">
              <router-link to="/login">Login</router-link>
            </v-col>
            <v-col class="d-flex justify-start" cols="2">
              <router-link to="/login">Register</router-link>
            </v-col>
          </v-row>
        </v-col>
      </v-row>
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
