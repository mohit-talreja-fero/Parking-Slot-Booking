<template>
  <div>
    <v-dialog v-model="dialog" max-width="820">
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

      <v-card class="pa-5" style="width: auto">
        <v-card-title
          class="text-h5 grey lighten-2 mb-7 mt-0"
          style="width: auto"
        >
          Choose Time Slot
          <v-spacer></v-spacer>
          <v-icon @click="dialog = false"> mdi-window-close</v-icon>
        </v-card-title>

        <!-- <TimePicker /> -->

        <v-row>
          <v-menu
            ref="menu2"
            v-model="start_time_menu"
            :close-on-content-click="false"
            :nudge-right="40"
            :return-value.sync="start_time"
            transition="scale-transition"
            offset-y
            max-width="290px"
            min-width="290px"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="start_time"
                label="Start Time"
                prepend-icon="mdi-clock-time-four-outline"
                readonly
                v-bind="attrs"
                v-on="on"
                class="mx-3"
              ></v-text-field>
            </template>
            <v-time-picker
              v-if="start_time_menu"
              v-model="start_time"
              full-width
              @click:minute="$refs.menu2.save(start_time)"
              format="24hr"
            ></v-time-picker>
          </v-menu>
          <!-- END TIME -->
          <v-menu
            ref="menu"
            v-model="end_time_menu"
            :close-on-content-click="false"
            :nudge-right="40"
            :return-value.sync="end_time"
            transition="scale-transition"
            offset-y
            max-width="290px"
            min-width="290px"
            outline
          >
            <template v-slot:activator="{ on, attrs }">
              <v-text-field
                v-model="end_time"
                label="End Time"
                prepend-icon="mdi-clock-time-four-outline"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-text-field>
            </template>
            <v-time-picker
              v-if="end_time_menu"
              v-model="end_time"
              full-width
              @click:minute="$refs.menu.save(end_time)"
              format="24hr"
              :min="start_time"
            ></v-time-picker>
          </v-menu>
        </v-row>
        <v-card-actions>
          <v-btn
            class="light-blue mt-5"
            text
            color="white"
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
  props: ["is_available", "slot_id"],
  data() {
    return {
      dialog: false,
      date: this.getToday(),
      start_time: null,
      end_time: null,
      start_time_menu: false,
      end_time_menu: false,
      time: null,
      menu2: false,
      modal2: false,
    };
  },
  // components: { TimePicker },
  methods: {
    bookSlot() {
      console.log(this.start_time);
      console.log(this.end_time);
      this.dialog = false;
      // console.log(this.slot_id);
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
