<template>
  <div class="card col-xl-4 col-lg-6 col-12 p-4 m-0 border-0 bg-transparent">
    <img
      v-if="game"
      class="card-img-top bg-dark p-4"
      style="height:200px; object-fit: contain;"
      :src="game.gameImgUrl"
      alt="Card image cap"
    />
    <div class="card text-center">
      <div class="card-body">
        <h5 v-if="game" class="card-title">{{ game.gamename }}</h5>
        <p v-if="game" class="card-text">Price: {{ info.gameprice }} EUR</p>
        <div v-if="game">
          <p class="card-text" style="display: inline">Genre:</p>
          <p
            v-for="genre in game.genres"
            :key="genre.genreid"
            style="display: inline"
          >
            {{ genre.genre + ", " }}
          </p>
        </div>
        <br />
        <div
          v-if="
            user !== null &&
              user.is_active === true &&
              user.is_staff === false &&
              user.is_superuser === false
          "
        >
          <button type="button" class="btn btn-light" @click="addToWishlist">
            Add to wish list
          </button>
          <button type="button" class="btn btn-success" @click="buyGame">
            Buy
          </button>
        </div>
        <div
          v-if="
            user !== null && user.is_active === true && user.is_staff === true
          "
        >
          <button
            type="button"
            class="btn btn-danger"
            @click="deleteGame(info.playstorerow)"
          >
            Delete
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "GameCard",
  props: ["game", "user", "info"],
  data() {
    return {};
  },
  methods: {
    buyGame() {
      this.$store.dispatch("buyGame", this.game.gameid);
    },
    addToWishlist() {
      this.$store.dispatch("addToWishlist", this.game.gameid);
    },
    deleteGame(playstorerow) {
      this.$store.dispatch("deleteGameFromPlaystore", playstorerow).then(() => {
        alert("Game has been deleted from the playstore.");
      });
    },
  },
};
</script>
