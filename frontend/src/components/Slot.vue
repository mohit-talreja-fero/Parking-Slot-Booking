<template>
  <div class="ma-2 border">
    <v-layout row>
      <v-flex class="yellow d-flex justify-center" md4>
        <v-icon x-large color="red" v-if="is_available">mdi-car-back</v-icon>
        <v-icon x-large color="green" v-else>mdi-parking</v-icon>
      </v-flex>
      <v-flex class="light-blue d-flex justify-center py-2" md4>
        <h1 x-large color="red" v-if="is_available">Not Available</h1>
        <h1 x-large color="green" v-else>Available</h1>
      </v-flex>
      <v-flex class="light-green d-flex justify-center" md4>
        <BookDialog class="my-3" :is_available="is_available" />
      </v-flex>
    </v-layout>
  </div>
</template>

<script>
import BookDialog from "@/components/BookDialog.vue";

export default {
  name: "Slot",
  props: ["is_available"],
  components: {
    BookDialog,
  },
  data() {
    return {
      icon: "parking",
    };
  },
};
</script>
