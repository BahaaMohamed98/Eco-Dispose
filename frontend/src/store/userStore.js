import { reactive } from "vue";
import { api } from "@/store/api.js";
import { deviceStore } from "@/store/deviceStore.js";

// reactive store
export const userStore = reactive({
  currentUser: null,
  isLoading: true,

  init(user) {
    this.currentUser = user;

    deviceStore.refreshDevices();
  },

  async register(newUser) {
    const formData = new FormData();

    formData.append("firstName", newUser.firstName);
    formData.append("lastName", newUser.lastName);
    formData.append("email", newUser.email);
    formData.append("password", newUser.password);

    try {
      const response = await fetch(`${api}/auth/register`, {
        method: "POST",
        body: formData,
        credentials: "include",
      });

      if (!response.ok) {
        console.error(response);
      }

      return this.login(newUser.email, newUser.password);
    } catch (e) {
      console.error(e);
      return { ok: false };
    }
  },

  async login(email, password) {
    const formData = new FormData();

    formData.append("email", email);
    formData.append("password", password);

    try {
      const response = await fetch(`${api}/auth/login`, {
        method: "POST",
        body: formData,
        credentials: "include",
      });

      if (!response.ok) {
        const errorData = await response.json();
        return { ok: false, message: errorData.message };
      }

      const data = await response.json();

      this.init(data.user);
      return { ok: true };
    } catch (e) {
      console.error(e);
      return { ok: false };
    }
  },

  async updateProfile(user, profileImageFile = null) {
    const formData = new FormData();
    formData.append("user", JSON.stringify(user));

    if (profileImageFile) {
      formData.append("profileImage", profileImageFile);
    }

    try {
      const response = await fetch(`${api}/auth/edit`, {
        method: "POST",
        body: formData,
        credentials: "include",
      });

      if (!response.ok) {
        throw "failed to update profile";
      }

      const data = await response.json();

      this.currentUser = data.user;
    } catch (e) {
      console.error(e);
    }
  },

  // get the profile picture or return the placeholder
  getProfileImage() {
    if (this.currentUser && this.currentUser.profileImageUrl) {
      return api + this.currentUser.profileImageUrl;
    }

    return "/Eco-Dispose/assets/placeholder.png";
  },

  logout() {
    fetch(`${api}/auth/logout`, {
      method: "POST",
      credentials: "include",
    }).catch((e) => console.error(e));

    this.currentUser = null;
  },

  async checkAuth() {
    this.isLoading = true;

    try {
      const response = await fetch(`${api}/auth/profile`, {
        method: "GET",
        credentials: "include",
      });

      if (!response.ok) {
        userStore.currentUser = null;
        throw "not logged in";
      }

      const data = await response.json();

      userStore.init(data.user);
    } catch (e) {
      console.error(e);
    } finally {
      this.isLoading = false;
    }
  },
});
