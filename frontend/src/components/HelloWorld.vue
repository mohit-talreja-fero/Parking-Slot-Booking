<template>
  <div>
    <SlotTray />
  </div>
</template>

<script>
import SlotTray from "./Common/SlotTray.vue";
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  components: {
    SlotTray,
  },
  mounted() {
    // this.$api.space.getSpaceList();
    this.$api.space.getSpaceDetails(1);
  },
};
</script>

