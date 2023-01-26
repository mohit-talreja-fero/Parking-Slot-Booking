<template>
  <div>
    <v-dialog v-model="dialog" max-width="700">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="red lighten-2" dark v-bind="attrs" v-on="on">
          Book Slot
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="text-h5 grey lighten-2 mb-3">
          Choose Date and Time
          <v-spacer></v-spacer>
          <v-icon @click="dialog = false"> mdi-window-close</v-icon>
        </v-card-title>

        <v-card-text>
          <v-row class="mb-4">
            <v-date-picker
              v-model="start_date"
              class="mr-5"
              :min="getToday()"
            ></v-date-picker>
            <v-time-picker v-model="start_time" format="24hr"></v-time-picker>
          </v-row>
          <v-row>
            <v-date-picker
              v-model="end_date"
              class="mr-5"
              :min="getToday()"
            ></v-date-picker>
            <v-time-picker v-model="end_time" format="24hr"></v-time-picker>
          </v-row>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="primary" text @click="bookSlot">Book Slot</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
export default {
  name: "BookDialog",
  data() {
    return {
      dialog: false,
      start_date: this.getToday(),
      start_time: "",
      end_date: this.getToday(),
      end_time: "",
    };
  },
  methods: {
    bookSlot() {
      console.log(this.start_date, this.start_time);
      console.log(this.end_date, this.end_time);
      this.dialog = false;
    },
    getToday() {
      return new Date().toISOString().slice(0, 10);
    },
    getCurrentTime() {
      return new Date().toISOString().slice(11, 16);
    },
  },
};
</script>
