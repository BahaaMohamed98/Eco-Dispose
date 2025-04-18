<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import { userStore } from "@/store/userStore.js";

const router = useRouter();

// Form data initialized with current user
const user = ref(userStore.currentUser);
const profileImage = ref(null);
const profileImageFile = ref(null);
const isSubmitting = ref(false);

// Handle image upload
function handleImageUpload(event) {
  const file = event.target.files[0];
  if (file) {
    profileImageFile.value = file;

    const reader = new FileReader();
    reader.onload = (e) => {
      profileImage.value = e.target.result;
    };
    reader.readAsDataURL(file);
  }
}

// Remove profile image
function removeImage() {
  profileImage.value = null;
  profileImageFile.value = null;

  const fileInput = document.getElementById("imageUpload");
  if (fileInput) fileInput.value = "";
}

function updateProfile() {
  isSubmitting.value = true;

  // some artificial delay
  setTimeout(() => {
    // Update user data in store using the new function
    if (userStore.currentUser) {
      // Save profile data
      userStore.updateProfile(user.value, profileImageFile.value);

      // Navigate back to profile page
      gotoProfile();
    }
  }, 800);
}

// Discard changes and go back to profile
function gotoProfile() {
  router.push("/profile");
}
</script>

<template>
  <div id="edit-profile">
    <!-- Header Section -->
    <div class="header-section">
      <div class="container">
        <h1 class="fw-bold text-primary mb-2">Edit Profile</h1>
        <p class="text-muted">Update your personal information</p>
      </div>
    </div>

    <div class="container mt-4">
      <div class="row">
        <!-- Left column - Profile picture -->
        <div class="col-lg-3 col-md-4">
          <div class="profile-card">
            <h5 class="card-title text-center fw-bold mb-4">Profile Picture</h5>

            <div class="profile-image-container mb-3">
              <!-- Update the image source in the template -->
              <img
                :src="profileImage || userStore.getProfileImage()"
                alt="Profile"
                class="profile-image"
              />
            </div>

            <div class="d-flex gap-2 mb-3">
              <label
                for="imageUpload"
                class="btn btn-outline-primary flex-grow-1"
              >
                <i class="fas fa-upload me-2"></i>Upload
              </label>
              <button @click="removeImage" class="btn btn-outline-danger">
                <i class="fas fa-times"></i>
              </button>
            </div>

            <input
              type="file"
              id="imageUpload"
              class="d-none"
              accept="image/*"
              @change="handleImageUpload"
            />
          </div>
        </div>

        <!-- Right column - Form fields -->
        <div class="col-lg-9 col-md-8">
          <div class="edit-form-card">
            <h5 class="card-title mb-4">Personal Information</h5>

            <div class="row mb-3">
              <div class="col-md-6">
                <label class="form-label text-primary">First Name</label>
                <div class="input-group">
                  <span class="input-group-text bg-light">
                    <i class="fas fa-user text-primary"></i>
                  </span>
                  <input
                    v-model="user.firstName"
                    type="text"
                    class="form-control"
                    placeholder="Enter first name"
                  />
                </div>
              </div>

              <div class="col-md-6">
                <label class="form-label text-primary">Last Name</label>
                <div class="input-group">
                  <span class="input-group-text bg-light">
                    <i class="fas fa-user text-primary"></i>
                  </span>
                  <input
                    v-model="user.lastName"
                    type="text"
                    class="form-control"
                    placeholder="Enter last name"
                  />
                </div>
              </div>
            </div>

            <div class="row mb-3">
              <div class="col-md-6">
                <label class="form-label text-primary">Phone Number</label>
                <div class="input-group">
                  <span class="input-group-text bg-light">
                    <i class="fas fa-phone text-primary"></i>
                  </span>
                  <input
                    v-model="user.phoneNumber"
                    type="text"
                    class="form-control"
                    placeholder="Enter phone number"
                  />
                </div>
              </div>
            </div>

            <h5 class="card-title mb-3 mt-4">Address Information</h5>

            <div class="row mb-3">
              <div class="col-md-6">
                <label class="form-label text-primary">Street</label>
                <div class="input-group">
                  <span class="input-group-text bg-light">
                    <i class="fas fa-map-marker-alt text-primary"></i>
                  </span>
                  <input
                    v-model="user.address.street"
                    type="text"
                    class="form-control"
                    placeholder="Enter street address"
                  />
                </div>
              </div>

              <div class="col-md-6">
                <label class="form-label text-primary">City</label>
                <div class="input-group">
                  <span class="input-group-text bg-light">
                    <i class="fas fa-city text-primary"></i>
                  </span>
                  <input
                    v-model="user.address.city"
                    type="text"
                    class="form-control"
                    placeholder="Enter city"
                  />
                </div>
              </div>
            </div>

            <div class="row mb-3">
              <div class="col-md-6">
                <label class="form-label text-primary">Country</label>
                <div class="input-group">
                  <span class="input-group-text bg-light">
                    <i class="fas fa-globe text-primary"></i>
                  </span>
                  <select v-model="user.address.country" class="form-select">
                    <option value="null" disabled>Select country</option>
                    <option value="Egypt">Egypt</option>
                    <option value="USA">United States</option>
                    <option value="UK">United Kingdom</option>
                    <option value="Canada">Canada</option>
                  </select>
                </div>
              </div>

              <div class="col-md-6">
                <label class="form-label text-primary">Postal Code</label>
                <div class="input-group">
                  <span class="input-group-text bg-light">
                    <i class="fas fa-map-pin text-primary"></i>
                  </span>
                  <input
                    v-model="user.address.zipCode"
                    type="text"
                    class="form-control"
                    placeholder="Enter postal code"
                  />
                </div>
              </div>
            </div>

            <div class="d-flex justify-content-end mt-4 gap-3">
              <button @click="gotoProfile" class="btn btn-outline-secondary">
                <i class="fas fa-times me-2"></i>Discard Changes
              </button>
              <button
                @click="updateProfile"
                class="btn btn-primary"
                :disabled="isSubmitting"
              >
                <span
                  v-if="isSubmitting"
                  class="spinner-border spinner-border-sm"
                  aria-hidden="true"
                ></span>
                <i v-else class="fas fa-save me-2"></i>

                <span v-if="isSubmitting"> Saving...</span>
                <span v-else>Save Changes</span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
#edit-profile {
  background-color: #f8f9fa;
  min-height: 100vh;
}

.header-section {
  background-color: #ffffff;
  padding: 2rem 0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  margin-bottom: 1.5rem;
}

.profile-card,
.edit-form-card {
  background-color: #ffffff;
  border-radius: 0.75rem;
  border: none;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
  padding: 1.5rem;
  height: 100%;
}

.profile-card {
  margin-bottom: 1.5rem;
}

.card-title {
  color: #4285f4;
  font-size: 1.25rem;
  font-weight: 600;
}

.profile-image-container {
  width: 150px;
  height: 150px;
  margin: 0 auto;
  position: relative;
}

.profile-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 50%;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
  background-color: #f5f5f5;
}

.form-label {
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.input-group {
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.03);
  border-radius: 0.5rem;
  overflow: hidden;
}

.input-group-text {
  border: none;
}

.form-control,
.form-select {
  border: none;
  padding: 0.625rem 0.75rem;
  font-size: 1rem;
}

.form-control:focus,
.form-select:focus {
  box-shadow: 0 0 0 0.25rem rgba(66, 133, 244, 0.15);
}

.btn-primary {
  background-color: #4285f4;
  border-color: #4285f4;
}

.btn-primary:hover {
  background-color: #3367d6;
  border-color: #3367d6;
}

.btn-outline-primary {
  color: #4285f4;
  border-color: #4285f4;
}

.btn-outline-primary:hover {
  background-color: #4285f4;
  color: white;
}

/* Responsive adjustments */
@media (max-width: 768px) {
  .profile-card {
    margin-bottom: 1.5rem;
  }
}
</style>
