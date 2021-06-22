<template>
  <div>
    <table class="table">
      <th colspan="6" class="header table-primary">Game Library</th>
      <tr>
        <td>Game</td>
        <td>Game name</td>
        <td>Date released</td>
        <td>Total time played</td>
        <td>Last time played</td>
        <td>Actions</td>
      </tr>
      <tr v-for="game in libraryGames" :key="game.gameid">
        <td><img width="125" height="125" :src="game.game.gameImgUrl" /></td>
        <td>{{ game.game.gamename }}</td>
        <td>{{ game.game.datereleased }}</td>
        <td>{{ game.totaltimeplayed }}</td>
        <td>{{ game.lasttimeplayed }}</td>
        <td>
          <button
            type="button"
            style="background: red"
            @click="deleteGame(game.game.gameid)"
          >
            <font-awesome-icon icon="trash" class="trash-icon" />
          </button>
        </td>
      </tr>
    </table>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "Gamelibrary",
  data() {
    return {};
  },
  mounted() {
    this.$store.dispatch("getLibraryGames");
  },
  computed: {
    ...mapState(["user", "libraryGames"]),
  },
  methods: {
    deleteGame(game_id) {
      this.$store.dispatch("deleteLibraryGame", game_id);
    },
  },
};
</script>

<style scoped>
.header {
  text-align: center;
}
tr {
  text-align: center;
}
</style>
