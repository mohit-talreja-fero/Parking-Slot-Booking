<template>
  <div>
    <h1>Slot List Page</h1>
    <li v-for="slot in slots" :key="slot.id">
      <v-chip class="ma-2" color="primary"> Primary </v-chip>
    </li>
  </div>
</template>

<script>
export default {
  name: "SlotList",
  data() {
    return {
      slots: [],
    };
  },
  beforeMount() {
    this.slots = [];
    this.getSlotList();
  },
  methods: {
    async getSlotList() {
      await this.$api.slot
        .getSlotList()
        .then((res) => {
          this.slots = res;
        })
        .catch((err) => {
          console.error(err);
        });
      console.log("----------->", this.slots);
    },
  },
};
</script>

<style></style>
