import { reactive } from "vue";

const currentUserKey = "currentUser";

function saveUser() {
  localStorage.setItem(currentUserKey, JSON.stringify(store.currentUser));
}

// reactive store
export const store = reactive({
  users: [],
  currentUser: null,

  register(newUser) {
    this.users.push(newUser);
    return this.login(newUser.email, newUser.password);
  },

  login(email, password) {
    const user = this.users.find(
      (user) => user.email === email && user.password === password,
    );

    if (user) {
      this.currentUser = user;
      saveUser();
      return { ok: true, message: "Login Successful" };
    }

    return { ok: false, message: "Invalid credentials" };
  },

  logout() {
    this.currentUser = null;
    localStorage.removeItem(currentUserKey);
  },

  // New function to save profile image
  saveProfileImage(imageData) {
    if (this.currentUser) {
      this.currentUser.profileImage = imageData;
      saveUser();
    }
  },

  // New function to get profile image or placeholder
  getProfileImage() {
    return this.currentUser?.profileImage || "/src/assets/placeholder.png";
  },

  // New function to update user profile
  updateProfile(profileData) {
    if (this.currentUser) {
      Object.assign(this.currentUser, profileData);
      saveUser();
      return true;
    }
    return false;
  },
});

export const devicesStore = reactive({
  devices: {},

  getDevices() {
    return this.devices;
  },

  getDeviceImage(device) {
    return device.image || "/src/assets/devices/device.png";
  },

  updateDeviceStatus(deviceId, status) {
    if (this.devices[deviceId]) {
      this.devices[deviceId].status = status;
    }
  },
});

// init store data
(() => {
  // fetch predefined users
  fetch("/data/users.json")
    .then((data) => data.json())
    .then((users) => (store.users = users))
    .catch((e) => console.error(e));

  const currentUser = localStorage.getItem(currentUserKey);
  if (currentUser) {
    store.currentUser = JSON.parse(currentUser);
  }
})();

// init devices store data
(() => {
  fetch("/data/devices.json")
    .then((data) => data.json())
    .then((devices) => {
      // Replace the hardcoded devices with fetched data
      if (devices && Object.keys(devices).length > 0) {
        devicesStore.devices = devices;
      }
    })
    .catch((e) => console.error("Error loading devices:", e));
})();
