<template>
  <div>
    <table class="table">
      <th colspan="6" class="header table-primary">Games</th>
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
        <td>
          <p v-for="genre in game.genres" :key="genre.genreid">
            {{ genre.genre }}
          </p>
        </td>
        <td>
          <button
            type="button"
            class="btn"
            style="background: aqua"
            @click="openUpdateModal"
          >
            <font-awesome-icon icon="edit" class="edit-icon" />
          </button>
          <button type="button" class="btn" style="background: red" @click="deleteGame(game.gameid)">
            <font-awesome-icon icon="trash" class="trash-icon" />
          </button>
        </td>
      </tr>
    </table>

    <div class="text-center my-3">
      <button
        type="button"
        class="btn btn-primary"
        style="width: 30%"
        @click="openAddModal"
      >
        Add Game
      </button>
    </div>
    <Modal v-model="showAddModal" modalClass="modal-wrapper">
      <h3 class="modal-title">Add Game</h3>
      <div class="modal-content">
        <form>
          <p class="text">Game name</p>
          <input
            type="text"
            v-model="gameToAdd.gamename"
            class="form-control"
            required
          />
          <p class="text">Date released</p>
          <input
            type="text"
            v-model="gameToAdd.datereleased"
            class="form-control"
            required
          />
          <p class="text">Game description</p>
          <input
            type="text"
            v-model="gameToAdd.gamedescription"
            class="form-control"
            required
          />
          <p class="text">Genre</p>
          <select v-model="gameToAdd.genres" class="form-control">
            <option
              v-for="genre in genres"
              v-bind:key="genre.genreid"
              v-bind:value="genre.genre"
              >{{ genre.genre }}</option
            >
          </select>
        </form>
      </div>
      <div class="delete-action-buttons">
        <button class="btn btn-primary" @click="addGame">
          Add
        </button>
        <button class="btn btn-danger" @click="closeAddModal">
          Cancel
        </button>
      </div>
    </Modal>
    <Modal v-model="showUpdateModal" modalClass="modal-wrapper">
      <h3 class="modal-title">Update Game</h3>
      <div class="modal-content">
        <form>
          <p class="text">Game name</p>
          <input
            type="text"
            v-model="gameToUpdate.gamename"
            v
            class="form-control"
            required
          />
          <p class="text">Date released</p>
          <input
            type="date"
            v-model="gameToUpdate.datereleased"
            class="form-control"
            required
          />
          <p class="text">Game description</p>
          <input
            type="text"
            v-model="gameToUpdate.gamedescription"
            class="form-control"
            required
          />
          <p class="text">Genre</p>
          <select v-model="gameToUpdate.genres" class="form-control">
            <option
              v-for="genre in genres"
              v-bind:key="genre.genreid"
              v-bind:value="genre.genre"
              >{{ genre.genre }}</option
            >
          </select>
          <p class="text">Game image</p>
          <input
            type="text"
            v-model="gameToUpdate.gameImgUrl"
            class="form-control"
            required
          />
        </form>
      </div>
      <div class="delete-action-buttons">
        <button class="btn btn-primary" type="submit" @click="updateGame">
          Add
        </button>
        <button class="btn btn-danger" type="button" @click="closeUpdateModal">
          Cancel
        </button>
      </div>
    </Modal>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "Games",
  data() {
    return {
      showAddModal: false,
      showUpdateModal: false,
      gameToAdd: {
        gameid: null,
        gamename: "",
        datereleased: "",
        gamedescription: "",
        genres: [],
        gameImgUrl: "",
      },
      gameToUpdate: {},
    };
  },
  mounted() {
    this.$store.dispatch("getAllGames", "getAllGenres");
  },
  computed: {
    ...mapState(["games", "genres"]),
  },
  methods: {
    openAddModal() {
      this.showAddModal = true;
    },
    closeAddModal() {
      this.showAddModal = false;
    },
    addGame() {
      this.$store.dispatch("addGame", this.gameToAdd).then(() => {
        alert("Game added");
        this.closeAddModal();
      });
    },
    openUpdateModal() {
      this.showUpdateModal = true;
    },
    closeUpdateModal() {
      this.showUpdateModal = false;
    },
    updateGame() {
      console.log(this.gameToUpdate.gamename);
      this.$store.dispatch("modifyGame", this.gameToUpdate).then(() => {
        alert("Game updated");
        this.closeAddModal();
      });
    },
    deleteGame(game_id) {
      this.$store.dispatch("deleteGame",game_id).then(() => {
        alert("Game deleted.")
      });
    }
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
.modal-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.modal-title {
  text-align: center;
  margin-bottom: 5px;
  font-weight: bold;
}
.modal-content {
  border: none !important;
  padding: 10x 0;
}
.delete-action-buttons {
  align-self: center;
  text-align: center;
  padding: 20px 0;
}
</style>
