<template>
  <div style="min-height: calc(100vh - 45.88px)" class="bg-light">
    <div class="row p-0 m-0">
      <AddForm v-if="user !== null && user.is_staff === true" />
      <GameCard
        v-for="game in gamesPlaystore"
        v-bind:key="game.playstorerow"
        v-bind:game="game.game"
        v-bind:info="game"
        v-bind:user="user"
      />
    </div>
  </div>
</template>

<script>
import GameCard from "./GameCard.vue";
import AddForm from "./AddForm.vue";
import { mapState } from "vuex";

export default {
  name: "Playstore",
  components: {
    GameCard,
    AddForm,
  },
  data() {
    return {};
  },
  mounted() {
    this.$store.dispatch("getAllGamesFromPlaystore");
  },
  computed: {
    ...mapState(["user", "gamesPlaystore"]),
  },
};
</script>
