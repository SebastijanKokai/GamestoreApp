<template>
  <form action="javascript:void(0);" class="card-body">
    Game:
    <select class="form-control" required>
      <option
        v-for="game in games"
        :key="game.game.gameid"
        :value="game.game.gamename"
        >{{ game.game.gamename }}</option
      >
    </select>
    Price:
    <input type="number" class="form-control" required />
    Discount:
    <input type="number" class="form-control" required />
    <input
      type="submit"
      value="Add"
      class="btn btn-dark m-4"
      @click="AddGameToPlayStore"
    />
  </form>
</template>

<script>
export default {
  name: "AddForm",
  props: ["games", "user"],
  data() {
    return {};
  },
  methods: {
    AddGameToPlayStore() {
      alert("Game has been added");
    },
  },
};
</script>
