<template>
  <div>
    <table class="table">
      <th colspan="6" class="header table-primary">Friend list</th>
      <tr>
        <td>First Name</td>
        <td>Last Name</td>
        <td>Nickname</td>
        <td>User level</td>
        <td>Date joined</td>
        <td>Actions</td>
      </tr>
      <tr v-for="friend in friends" :key="friend.friend.id">
        <td>{{ friend.friend.first_name }}</td>
        <td>{{ friend.friend.last_name }}</td>
        <td>{{ friend.friend.nickname }}</td>
        <td>{{ friend.friend.user_level }}</td>
        <td>{{ friend.friend.date_joined }}</td>
        <td>
          <button
            type="button"
            style="background: red"
            @click="deleteFriend(friend.friend.id)"
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
        Add Friend
      </button>
    </div>
    <Modal v-model="showAddModal" modalClass="modal-wrapper">
      <h3 class="modal-title">Add Friend</h3>
      <div class="modal-content">
        <p class="text">Username</p>
        <select v-model="selectedUser" class="form-control" required>
          <option
            v-for="user in users"
            v-bind:key="user.id"
            v-bind:value="user.username"
            >{{ user.username }}</option
          >
        </select>
      </div>
      <div class="delete-action-buttons">
        <button class="btn btn-primary" @click="addFriend">
          Add
        </button>
        <button class="btn btn-danger" @click="closeAddModal">
          Cancel
        </button>
      </div>
    </Modal>
  </div>
</template>

<script>
import { mapState } from "vuex";

export default {
  name: "FriendList",
  data() {
    return {
      showAddModal: false,
      selectedUser: null,
    };
  },
  mounted() {
    this.$store.dispatch("getAllUsers");
    this.$store.dispatch("getFriends");
  },
  computed: {
    ...mapState(["users", "friends", "user"]),
  },
  methods: {
    addFriend() {
      this.$store.dispatch("addFriend", this.selectedUser);
    },
    deleteFriend(friend_id) {
      this.$store.dispatch("deleteFriend", friend_id);
    },
    openAddModal() {
      this.showAddModal = true;
    },
    closeAddModal() {
      this.showAddModal = false;
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
