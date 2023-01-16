<template>
  <h1>Hello World</h1>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
  },
  mounted() {
    console.log("Hello World");
    this.$api.space.getSpaceList({ params: "" });
  },
};
</script>

