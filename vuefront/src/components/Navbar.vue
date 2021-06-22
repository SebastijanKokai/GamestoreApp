<template>
  <div>
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand to="/playstore">Playstore</b-navbar-brand>

      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav
          class="mr-auto"
          v-if="
            user !== null &&
              user.is_active === true &&
              user.is_staff === false &&
              user.is_superuser === false
          "
        >
          <b-nav-item to="/gamelibrary">Game Library</b-nav-item>
          <b-nav-item to="/friendlist">Friend List</b-nav-item>
          <b-nav-item to="/wishlist">Wish List</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav
          class="mr-auto"
          v-if="
            user !== null &&
              user.is_active === true &&
              user.is_staff === true &&
              user.is_superuser === false
          "
        >
          <b-nav-item to="/games">Games</b-nav-item>
          <b-nav-item to="/genres">Genres</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav
          class="mr-auto"
          v-if="
            user !== null &&
              user.is_active === true &&
              user.is_staff === true &&
              user.is_superuser === true
          "
        >
          <b-nav-item to="/">Users</b-nav-item>
          <b-nav-item to="/">Games</b-nav-item>
          <b-nav-item to="/">Genres</b-nav-item>
        </b-navbar-nav>

        <!-- Right aligned nav items -->
        <b-navbar-nav class="ml-auto" v-if="!user">
          <b-nav-item to="/register">Register</b-nav-item>
          <b-nav-item to="/login">Login</b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav class="ml-auto" v-else>
          <b-nav-text class="ml-lg-2 ml-xl-2 mr-lg-2 mr-xl-2"
            >Welcome, {{ user.first_name }}</b-nav-text
          >
          <b-nav-item to="/logout">Logout</b-nav-item>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
import { mapState } from "vuex";
export default {
  name: "App",
  date() {
    return {
      user: this.$store.state.user,
    };
  },
  computed: {
    ...mapState(["user"]),
  },
};
</script>

<style scoped></style>
