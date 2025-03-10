<script setup>
import { computed, ref } from "vue";
import { store } from "@/store/store.js";
import router from "@/router/routes.js";

const email = ref("");
const password = ref("");
const invalidCredentials = ref(false);

function submitForm() {
  const response = store.login(email.value, password.value);
  if (response.ok) {
    if (store.currentUser.isAdmin) {
      router.push({ path: "/admin" });
    } else {
      router.push({ path: "/profile" });
    }
  } else {
    invalidCredentials.value = true;
  }
}

const isFormInvalid = computed(() => !email.value || !password.value);
</script>

<template>
  <div class="row">
    <div class="col-lg">
      <img
        src="@/assets/computerchip1.jpeg"
        alt="responsive image"
        style="height: auto; width: 100%; border-radius: 10px; margin: 10px"
      />
    </div>

    <div class="col">
      <form class="p-3">
        <h1 style="color: var(--bs-primary)" class="fw-bold text-center mb-4">
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
          />
          <div class="form-text ps-3 mb-3"
            >we'll never share your email with anyone.
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
          <p
            >Don't have an account?
            <router-link to="/register" style="text-decoration: none"
              >sign up
            </router-link>
          </p>
          <p
            >By creating an account, you agree to the Terms of use and Privacy
            Policy.</p
          >
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
