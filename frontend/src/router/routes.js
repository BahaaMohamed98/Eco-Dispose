import { createRouter, createWebHistory } from "vue-router";

import HomePage from "@/views/HomePage.vue";
import About from "@/views/About.vue";
import Login from "@/views/Login.vue";
import Register from "@/views/Register.vue";
import Profile from "@/views/Profile.vue";
import EditProfile from "@/views/EditProfile.vue";
import Upload from "@/views/Upload.vue";
import AdminDashBoard from "@/views/AdminDashBoard.vue";
import Listings from "@/views/Listings.vue";
import NotFound from "@/views/NotFound.vue";
import { store } from "@/store/store.js";

const routes = [
  { path: "/", redirect: "/home" },
  { path: "/home", component: HomePage },
  { path: "/about", component: About },
  { path: "/login", component: Login, meta: { requiresGuest: true } },
  { path: "/register", component: Register, meta: { requiresGuest: true } },
  { path: "/upload", component: Upload, meta: { requiresUser: true } },
  { path: "/list", component: Listings, meta: { requiresUser: true } },
  { path: "/admin", component: AdminDashBoard, meta: { requiresAdmin: true } },
  { path: "/profile", component: Profile, meta: { requiresAuth: true } },
  {
    path: "/profile/edit",
    component: EditProfile,
    meta: { requiresAuth: true },
  },
  { path: "/:pathMatch(.*)*", name: "NotFound", component: NotFound },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: routes,
  scrollBehavior(to) {
    // if a hash is provided, scroll to the hash
    if (to.hash) {
      return { el: to.hash, behavior: "smooth" };
    }
    // scroll to top
    return { top: 0 };
  },
});

router.beforeEach(async (to, from, next) => {
  if (
    (to.meta.requiresAuth || to.meta.requiresUser || to.meta.requiresAdmin) &&
    !store.currentUser
  ) {
    next({ path: "/login" });
  } else if (to.meta.requiresGuest && store.currentUser) {
    next({ path: "/profile" });
  } else if (to.meta.requiresAdmin && !store.currentUser.isAdmin) {
    next({ path: "/home" });
  } else {
    next();
  }
});

export default router;
