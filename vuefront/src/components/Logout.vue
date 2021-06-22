<template>
  <div class="log"></div>
</template>

<script>
import router from "../router/router";
export default {
  created() {
    this.$store.dispatch("logout").then(() => {
      router.push("/login");
    });
  },
};
</script>
