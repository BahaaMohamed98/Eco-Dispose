<script setup>
import { store } from "@/store/store.js";
import router from "@/router/routes.js";
import { computed, ref } from "vue";

const firstName = ref("");
const lastName = ref("");
const email = ref("");
const password = ref("");

function submitForm() {
  const response = store.register({
    firstName: firstName.value,
    lastName: lastName.value,
    email: email.value,
    password: password.value,
    phoneNumber: "",
    address: {
      street: "",
      city: "",
      country: "",
      zip: "",
    },
  });

  if (response.ok) {
    router.push({ path: "/profile/edit" });
  }
}

const isFormInvalid = computed(
  () => !firstName.value || !lastName.value || !email.value || !password.value,
);
</script>

<template>
  <div class="row flex-grow-1 m-0">
    <div class="col">
      <div class="container p-4">
        <form>
          <h1
            class="fw-bold text-center text-primary"
            style="margin-bottom: 80px"
          >
            Welcome to Eco-Dispose
          </h1>
          <div class="mb-3 row">
            <div class="col-md-6">
              <label for="firstName" class="form-label fw-bold"
                >First Name</label
              >
              <input
                v-model="firstName"
                type="text"
                class="form-control rounded-pill"
                id="firstName"
                placeholder="First Name"
                autofocus
              />
            </div>
            <div class="col-md-6">
              <label for="lastName" class="form-label fw-bold">Last Name</label>
              <input
                v-model="lastName"
                type="text"
                class="form-control rounded-pill"
                id="lastName"
                placeholder="Last Name"
              />
            </div>
          </div>
          <div class="mb-3">
            <label for="email" class="form-label fw-bold">Email</label>
            <input
              v-model="email"
              type="email"
              class="form-control rounded-pill"
              id="email"
              placeholder="Email address"
            />
          </div>
          <div class="mb-3">
            <label for="password" class="form-label fw-bold">Password</label>
            <div class="input-group">
              <input
                v-model="password"
                type="password"
                class="form-control rounded-pill"
                id="password"
                placeholder="Password"
                autocomplete="password"
              />
            </div>
          </div>
          <ul style="list-style-type: disc; margin-bottom: 10px">
            <li>Use 8 or more characters</li>
            <li>One Uppercase character</li>
            <li>One lowercase character</li>
            <li>One special character</li>
            <li>One number</li>
          </ul>
          <div class="form-check my-3">
            <input class="form-check-input" type="checkbox" id="emails" />
            <label class="form-check-label" for="emails">
              I want to receive emails about the product, events, and marketing
              promotions.
            </label>
            <p class="mt-3">
              By creating an account, you agree to the Terms of use and Privacy
              Policy.
            </p>
          </div>
          <div class="container text-center">
            <button
              @click.prevent="submitForm"
              type="submit"
              class="btn btn-primary mt-3 rounded-pill"
              :disabled="isFormInvalid"
            >
              <i class="fa-solid fa-user-plus"></i> Create an account
            </button>
            <p class="mt-3">
              Already have an account?
              <router-link to="/login" style="text-decoration: none">
                Sign in
              </router-link>
            </p>
          </div>
        </form>
      </div>
    </div>
    <div
      class="col-lg"
      style="
        background: url(assets/computerchip2.jpeg) no-repeat center center;
        background-size: cover;
      "
    ></div>
  </div>
</template>

<style scoped></style>
