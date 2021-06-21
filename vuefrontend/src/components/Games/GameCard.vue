<template>
  <div class="card col-xl-4 col-lg-6 col-12 p-4 m-0 border-0 bg-transparent">
    <img
      class="card-img-top bg-dark p-4"
      style="height:200px; object-fit: contain;"
      :src="game.game.gameImgUrl"
      alt="Card image cap"
    />
    <div class="card text-center">
      <div class="card-body">
        <h5 class="card-title">{{ game.game.gamename }}</h5>
        <p class="card-text">Price: {{ game.gameprice }} EUR</p>
        <div>
          <p class="card-text" style="display: inline">Genre:</p>
          <p
            v-for="genre in game.game.genres"
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
          <button type="button" class="btn btn-light">Add to wish list</button>
          <button type="button" class="btn btn-success">Buy</button>
        </div>
        <div
          v-if="
            user !== null && user.is_active === true && user.is_staff === true
          "
        >
          <button type="button" class="btn btn-danger">Delete</button>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: "GameCard",
  props: ["game", "user"],
  data() {
    return {};
  },
};
</script>
