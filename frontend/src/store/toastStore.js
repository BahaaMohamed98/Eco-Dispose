import { reactive } from "vue";

export const toastStore = {
  toasts: reactive([]),

  // Show a new toast notification
  showToast(title, message, type = "info") {
    const toast = {
      id: Date.now(),
      title,
      message,
      type,
    };

    this.toasts.push(toast);

    // Auto-hide after 5 seconds
    setTimeout(() => this.closeToast(toast.id), 5000);

    return toast.id;
  },

  // Close a specific toast
  closeToast(id) {
    const index = this.toasts.findIndex((toast) => toast.id === id);
    if (index !== -1) {
      this.toasts.splice(index, 1);
    }
  },
};

