<template>
  <div>
    <table class="table">
      <th colspan="6" class="header table-primary">Game Library</th>
      <tr>
        <td>Game</td>
        <td>Game name</td>
        <td>Date released</td>
        <td>Game description</td>
        <td>Genre</td>
        <td>Actions</td>
      </tr>
      <tr v-for="game in games" :key="game.gameid">
        <td><img width="125" height="125" :src="game.gameImgUrl" /></td>
        <td>{{ game.gamename }}</td>
        <td>{{ game.datereleased }}</td>
        <td>{{ game.gamedescription }}</td>
        <td>PLACEHOLDER</td>
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
  name: "Games",
  data() {
    return {};
  },
  mounted() {
    this.$store.dispatch("getAllGames");
  },
  computed: {
    ...mapState(["games"]),
  },
  methods: {},
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
