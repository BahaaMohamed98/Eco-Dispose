<script setup>
import { links } from "@/store/links.js";
</script>

<template>
    <div class="container mt-auto">
        <footer class="py-3 my-4">
            <ul class="nav justify-content-center border-bottom pb-3 mb-3">
                <li
                    v-for="(link, index) in links"
                    :key="index"
                    class="nav-item"
                >
                    <router-link
                        :to="link.to"
                        class="nav-link px-2 text-muted Link"
                        >{{ link.text }}
                    </router-link>
                </li>
            </ul>
            <p class="text-center text-muted">&copy; 2025 Eco-Dispose </p>
        </footer>
    </div>
</template>

<style scoped></style>
