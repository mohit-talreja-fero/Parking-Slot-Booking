<template>
  <div>
    <template>
      <v-row class="d-flex" justify="center">
        <v-menu v-model="showMenu" absolute offset-y style="max-width: 600px">
          <template v-slot:activator="{ on, attrs }">
            <v-text-field
              v-bind="attrs"
              v-on="on"
              label="Choose Time"
              width="500"
            ></v-text-field>
          </template>
          <v-time-picker v-model="start_time" format="24hr"></v-time-picker>
        </v-menu>
      </v-row>
    </template>
  </div>
</template>
<script>
export default {
  name: "TimePicker",
};
</script>
