<template>
  <div>
    <h1 class="ma-5">Booking Date: {{ date }}</h1>
    <!-- <v-menu
      ref="menu"
      v-model="date_menu"
      :close-on-content-click="false"
      :nudge-right="40"
      :return-value.sync="date"
      transition="scale-transition"
      offset-y
      max-width="290px"
      min-width="290px"
      outline
    >
      <template v-slot:activator="{ on, attrs }">
        <v-text-field
          max-width="290px"
          min-width="290px"
          v-model="date"
          prepend-icon="mdi-calendar-check"
          readonly
          v-bind="attrs"
          v-on="on"
        ></v-text-field>
      </template>
      <v-row justify="center">
        <v-date-picker v-model="date"></v-date-picker>
      </v-row>
    </v-menu> -->
    <v-menu
      v-model="date_menu"
      :close-on-content-click="false"
      :nudge-right="40"
      transition="scale-transition"
      offset-y
      min-width="auto"
    >
      <template v-slot:activator="{ on, attrs }">
        <v-text-field
          v-model="date"
          label="Picker without buttons"
          prepend-icon="mdi-calendar"
          readonly
          v-bind="attrs"
          v-on="on"
        ></v-text-field>
      </template>
      <v-date-picker v-model="date" @input="date_menu = false"></v-date-picker>
    </v-menu>

    <!-- Start and End Time -->
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
          :max="end_time"
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
    <v-btn
      color="blue"
      :disabled="!(start_time && end_time)"
      @click="checkSlotAvailability"
      >Check Slot Availability</v-btn
    >
  </div>
</template>

<script>
import { getToday } from "@/utils/functions";
export default {
  name: "BookingPage",
  data() {
    return {
      date: getToday(),
      start_time: null,
      end_time: null,
      start_time_menu: false,
      end_time_menu: false,
      date_menu: false,
      time: null,
      menu2: false,
      modal2: false,
    };
  },
  methods: {
    async checkSlotAvailability() {
      await this.$api.slot
        .showAvailableSlots({
          params: {
            start_time: `${this.date} ${this.start_time}`,
            end_time: `${this.date} ${this.start_time}`,

            // example
            // start_time: "2023-01-26 13:59",
            // end_time: "2023-01-27 22:00",
          },
        })
        .then((res) => console.log(res))
        .catch((err) => console.log(err));
    },
  },
};
</script>
