<template>
  <div>
    <h1>Slot List Page</h1>

    <v-container v-for="slot in slots" :key="slot.id">
      <Slot :is_available="slot.is_available" />
    </v-container>
  </div>
</template>

<script>
import Slot from "@/components/Slot.vue";
export default {
  name: "SlotList",
  components: { Slot },
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
    },
    whichClicked(id) {
      console.log(id);
    },
  },
};
</script>

<style></style>
