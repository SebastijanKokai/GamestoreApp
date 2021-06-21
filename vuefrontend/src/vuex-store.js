import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import VueJwtDecode from "vue-jwt-decode";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    accessToken: null,
    refreshToken: null,
    user: null,
  },
  mutations: {
    updateStorage(state, { access, refresh }) {
      state.accessToken = access;
      state.refreshToken = refresh;
      state.user = VueJwtDecode.decode(access);
    },
    destroyToken(state) {
      (state.accessToken = null),
        (state.refreshToken = null),
        (state.user = null);
    },
  },
  actions: {
    async logout(context) {
      if (this.state.user !== null) {
        context.commit("destroyToken");
      }
    },
    async login(context, user) {
      return await axios
        .post("http://localhost:8000/auth/login/", user)
        .then((response) => {
          context.commit("updateStorage", {
            access: response.data.access,
            refresh: response.data.refresh,
          });
        });
    },
    async register({ dispatch }, form) {
      const user = {
        first_name: form.first_name,
        last_name: form.last_name,
        nickname: form.nickname,
        phone_number: form.phone_number,
        user_level: 0,
        username: form.username,
        email: form.email,
        password: form.password,
        password2: form.password2,
      };
      console.log(user);
      const response = await axios.post(
        "http://localhost:8000/auth/register/",
        user
      );
      console.log(response);
      dispatch("login");
    },
  },
});
