<template>
  <form action="javascript:void(0);" class="card-body">
    Game:
    <select v-model="selectedGame.game" class="form-control" required>
      <option v-for="game in games" :key="game.gameid" :value="game.gamename">{{
        game.gamename
      }}</option>
    </select>
    Price:
    <input
      v-model="selectedGame.price"
      type="number"
      class="form-control"
      required
    />
    Discount:
    <input
      v-model="selectedGame.discount"
      type="number"
      step=".01"
      class="form-control"
      required
    />
    <input
      type="submit"
      value="Add"
      class="btn btn-dark m-4"
      @click="AddGameToPlayStore"
    />
  </form>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "AddForm",
  data() {
    return {
      selectedGame: {
        game: "Heartstone",
      },
      gamesToAdd: [],
    };
  },
  methods: {
    AddGameToPlayStore() {
      this.$store.dispatch(
        "addGameToPlaystore",
        this.selectedGame,
        this.selectedGame.game.gameid
      );
    },
  },
  mounted() {
    this.$store.dispatch("getAllGames");
    // this.$store.dispatch("getAllGamesFromPlaystore").then(() => {
    //   this.gamesToAdd = games.filter((game) => !gamesPlaystore.includes(game));
    // });
  },
  computed: {
    ...mapState(["games", "gamesPlaystore"]),
  },
};
</script>
