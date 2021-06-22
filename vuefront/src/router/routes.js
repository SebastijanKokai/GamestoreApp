import Home from "../components/Home";
import Register from "../components/Register";
import Login from "../components/Login";
import Logout from "../components/Logout";
import Playstore from "../components/Games/Playstore";
import Gamelibrary from "../components/Gamelibrary";
import Wishlist from "../components/Wishlist";
import FriendList from "../components/FriendList";
import Games from "../components/Games";
import { store } from "../vuex-store";

function isStaff() {
  const user = store.state.user;
  return user && user.is_staff === true;
}
function isSuperUser() {
  const user = store.state.user;
  return user && user.is_superuser === true;
}
function isRegular() {
  const user = store.state.user;
  return (
    user &&
    user.is_staff === false &&
    user.is_superuser === false &&
    user.is_active === true
  );
}

const routes = [
  {
    path: "/",
    component: Home,
  },
  {
    path: "/register",
    component: Register,
  },
  {
    path: "/login",
    component: Login,
  },
  {
    path: "/playstore",
    component: Playstore,
  },
  {
    path: "/logout",
    component: Logout,
  },
  {
    path: "/gamelibrary",
    component: Gamelibrary,
    beforeEnter: (to, from, next) => (isRegular() ? next() : next("/login")),
  },
  {
    path: "/wishlist",
    component: Wishlist,
    beforeEnter: (to, from, next) => (isRegular() ? next() : next("/login")),
  },
  {
    path: "/friendlist",
    component: FriendList,
    beforeEnter: (to, from, next) => (isRegular() ? next() : next("/login")),
  },
  {
    path: "/games",
    component: Games,
    beforeEnter: (to, from, next) => (isStaff() ? next() : next("/login")),
  },
];

export default routes;
