<template>
  <div>
    <table class="table">
      <th colspan="6" class="header table-primary">Wish list</th>
      <tr>
        <td>Game</td>
        <td>Game name</td>
        <td>Date released</td>
        <td>Actions</td>
      </tr>
      <tr v-for="game in wishListGames" :key="game.gameid">
        <td><img width="125" height="125" :src="game.game.gameImgUrl" /></td>
        <td>{{ game.game.gamename }}</td>
        <td>{{ game.game.datereleased }}</td>
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
  name: "Wishlist",
  data() {
    return {};
  },
  mounted() {
    this.$store.dispatch("getWishlistGames");
  },
  computed: {
    ...mapState(["user", "wishListGames"]),
  },
  methods: {
    deleteGame(game_id) {
      this.$store.dispatch("deleteWishlistGame", game_id);
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
