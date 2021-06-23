<template>
  <div>
    <table class="table">
      <th colspan="6" class="header table-primary">Genres</th>
      <tr>
        <td>Genre</td>
        <td>Actions</td>
      </tr>
      <tr v-for="genre in genres" :key="genre.genreid">
        <td>{{ genre.genre }}</td>
        <td>
          <button type="button" class="btn" style="background: aqua">
            <font-awesome-icon icon="edit" class="edit-icon" />
          </button>
          <button
            type="button"
            class="btn"
            style="background: red"
            @click="deleteGenre(genre.genreid)"
          >
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
        @click="openAddModal()"
      >
        Add Genre
      </button>
    </div>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "Genres",
  data() {
    return {};
  },
  mounted() {
    this.$store.dispatch("getAllGenres");
  },
  computed: {
    ...mapState(["genres"]),
  },
  methods: {
    openAddModal() {
      alert("opened");
    },
    deleteGenre(genre_id) {
      this.$store.dispatch("deleteGenre", genre_id).then(() => {
        alert("Genre deleted.");
      });
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
