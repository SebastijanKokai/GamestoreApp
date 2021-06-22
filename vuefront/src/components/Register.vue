<template>
  <div class="centered-container">
    <form @submit.prevent="register">
      <h3 class="title">Registration</h3>
      <div class="form-group">
        <label>First Name</label>
        <input
          type="text"
          class="form-control"
          placeholder="Enter first name"
          v-model="form.first_name"
        />
      </div>

      <div class="form-group">
        <label>Last name</label>
        <input
          type="text"
          class="form-control"
          placeholder="Enter last name"
          v-model="form.last_name"
        />
      </div>
      <div class="form-group">
        <label>Nickname</label>
        <input
          type="text"
          class="form-control"
          placeholder="Enter nickname"
          v-model="form.nickname"
        />
      </div>
      <div class="form-group">
        <label>Phone number</label>
        <input
          type="text"
          class="form-control"
          placeholder="Enter phone number"
          v-model="form.phone_number"
        />
      </div>
      <div class="form-group">
        <label>Username</label>
        <input
          type="text"
          class="form-control"
          placeholder="Enter username"
          v-model="form.username"
        />
      </div>
      <div class="form-group">
        <label>Email</label>
        <input
          type="email"
          class="form-control"
          placeholder="Enter email"
          v-model="form.email"
        />
      </div>
      <div class="form-group">
        <label>Password</label>
        <input
          type="password"
          class="form-control"
          placeholder="Enter password"
          v-model="form.password"
        />
      </div>
      <div class="form-group">
        <label>Confirm password</label>
        <input
          type="password"
          class="form-control"
          placeholder="Confirm password"
          v-model="form.password2"
        />
      </div>
      <input type="submit" value="Register" class="btn btn-primary" />
    </form>
  </div>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      loading: false,
      error: null,
      form: {
        first_name: "",
        last_name: "",
        nickname: "",
        username: "",
        email: "",
        phone_number: "",
        password: "",
        password2: "",
      },
    };
  },
  methods: {
    register() {
      const user = {
        first_name: this.form.first_name,
        last_name: this.form.last_name,
        nickname: this.form.nickname,
        phone_number: this.form.phone_number,
        user_level: 0,
        username: this.form.username,
        email: this.form.email,
        password: this.form.password,
        password2: this.form.password2,
      };
      this.loading = true;
      this.$store.dispatch("register", user).catch((error) => {
        console.log(error);
      });
      this.loading = false;
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
