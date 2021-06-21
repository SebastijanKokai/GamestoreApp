import Home from "../components/Home";
import Register from "../components/Register";
import Login from "../components/Login";
import Logout from "../components/Logout";
import GameCard from "../components/Games/GameCard";
import Playstore from "../components/Games/Playstore";
import AddForm from "../components/Games/AddForm";

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
    path: "/gamecard",
    component: GameCard,
  },
  {
    path: "/playstore",
    component: Playstore,
  },
  {
    path: "/logout",
    component: Logout,
  },
];

export default routes;
