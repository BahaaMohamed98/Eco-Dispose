<script setup>
import NavBar from "@/components/NavBar.vue";
import Footer from "@/components/Footer.vue";
import router from "@/router/routes.js";
import { computed } from "vue";

const footerExcludePaths = ["/login", "/register"];

const renderFooter = computed(
  () => !footerExcludePaths.includes(router.currentRoute.value.path),
);
</script>

<template>
  <NavBar></NavBar>

  <router-view></router-view>

  <Footer v-if="renderFooter"></Footer>
</template>

<style scoped></style>
