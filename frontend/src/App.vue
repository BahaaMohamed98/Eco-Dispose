<script setup>
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
import ToastContainer from "@/components/ToastContainer.vue";
import router from "@/router/routes.js";
import { computed } from "vue";

const footerExcludePaths = ["/login", "/register"];

const renderFooter = computed(
  () => !footerExcludePaths.includes(router.currentRoute.value.path),
);
</script>

<template>
  <ToastContainer></ToastContainer>

  <NavBar></NavBar>

  <RouterView></RouterView>

  <Footer v-if="renderFooter"></Footer>
</template>

<style scoped></style>
