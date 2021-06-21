<template>
  <div class="centered-container">
    <md-content class="md-elevation-3 max-height-90">
      <div class="title">
        <h3>Login</h3>
      </div>

      <div class="form">
        <md-field>
          <label>Username</label>
          <md-input v-model="form.username" type="text"></md-input>
        </md-field>
        <md-field md-has-password>
          <label>Password</label>
          <md-input
            v-model="form.password"
            type="password"
            minlength="6"
          ></md-input>
        </md-field>
      </div>

      <div class="actions md-layout md-alignment-center">
        <md-button class="md-raised md-primary" @click="login">Login</md-button>
      </div>

      <div class="loading-overlay" v-if="loading">
        <md-progress-spinner
          md-mode="indeterminate"
          :md-stroke="2"
        ></md-progress-spinner>
      </div>
    </md-content>
  </div>
</template>

<script>
import router from "../router/router";

export default {
  name: "App",
  data() {
    return {
      loading: false,
      error: null,
      form: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    login() {
      const user = {
        username: this.form.username,
        password: this.form.password,
      };
      this.$store.dispatch("login", user).then(() => {
        router.push("/playstore");
      });
    },
  },
};
</script>

<style scoped>
.centered-container {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  background-color: white;
  min-height: 90vh;
}
.title {
  text-align: center;
  margin-bottom: 30px;
}
img {
  margin-bottom: 16px;
  max-width: 80px;
}
.md-button {
  margin: 0;
}
.form {
  margin-bottom: 20px;
}
.md-content {
  z-index: 1;
  padding: 40px;
  width: 100%;
  max-width: 400px;
  position: relative;
}
.loading-overlay {
  z-index: 10;
  top: 0;
  left: 0;
  right: 0;
  position: absolute;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
}
.max-height-90 {
  margin-top: 5px;
  margin-bottom: 5px;
}
</style>
