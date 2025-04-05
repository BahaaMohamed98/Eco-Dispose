<script setup>
import { store } from "@/store/store.js";
import { links } from "@/store/links.js";
import router from "@/router/routes.js";

function logout() {
  store.logout();
  router.push({ path: "/login" });
}
</script>

<template>
  <nav class="navbar sticky-top navbar-expand-lg navbar-dark bg-dark px-3 b-3">
    <div class="container-fluid">
      <!-- brand -->
      <router-link class="navbar-brand fs-4 fw-bold text-primary" to="/home"
        >Eco-Dispose
      </router-link>

      <!--            <img src="@/assets/logo.png" class="navbar-brand" width="200" height="200" />-->

      <!-- navbar toggler -->
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="collapse"
        data-bs-target="#navbarNav"
      >
        <span class="navbar-toggler-icon"></span>
      </button>

      <!-- links -->
      <div class="collapse navbar-collapse" id="navbarNav">
        <ul class="navbar-nav text-center">
          <li v-for="(link, index) in links" :key="index" class="nav-item">
            <router-link
              class="nav-link font-size Link"
              :class="{
                active:
                  $route.path === link.to.path && $route.hash === link.to.hash,
              }"
              :to="link.to"
              >{{ link.text }}
            </router-link>
          </li>
        </ul>

        <!-- login and register buttons -->
        <div v-if="!store.currentUser" class="ms-auto">
          <router-link to="/login" class="btn btn-primary me-2">
            <i class="fa-solid fa-right-to-bracket"></i> Login
          </router-link>
          <router-link to="/register" class="btn btn-outline-primary Button">
            <i class="fa-solid fa-user-plus"></i> Register
          </router-link>
        </div>

        <div v-else class="dropdown d-flex ms-auto align-items-center">
          <!-- profile picture -->
          <router-link to="/profile" class="mx-2">
            <img
              :src="store.getProfileImage()"
              alt="Profile"
              class="profile-pic rounded-circle"
          /></router-link>

          <!-- Profile Dropdown -->
          <a
            class="nav-link dropdown-toggle text-white px-3 d-flex align-items-center"
            data-bs-toggle="dropdown"
            href="#"
            role="button"
            aria-expanded="false"
          >
            <!-- Dropdown Icon -->
            <span class="fs-3">&#9776;</span>
          </a>
          <!-- drop down options -->
          <ul class="dropdown-menu dropdown-menu-end">
            <li v-if="!store.currentUser.isAdmin">
              <router-link to="/list" class="dropdown-item"
                ><i class="fa-solid fa-list-ul"></i> Listed Devices
              </router-link>
            </li>
            <li v-if="!store.currentUser.isAdmin">
              <router-link to="/upload" class="dropdown-item"
                ><i class="fa-solid fa-arrow-up-from-bracket"></i> Upload Device
              </router-link>
            </li>
            <li v-if="store.currentUser.isAdmin">
              <router-link to="/admin" class="dropdown-item"
                ><i class="fa-solid fa-user-tie"></i> Admin Dashboard
              </router-link>
            </li>
            <li>
              <router-link to="/profile/edit" class="dropdown-item"
                ><i class="fa-solid fa-user-pen"></i> Edit Profile
              </router-link>
            </li>
            <li>
              <hr class="dropdown-divider" />
            </li>
            <li>
              <button class="dropdown-item text-danger" @click="logout">
                <i class="fa-solid fa-right-from-bracket"></i> Logout
              </button>
            </li>
          </ul>
        </div>
      </div>
    </div>
  </nav>
</template>

<style scoped>
/* remove dropdown arrow */
.dropdown-toggle::after {
  content: none;
}

.nav-link {
  position: relative;
  margin: 0 0.25rem;
  padding: 0.5rem 0.75rem;
  transition: all 0.3s ease;
}

.profile-pic {
  width: 60px;
  height: 60px;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.profile-pic:hover {
  transform: scale(1.1);
}
</style>
