// const { defineConfig } = require("@vue/cli-service");
// module.exports = defineConfig({
//   transpileDependencies: ["vuetify"],
//   lintOnSave: false,
// });

module.exports = {
  transpileDependencies: ["vuetify", "vue-router"],
  chainWebpack: (config) => {
    config.plugin("html").tap((args) => {
      args[0].title = "Parking Slot Booking";
      return args;
    });
  },
};
