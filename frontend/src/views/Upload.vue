<script setup>
import { computed, reactive, ref } from "vue";
import { useRouter } from "vue-router";
import { deviceStore } from "@/store/deviceStore.js";

const router = useRouter();

// Form data with a reactive object
const device = reactive({
  name: "",
  type: "",
  userDescription: "",
  defects: "",
});
const imageFile = ref(null);

// Form validation
const errors = ref({});
const isSubmitting = ref(false);
const imagePreview = ref([]);

// drag and drop
const fileInput = ref(null);
const dragActive = ref(false);

const onFileDrop = (event) => {
  dragActive.value = false;
  const files = event.dataTransfer.files;
  if (files.length) {
    // Process the dropped files
    imagePreview.value = [];
    imageFile.value = null;

    Array.from(files).forEach((file) => {
      if (file.type.startsWith("image/")) {
        imageFile.value = file;

        const reader = new FileReader();
        reader.onload = (e) => {
          imagePreview.value.push(e.target.result);
        };
        reader.readAsDataURL(file);
      }
    });
  }
};

const isFormValid = computed(() => {
  return (
    device.name &&
    device.type &&
    device.userDescription &&
    imagePreview.value.length > 0
  );
});

// Handle file uploads
const handleFileUpload = (event) => {
  const files = event.target.files;
  if (!files.length) return;

  // Clear previous previews
  imagePreview.value = [];
  imageFile.value = null;

  // Process each file
  Array.from(files).forEach((file) => {
    imageFile.value = file;

    const reader = new FileReader();
    reader.onload = (e) => {
      imagePreview.value.push(e.target.result);
    };
    reader.readAsDataURL(file);
  });
};

// Submit device
const submitDevice = async () => {
  if (!isFormValid.value) return;

  isSubmitting.value = true;
  errors.value = {};

  try {
    await deviceStore.addDevice(device.id, device, imageFile.value);

    // Redirect with a success message
    await router.push("/list");
  } catch (error) {
    errors.value.submit = "Failed to submit device. Please try again.";
    console.error(error);
  } finally {
    isSubmitting.value = false;
  }
};

// Remove preview image
const removeImage = (index) => {
  imagePreview.value.splice(index, 1);
  imageFile.value = null;
};
</script>

<template>
  <div class="upload-container">
    <!-- Hero Section -->
    <div class="bg-light py-5 mb-5">
      <div class="container">
        <div class="row justify-content-center">
          <div class="col-lg-8 text-center">
            <h1 class="fw-bold text-primary mb-3">Upload Your Device</h1>
            <p class="lead text-secondary">
              Provide details about your device to get an evaluation and offer
            </p>
          </div>
        </div>
      </div>
    </div>

    <div class="container mb-5">
      <h2 class="fw-bold text-center text-primary mb-4 section-header">
        Device Details
      </h2>
      <div class="row justify-content-center">
        <div class="col-lg-8">
          <form
            @submit.prevent="submitDevice"
            class="device-upload-form shadow-lg rounded-4 p-4 p-md-5 bg-white position-relative overflow-hidden"
          >
            <!-- Decorative elements -->
            <div class="form-decoration-circle circle-1"></div>
            <div class="form-decoration-circle circle-2"></div>

            <!-- Name field -->
            <div class="mb-4 form-floating">
              <input
                v-model="device.name"
                type="text"
                class="form-control"
                id="deviceName"
                placeholder="Device Name"
                required
              />
              <label for="deviceName">
                <i class="fas fa-mobile-alt me-2"></i>Device Name
              </label>
            </div>

            <!-- Type field -->
            <div class="mb-4 form-floating">
              <input
                v-model="device.type"
                type="text"
                class="form-control"
                id="deviceType"
                placeholder="Device Type"
                required
              />
              <label for="deviceType">
                <i class="fas fa-laptop me-2"></i>Device Type
              </label>
            </div>

            <h5 class="mt-4 mb-3">Device Details</h5>

            <div class="row g-3 mb-4">
              <!-- Known Defects -->
              <div class="col-12">
                <div class="form-floating">
                  <input
                    v-model="device.defects"
                    type="text"
                    class="form-control"
                    id="deviceDefects"
                    placeholder="Known Defects"
                  />
                  <label for="deviceDefects">
                    <i class="fas fa-exclamation-triangle me-2"></i>Known
                    Defects
                  </label>
                </div>
              </div>
            </div>

            <!-- Description field -->
            <div class="mb-4 form-floating">
              <textarea
                v-model="device.userDescription"
                class="form-control"
                id="deviceDescription"
                style="height: 120px"
                placeholder="Device Description"
                required
              ></textarea>
              <label for="deviceDescription">
                <i class="fas fa-info-circle me-2"></i>Description
              </label>
            </div>

            <!-- Photos field with preview -->
            <div class="mb-4">
              <label class="form-label fw-bold">
                <i class="fas fa-camera me-2"></i>Photos
              </label>
              <div
                class="upload-area p-3 rounded-3 bg-light text-center position-relative"
                @dragover.prevent
                @dragenter.prevent="dragActive = true"
                @dragleave.prevent="dragActive = false"
                @drop.prevent="onFileDrop"
                :class="{ 'drag-active': dragActive }"
                @click="$refs.fileInput.click()"
              >
                <input
                  type="file"
                  ref="fileInput"
                  class="d-none"
                  id="deviceImage"
                  accept="image/*"
                  multiple
                  @change="handleFileUpload"
                  required
                />
                <div v-if="!imagePreview.length" class="py-4">
                  <i class="fas fa-cloud-upload-alt fs-2 text-primary mb-2"></i>
                  <p class="mb-0">Drag files here or click to browse</p>
                  <p class="small text-muted">
                    Upload high-quality images of your device
                  </p>
                </div>
              </div>

              <!-- Image previews -->
              <div v-if="imagePreview.length" class="image-preview-area mt-3">
                <div class="row g-2">
                  <div
                    v-for="(img, index) in imagePreview"
                    :key="index"
                    class="col-4 col-md-3"
                  >
                    <div class="position-relative preview-img-container">
                      <img :src="img" class="img-fluid rounded" alt="Preview" />
                      <button
                        @click.prevent="removeImage(index)"
                        class="btn btn-sm btn-danger position-absolute top-0 end-0 rounded-circle"
                      >
                        <i class="fas fa-times"></i>
                      </button>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <!-- Submit error message -->
            <div v-if="errors.submit" class="alert alert-danger">
              {{ errors.submit }}
            </div>

            <!-- Buttons -->
            <div class="d-flex flex-column gap-2 mt-4">
              <button
                type="submit"
                class="btn btn-primary btn-lg shadow-sm"
                :disabled="!isFormValid || isSubmitting"
              >
                <span
                  v-if="isSubmitting"
                  class="spinner-border spinner-border-sm me-2"
                  role="status"
                ></span>
                <i v-else class="fas fa-paper-plane me-2"></i>
                Submit for Evaluation
              </button>
              <router-link to="/list" class="btn btn-outline-secondary">
                <i class="fas fa-arrow-left me-2"></i>Back to Listings
              </router-link>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.upload-container {
  overflow-x: hidden;
}

.device-upload-form {
  border: none;
  position: relative;
  z-index: 1;
  transition: all 0.3s ease;
}

.form-decoration-circle {
  position: absolute;
  border-radius: 50%;
  z-index: -1;
  opacity: 0.05;
}

.circle-1 {
  background: linear-gradient(135deg, var(--bs-primary) 0%, #4895ef 100%);
  width: 300px;
  height: 300px;
  top: -100px;
  right: -100px;
}

.circle-2 {
  background: linear-gradient(135deg, #4361ee 0%, var(--bs-primary) 100%);
  width: 200px;
  height: 200px;
  bottom: -50px;
  left: -50px;
}

.preview-img-container {
  aspect-ratio: 1/1;
  overflow: hidden;
  border-radius: 8px;
  border: 2px solid #f8f9fa;
}

.preview-img-container img {
  object-fit: cover;
  width: 100%;
  height: 100%;
}

.preview-img-container .btn {
  width: 24px;
  height: 24px;
  padding: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 4px;
}

.upload-area {
  border: 2px dashed var(--bs-primary);
  transition: all 0.3s ease;
  cursor: pointer;
}

.upload-area:hover {
  border-color: var(--bs-info);
  background-color: #f0f7ff !important;
}

.drag-active {
  border-color: var(--bs-primary);
  background-color: #e6f0ff !important;
  transform: scale(1.01);
}

.btn-primary {
  background: linear-gradient(135deg, #4361ee 0%, #4895ef 100%);
  border: none;
}

.btn-primary:hover {
  background: linear-gradient(135deg, #3b54cc 0%, #3d7fcf 100%);
  transform: translateY(-2px);
}

.form-control:focus {
  border-color: #4895ef;
  box-shadow: 0 0 0 0.25rem rgba(67, 97, 238, 0.15);
}

@media (max-width: 576px) {
  .upload-area {
    padding: 1rem !important;
  }

  .col-4 {
    width: 33.333%;
  }

  .form-decoration-circle {
    opacity: 0.03;
  }
}

.section-header {
  position: relative;
  margin-bottom: 2rem;
  padding-bottom: 1rem;
}

.section-header::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 4px;
  background: var(--bs-primary);
  border-radius: 2px;
}
</style>
