import { createRouter, createWebHistory } from "vue-router";
import HomePage from "../views/HomePage.vue";
import LoginPage from "../views/LoginPage.vue";
import SignupPage from "../views/SignupPage.vue";
import TestLearn from "../views/TestLearn.vue";
import { supabase } from "../supabase/init";

let localUser;

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "homepage",
      component: HomePage,
    },
    {
      path: "/login",
      name: "loginpage",
      component: LoginPage,
      meta: { requiresUnAuth: true },
    },
    {
      path: "/signup",
      name: "signuppage",
      component: SignupPage,
      meta: { requiresUnAuth: true },
    },
    {
      path: "/testlearn",
      name: "testlearn",
      component: TestLearn,
      meta: { requiresAuth: true },
    },
  ],
});

async function getUserAuth(next) {
  localUser = await supabase.auth.getSession();
  if (localUser.data.session == null) {
    next("/login");
  } else {
    next();
  }
}

async function getUserUnAuth(next) {
  localUser = await supabase.auth.getSession();
  if (localUser.data.session == null) {
    next();
  } else {
    next("/");
  }
}

router.beforeEach(async (to, from, next) => {
  if (to.meta.requiresAuth) {
    await getUserAuth(next);
  } else if (to.meta.requiresUnAuth) {
    await getUserUnAuth(next);
  } else {
    next();
  }
});

export default router;
