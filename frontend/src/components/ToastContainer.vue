<script setup>
import { toastStore } from "@/store/toastStore.js";
</script>

<template>
  <div class="toast-container position-fixed top-0 end-0 p-3">
    <div
      v-for="toast in toastStore.toasts"
      :key="toast.id"
      class="toast show"
      role="alert"
      aria-live="assertive"
      aria-atomic="true"
    >
      <div class="toast-header text-white" :class="`bg-${toast.type}`">
        <i
          class="fas me-2"
          :class="
            toast.type === 'success'
              ? 'fa-check-circle'
              : 'fa-exclamation-circle'
          "
        ></i>
        <strong class="me-auto">{{ toast.title }}</strong>
        <button
          type="button"
          class="btn-close"
          @click="toastStore.closeToast(toast.id)"
        ></button>
      </div>

      <div class="toast-body">
        {{ toast.message }}
      </div>
    </div>
  </div>
</template>

<style scoped></style>
