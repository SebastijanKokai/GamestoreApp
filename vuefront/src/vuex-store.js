import Vue from "vue";
import Vuex from "vuex";
import { createAxiosInstance, AxiosWithoutToken } from "./axios-api";
import VueJwtDecode from "vue-jwt-decode";
import router from "./router/router";

Vue.use(Vuex);

export const store = new Vuex.Store({
  state: {
    accessToken: null,
    refreshToken: null,
    user: null,
    users: [],
    games: [],
    genres: [],
    gamesPlaystore: [],
    libraryGames: [],
    wishListGames: [],
    friends: [],
  },
  getters: {
    token: (state) => {
      return state.accessToken;
    },
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
    updateGamesPlaystore(state, games) {
      state.gamesPlaystore = games;
    },
    setLibraryGames(state, games) {
      state.libraryGames = games;
    },
    setWishlistGames(state, games) {
      state.wishListGames = games;
    },
    setFriends(state, friends) {
      state.friends = friends;
    },
    setUsers(state, users) {
      state.users = users;
    },
    setGames(state, games) {
      state.games = games;
    },
    setGenres(state, genres) {
      state.genres = genres;
    },
  },
  actions: {
    async logout(context) {
      if (this.state.user !== null) {
        context.commit("destroyToken");
      }
    },
    async login(context, user) {
      return await AxiosWithoutToken.post("auth/login/", user)
        .then((response) => {
          context.commit("updateStorage", {
            access: response.data.access,
            refresh: response.data.refresh,
          });
        })
        .then(() => {
          router.push("/");
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
      await AxiosWithoutToken.post("auth/register/", user).then((response) => {
        dispatch("login", user);
      });
    },
    async getAllUsers(context) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      await getAPI.get("auth/getUsers/").then((users) => {
        context.commit("setUsers", users.data);
      });
    },
    async getAllGamesFromPlaystore(context) {
      await AxiosWithoutToken.get("gamestore/getPlaystoreGames/").then(
        (games) => {
          context.commit("updateGamesPlaystore", games.data);
        }
      );
    },
    async buyGame(context, game_id) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      const bodyParameters = {
        gameid: game_id,
      };
      console.log("gameid");
      console.log(game_id);
      await getAPI
        .post("auth/createLibraryRow/", bodyParameters)
        .then(console.log)
        .catch(console.log);
    },
    async getLibraryGames(context) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      await getAPI.get("auth/getLibraryByUser/").then((games) => {
        context.commit("setLibraryGames", games.data);
      });
    },
    async deleteLibraryGame(context, game_id) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      await getAPI.delete("auth/deleteLibraryRow/" + game_id + "/").then(() => {
        this.dispatch("getLibraryGames");
      });
    },
    async addToWishlist(context, game_id) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      const bodyParameters = {
        gameid: game_id,
      };

      await getAPI
        .post("auth/createWishlistRow/", bodyParameters)
        .then(console.log)
        .catch(console.log);
    },
    async getWishlistGames(context) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      await getAPI.get("auth/getWishlistByUser/").then((games) => {
        context.commit("setWishlistGames", games.data);
      });
    },
    async deleteWishlistGame(context, game_id) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      await getAPI
        .delete("auth/deleteWishlistRow/" + game_id + "/")
        .then(() => {
          this.dispatch("getWishlistGames");
        });
    },
    async getFriends(context) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      await getAPI.get("auth/getFriendlistByUser/").then((friends) => {
        context.commit("setFriends", friends.data);
      });
    },
    async addFriend(context, friend_username) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      let friendToAdd = null;
      this.state.users.forEach((user) => {
        if (user.username === friend_username) {
          friendToAdd = user;
        }
      });
      const bodyParameters = {
        friendid: friendToAdd.id,
      };
      await getAPI
        .post("auth/createFriendlistRow/", bodyParameters)
        .then(() => {
          this.dispatch("getFriends");
        });
    },
    async deleteFriend(context, friend_id) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      await getAPI
        .delete("auth/deleteFriendlistRow/" + friend_id + "/")
        .then(() => {
          this.dispatch("getFriends");
        });
    },
    async addGameToPlaystore(context, gameToAdd, game_id) {
      let gameprice = gameToAdd.price * (1 - gameToAdd.discount);
      console.log(game_id);
      console.log(gameprice);
      console.log(gameToAdd.discount);
      const bodyParameters = {
        game: game_id,
        gameprice: gameprice,
        discount: gameToAdd.discount,
        dateadded: "2020-12-12",
      };
      const getAPI = createAxiosInstance(this.state.accessToken);
      await getAPI
        .post("gamestore/addGameToPlaystore/", bodyParameters)
        .then(() => {
          this.dispatch("getAllGamesFromPlaystore");
        });
    },
    async deleteGameFromPlaystore(context, playstorerow) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      await getAPI
        .delete("gamestore/deleteGameFromPlaystore/" + playstorerow + "/")
        .then(() => {
          this.dispatch("getAllGamesFromPlaystore");
        });
    },
    async getAllGames(context) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      return await getAPI.get("gamestore/getGames/").then((games) => {
        context.commit("setGames", games.data);
      });
    },
    async addGame(context, gameToAdd) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      const bodyParameters = {
        gamename: gameToAdd.gamename,
        datereleased: gameToAdd.datereleased,
        gamedescription: gameToAdd.gamedescription,
      };
      return await getAPI
        .post("gamestore/createGame/", bodyParameters)
        .then(() => {
          this.dispatch("getAllGames");
        });
    },
    async modifyGame(context, gameToUpdate) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      const bodyParameters = {
        gamename: gameToUpdate.gamename,
        datereleased: gameToUpdate.datereleased,
        gamedescription: gameToUpdate.gamedescription,
        gameImgUrl:
          "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRgqpAoCAiLrhEcMEFLv4_Zk8bLixW1ZrWfrQ&usqp=CAU",
      };
      let gameid = null;
      this.state.games.forEach((game) => {
        if (game.gamename === gameToUpdate.gamename) {
          gameid = game.gameid;
        }
      });
      return await getAPI
        .put("gamestore/modifyGame/" + gameid + "/", bodyParameters)
        .then(() => {
          this.dispatch("getAllGames");
        });
    },
    async deleteGame(context, game_id) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      return await getAPI
        .delete("gamestore/deleteGame/" + game_id + "/")
        .then(() => {
          this.dispatch("getAllGames");
        });
    },
    async getAllGenres(context) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      return await getAPI.get("gamestore/getGenres/").then((genres) => {
        context.commit("setGenres", genres.data);
      });
    },
    async addGenre(context) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      return await getAPI.get("gamestore/getGames/").then((games) => {
        context.commit("setGames", games.data);
      });
    },
    async modifyGenre(context) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      return await getAPI.get("gamestore/getGames/").then((games) => {
        context.commit("setGames", games.data);
      });
    },
    async deleteGenre(context, genre_id) {
      const getAPI = createAxiosInstance(this.state.accessToken);
      return await getAPI
        .delete("gamestore/deleteGenre/" + genre_id + "/")
        .then(() => {
          this.dispatch("getAllGenres");
        });
    },
  },
});
