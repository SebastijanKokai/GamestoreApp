<template>
  <div style="min-height: calc(100vh - 45.88px)" class="bg-light">
    <div class="row p-0 m-0">
      <AddForm
        v-if="user !== null && user.is_staff === true"
        v-bind:games="this.games"
      />
      <GameCard
        v-for="game in games"
        v-bind:key="game.gameid"
        v-bind:game="game"
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
    return {
      games: [],
    };
  },
  async mounted() {
    var response = await fetch("http://localhost:8000/gamestore/");
    this.games = await response.json();
  },
  computed: {
    ...mapState(["user"]),
  },
};
</script>
