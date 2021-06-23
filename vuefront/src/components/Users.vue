<template>
  <div>
    <table class="table">
      <th colspan="6" class="header table-primary">Users</th>
      <tr>
        <td>ID</td>
        <td>Username</td>
        <td>First name</td>
        <td>Last name</td>
        <td>Nickname</td>
        <td>User level</td>
        <td>Date joined</td>
        <td>Actions</td>
      </tr>
      <tr v-for="user in users" :key="user.id">
        <td>{{ user.id }}</td>
        <td>{{ user.username }}</td>
        <td>{{ user.first_name }}</td>
        <td>{{ user.last_name }}</td>
        <td>{{ user.nickname }}</td>
        <td>{{ user.user_level }}</td>
        <td>{{ user.date_joined }}</td>
        <td>
          <button type="button" class="btn" style="background: aqua">
            <font-awesome-icon icon="edit" class="edit-icon" />
          </button>
          <button type="button" class="btn" style="background: red">
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
  name: "Users",
  data() {
    return {};
  },
  mounted() {
    this.$store.dispatch("getAllUsers");
  },
  computed: {
    ...mapState(["users"]),
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
