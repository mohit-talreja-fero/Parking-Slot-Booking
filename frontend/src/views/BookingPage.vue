<template>
  <div>
    <h1 v-if="isBookedSuccessfully">Booked Successfully!</h1>
    <h2 v-if="isBookedSuccessfully">Redirecting to home page ...</h2>
    <h1 class="ma-5">Booking Date: {{ date }}</h1>
    <!-- Date Picker -->
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

    <!-- Start and End Time pickers -->
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
            :error-messages="error.start_time"
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
        :error-messages="error.end_time"
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
      class="mt-5"
      :disabled="!(start_time && end_time)"
      @click="checkSlotAvailability"
      >Check Slot Availability</v-btn
    >

    <!-- Slot Listing -->
    <div v-if="slots.length > 0" class="ma-5">
      <v-row>
        <v-card
          v-for="slot in slots"
          :key="slot.id"
          class="ma-5"
          :class="slot.availability ? `light-blue` : `red`"
          max-width="210"
          max-height="250"
          border="right"
          dark
        >
          <v-card-title>
            <span class="text-h6 font-weight">Slot ID: {{ slot.id }}</span>
          </v-card-title>

          <v-card-text class="blue--text" v-if="slot.availability">
            <v-btn @click="bookSlot(slot.id)">Book Slot</v-btn>
          </v-card-text>
          <v-card-text class="white--text" v-else>
            <span>Slot Not Available</span>
          </v-card-text>
        </v-card>
      </v-row>
    </div>
  </div>
</template>

<script>
import {
  getToday,
  dateTimeConstructor,
  waitForNSeconds,
} from "@/utils/functions";
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
      slots: [],
      isBookedSuccessfully: false,
      error: [],
      showError: false,
    };
  },
  methods: {
    async checkSlotAvailability() {
      await this.$api.slot
        .showAvailableSlots({
          params: {
            start_time: dateTimeConstructor(this.date, this.start_time),
            end_time: dateTimeConstructor(this.date, this.end_time),
          },
        })
        .then((res) => {
          this.slots = res;
        })
        .catch((err) => {
          this.error = err;
        });
    },
    bookSlot(id) {
      if (this.start_time >= this.end_time) {
        this.showError = true;
        return;
      }
      this.$api.slot
        .bookMySlot(id, {
          start_time: dateTimeConstructor(this.date, this.start_time),
          end_time: dateTimeConstructor(this.date, this.end_time),
        })
        .then(async () => {
          this.isBookedSuccessfully = true;
          await waitForNSeconds(3);
          this.$router.push({ name: "home" });
        })
        .catch((err) => {
          this.error = err.errors;
          this.showError = true;
        });
    },
  },
};
</script>
