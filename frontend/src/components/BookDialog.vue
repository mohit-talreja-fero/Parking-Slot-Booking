<template>
  <div>
    <v-dialog v-model="dialog" max-width="700">
      <template v-slot:activator="{ on, attrs }">
        <v-btn
          color="blue"
          dark
          v-bind="attrs"
          :disabled="is_available"
          v-on="on"
        >
          Book Slot
        </v-btn>
      </template>

      <v-card>
        <v-card-title class="text-h5 grey lighten-2 mb-3">
          Choose Time slot
          <v-spacer></v-spacer>
          <v-icon @click="dialog = false"> mdi-window-close</v-icon>
        </v-card-title>

        <!-- <TimePicker /> -->
        <v-divider></v-divider>
        <v-row justify="space-around" align="center">
          <v-col style="width: 350px; flex: 0 1 auto">
            <v-time-picker
              v-model="start_time"
              :max="end_time"
              format="24hr"
              :rules="inputRules"
            ></v-time-picker>
          </v-col>
          <v-col style="width: 350px; flex: 0 1 auto">
            <v-time-picker
              v-model="end_time"
              :min="start_time"
              format="24hr"
            ></v-time-picker>
          </v-col>
        </v-row>
        <v-card-actions>
          <v-btn
            class="light-blue mt-5"
            text
            color="white"
            flat
            :disabled="!(start_time && end_time)"
            @click="bookSlot"
            >Book Slot</v-btn
          >
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
// import TimePicker from "@/components/Common/TimePicker.vue";
export default {
  name: "BookDialog",
  props: ["is_available"],
  data() {
    return {
      dialog: false,
      date: this.getToday(),
      start_time: null,
      end_time: null,
    };
  },
  // components: { TimePicker },
  methods: {
    bookSlot() {
      console.log(this.start_time);
      console.log(this.end_time);
      this.dialog = false;
    },
    getToday() {
      return new Date().toISOString().slice(0, 10);
    },
    getBookingDate() {
      return this.getToday();
    },
    getCurrentTime() {
      return new Date().toISOString().slice(11, 16);
    },
  },
};
</script>
