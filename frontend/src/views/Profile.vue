<script setup>
import { computed } from "vue";
import { userStore } from "@/store/userStore.js";

const address = computed(() => {
  const userAddress = userStore.currentUser?.address;
  let address = "";

  if (userAddress?.street) {
    address += userAddress.street;
  }

  if (userAddress?.city) {
    address += ", " + userAddress.city;
  }

  if (userAddress?.country) {
    address += ", " + userAddress.country;
  }

  if (userAddress?.zipCode) {
    address += ", " + userAddress.zipCode;
  }

  return address;
});
</script>

<template>
  <div class="container mt-5">
    <div class="top-section">
      <!-- Left column - Profile info -->
      <div class="left">
        <div class="profile-info">
          <div class="more-options">
            <div class="dots">
              <div class="dot"></div>
              <div class="dot"></div>
              <div class="dot"></div>
            </div>
          </div>

          <!-- profile photo-->
          <div class="profile-image-container">
            <img
              :src="userStore.getProfileImage()"
              alt="Profile Image"
              style="
                width: 100%;
                height: 100%;
                object-fit: cover;
                border-radius: 50%;
              "
            />
          </div>

          <h2 class="username">
            {{
              `${userStore.currentUser.firstName} ${userStore.currentUser.lastName}`
            }}
          </h2>
          <div class="admin-badge">
            <div v-if="userStore.currentUser.isAdmin">
              <span class="crown-icon">👑</span>
              <span>Admin</span>
            </div>
          </div>
          <button class="edit-details-btn">Edit Details</button>
        </div>
        <div class="navigation">
          <div class="nav-item active">Profile</div>
        </div>
      </div>

      <!-- Middle column - Main content -->
      <div class="main-content">
        <div class="profile-header">
          <h1 class="profile-title">Profile</h1>
          <router-link to="/profile/edit" class="edit-profile-btn">
            <span class="pencil-icon">🖊️</span>
            Edit Profile
          </router-link>
        </div>
        <div class="overview-section">
          <div class="overview-header">
            <h2 class="overview-title">Overview</h2>
            <div class="info-icon">i</div>
          </div>
          <div class="profile-fields">
            <div class="field-group">
              <div class="field-label">First Name</div>
              <div class="field-value">
                {{ userStore.currentUser.firstName }}
              </div>
            </div>
            <div class="field-group">
              <div class="field-label">Last Name</div>
              <div class="field-value">
                {{ userStore.currentUser.lastName }}
              </div>
            </div>
            <div class="field-group">
              <div class="field-label">Role</div>
              <div class="field-value">
                {{ userStore.currentUser.isAdmin ? "Administrator" : "User" }}
              </div>
            </div>
            <div class="field-group">
              <div class="field-label">Phone Number</div>
              <div class="field-value">
                {{ userStore.currentUser?.phoneNumber }}
              </div>
            </div>
            <div class="field-group">
              <div class="field-label">Address</div>
              <div class="field-value">{{ address }}</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
* {
  box-sizing: border-box;
  font-family: Arial, sans-serif;
}

body {
  background-color: #f8f9fa;
  padding: 0;
}

/* Three-column layout styles */
.container {
  display: flex;
  flex-direction: column;
  max-width: 1200px;
  margin: 0 auto;
  gap: 20px;
}

.top-section {
  display: flex;
  gap: 20px;
  margin: 0;
}

/* Left column - Profile info */
.left {
  margin: 0;
  width: 25%;
}

.profile-info {
  flex: 0 0 300px;
  background-color: #fff;
  border-radius: 8px;
  border: 1px solid #e0e0e0;
  padding: 30px;
  display: flex;
  flex-direction: column;
  align-items: center;
  position: relative;
  height: fit-content;
  margin-bottom: 20px;
  width: 100%;
}

.more-options {
  position: absolute;
  top: 15px;
  right: 15px;
  cursor: pointer;
}

.more-options .dots {
  display: flex;
  flex-direction: column;
  align-items: center;
  height: 24px;
}

.more-options .dot {
  width: 4px;
  height: 4px;
  background-color: #333;
  border-radius: 50%;
  margin: 2px 0;
}

.profile-image-container {
  width: 100px;
  height: 100px;
  margin-bottom: 20px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.username {
  font-size: 22px;
  font-weight: bold;
  color: #333;
  margin-bottom: 5px;
}

.admin-badge {
  display: flex;
  align-items: center;
  gap: 5px;
  color: #888;
  margin-bottom: 20px;
}

.crown-icon {
  color: #ffc107;
  font-size: 16px;
}

.edit-details-btn {
  width: 100%;
  padding: 12px 0;
  background-color: white;
  color: #4285f4;
  border: 1px solid #e0e0e0;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.edit-details-btn:hover {
  background-color: #f5f5f5;
}

/* Middle column - Main content */
.main-content {
  flex: 1;
  background-color: #fff;
  border-radius: 8px;
  border: 1px solid #e0e0e0;
  width: 40%;
}

.profile-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px 30px;
  border-bottom: 1px solid #e0e0e0;
}

.profile-title {
  font-size: 24px;
  color: #4285f4;
  font-weight: normal;
}

.edit-profile-btn {
  display: flex;
  align-items: center;
  gap: 8px;
  background-color: white;
  color: #4285f4;
  border: 1px solid #4285f4;
  border-radius: 4px;
  padding: 8px 16px;
  font-size: 14px;
  cursor: pointer;
  text-decoration: none;
}

.edit-profile-btn:hover {
  background-color: #f5f5f5;
}

.pencil-icon {
  color: #4285f4;
}

.overview-section {
  padding: 20px 30px;
}

.overview-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.overview-title {
  font-size: 20px;
  color: #4285f4;
  font-weight: normal;
}

.info-icon {
  width: 24px;
  height: 24px;
  border-radius: 50%;
  background-color: #f1f8ff;
  color: #4285f4;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 14px;
  cursor: pointer;
}

.profile-fields {
  display: grid;
  grid-template-columns: 1fr;
  gap: 24px;
}

.field-group {
  display: grid;
  grid-template-columns: 1fr;
  gap: 8px;
}

.field-label {
  font-size: 16px;
  color: #4285f4;
}

.field-value {
  font-size: 18px;
  color: #333;
}

/* Right column - Navigation */
.navigation {
  flex: 0 0 200px;
  background-color: #f1f8ff;
  border: 1px solid #e0e0e0;
  border-radius: 8px;
  overflow: hidden;
  height: fit-content;
}

.nav-item {
  padding: 15px 20px;
  color: #4285f4;
  font-size: 18px;
  cursor: pointer;
}

.nav-item.active {
  background-color: #f1f8ff;
  font-weight: bold;
}

/* Responsive adjustments */
@media (max-width: 992px) {
  .top-section {
    flex-direction: column;
  }

  .profile-info,
  .navigation {
    width: 100%;
    flex: none;
  }
}
</style>
