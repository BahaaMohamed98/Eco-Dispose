<script setup>
import { computed, ref } from "vue";
import { userStore } from "@/store/userStore.js";
import router from "@/router/routes.js";

const email = ref("");
const password = ref("");
const invalidCredentials = ref(false);

function submitForm() {
  userStore
    .login(email.value, password.value)
    .then((response) => {
      if (!response.ok) {
        invalidCredentials.value = true;
        return;
      }

      if (userStore.currentUser.isAdmin) {
        router.push({ path: "/admin" });
      } else {
        router.push({ path: "/list" });
      }
    })
    .catch((e) => console.error(e));
}

const isFormInvalid = computed(() => !email.value || !password.value);
</script>

<template>
  <div class="row flex-grow-1 m-0">
    <div
      class="col-lg"
      style="
        background: url(assets/computerchip1.jpeg) no-repeat center center;
        background-size: cover;
      "
    ></div>

    <div class="col-sm">
      <form class="p-3">
        <h1
          class="fw-bold text-center text-primary"
          style="margin-bottom: 80px"
        >
          Sign In
        </h1>
        <div class="mb-3">
          <label for="exampleInputEmail1" class="form-label fw-bold"
            >Email address</label
          >
          <input
            v-model="email"
            type="email"
            class="form-control rounded-pill"
            placeholder="Email address"
            aria-describedby="emailHelp"
            autofocus
            autocomplete="username"
          />
          <div class="form-text ps-3 mb-3">
            we'll never share your email with anyone.
          </div>
        </div>
        <div class="mb-3">
          <label for="exampleInputPassword1" class="form-label fw-bold"
            >Password
          </label>
          <input
            v-model="password"
            type="password"
            class="form-control rounded-pill"
            placeholder="Password"
            autocomplete="current-password"
          />
        </div>
        <button
          @click.prevent="submitForm"
          :disabled="isFormInvalid"
          type="submit"
          class="btn btn-primary form-control rounded-pill mt-4"
        >
          <i class="fa-solid fa-right-to-bracket"></i> Sign in
        </button>
      </form>
      <div
        v-if="invalidCredentials"
        class="alert alert-danger mx-3"
        role="alert"
      >
        Invalid Credentials
      </div>
      <div class="container d-flex justify-content-center align-items-center">
        <div class="text-center" style="padding-top: 1rem">
          <div class="or-divider">
            <hr class="left-line" />
            <span class="or-text">OR</span>
            <hr class="right-line" />
          </div>
          <p>
            Don't have an account?
            <router-link to="/register" style="text-decoration: none"
              >sign up
            </router-link>
          </p>
          <p>
            By creating an account, you agree to the Terms of use and Privacy
            Policy.
          </p>
          <hr />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.or-divider {
  display: flex;
  align-items: center;
  text-align: center;
}

.or-divider hr {
  flex-grow: 1;
  border: 0;
  border-top: 1px solid #ccc;
}

.or-text {
  padding: 0 10px;
}
</style>
