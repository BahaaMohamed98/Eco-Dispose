<!--suppress CssUnusedSymbol -->
<script setup>
import { ref, computed } from "vue";
import { deviceStore } from "@/store/deviceStore.js";

// UI state
const searchQuery = ref("");
const statusFilter = ref("");
const conditionFilter = ref("");
const currentPage = ref(1);
const itemsPerPage = ref(6);
const toasts = ref([]);

// Filter devices based on search and filters
const filteredDevices = computed(() => {
  let result = Array.from(deviceStore.devices.values());

  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase();
    result = result.filter(
      (device) =>
        device.name?.toLowerCase().includes(query) ||
        device.user?.toLowerCase().includes(query) ||
        device.description?.toLowerCase().includes(query),
    );
  }

  if (statusFilter.value) {
    result = result.filter((device) => device.status === statusFilter.value);
  }

  if (conditionFilter.value) {
    result = result.filter(
      (device) => device.condition === conditionFilter.value,
    );
  }

  // Apply pagination
  const startIndex = (currentPage.value - 1) * itemsPerPage.value;
  const endIndex = startIndex + itemsPerPage.value;

  return result.slice(startIndex, endIndex);
});

// Calculate total pages for pagination
const totalPages = computed(() => {
  const filteredCount = Object.values(deviceStore.devices).length;
  return Math.ceil(filteredCount / itemsPerPage.value) || 1;
});

// Send offer to user
function sendOffer(deviceId) {
  const device = deviceStore.devices.get(deviceId);

  if (!device.estimatedPrice || device.estimatedPrice <= 0) {
    showNotification(
      "Validation Error",
      "Please enter a valid price for the offer.",
      "danger",
    );
    return;
  }

  if (!device.adminNotes) {
    showNotification(
      "Validation Error",
      "Please add evaluation notes before sending the offer.",
      "danger",
    );
    return;
  }

  device.status = "evaluated";

  deviceStore
    .updateDevice(deviceId, device)
    .then((response) => {
      if (!response.ok) {
        showNotification("Failed", "Failed to send offer", "danger");
        return;
      }

      showNotification(
        "Offer Sent",
        `An offer of $${device.estimatedPrice} has been sent for ${device.name}.`,
        "success",
      );
    })
    .catch((e) => console.error(e));
}

// Filter methods
function applyFilters() {
  currentPage.value = 1;
}

function resetFilters() {
  searchQuery.value = "";
  statusFilter.value = "";
  conditionFilter.value = "";
  currentPage.value = 1;
}

// Pagination
function changePage(page) {
  if (page >= 1 && page <= totalPages.value) {
    currentPage.value = page;
  }
}

// Refresh devices
function refreshDevices() {
  deviceStore
    .refreshDevices()
    .then((response) => {
      if (response.ok) {
        showNotification(
          "Data Refreshed",
          "Device data has been refreshed.",
          "info",
        );
      }
    })
    .catch((e) => console.error(e));
}

// Helper methods
function getStatusBadgeClass(status) {
  const badgeMap = {
    waiting: "bg-primary",
    collected: "bg-warning",
    evaluated: "bg-info",
    accepted: "bg-success",
    rejected: "bg-danger",
  };
  return badgeMap[status] || "bg-secondary";
}

function getStatusText(status) {
  const textMap = {
    waiting: "Waiting",
    collected: "Collected",
    evaluated: "Offer Sent",
    accepted: "Accepted",
    rejected: "Rejected",
  };
  return textMap[status] || "Unknown";
}

function getConditionClass(condition) {
  if (!condition) {
    return "";
  }
  const conditionMap = {
    excellent: "condition-excellent",
    good: "condition-good",
    fair: "condition-fair",
    poor: "condition-poor",
  };
  return conditionMap[condition] || "";
}

// Show notification toast
function showNotification(title, message, type) {
  const toast = {
    id: Date.now(),
    title,
    message,
    type,
    visible: true,
  };

  toasts.value.push(toast);

  // Auto-hide after 5 seconds
  setTimeout(() => closeToast(toast.id), 5000);
}

// Close toast manually
function closeToast(toastId) {
  const index = toasts.value.findIndex((t) => t.id === toastId);
  if (index !== -1) {
    toasts.value[index].visible = false;
    setTimeout(() => {
      toasts.value = toasts.value.filter((t) => t.id !== toastId);
    }, 500);
  }
}
</script>

<template>
  <div id="admin-dashboard">
    <!-- Admin Header Section -->
    <div class="header-section">
      <div class="container">
        <div class="row align-items-center">
          <div class="col-md-6">
            <h1 class="fw-bold text-primary mb-0">Device Offers</h1>
            <p class="text-muted mb-0">Review devices and send price offers</p>
          </div>
          <div class="col-md-6">
            <div class="d-flex justify-content-md-end mt-3 mt-md-0">
              <button class="btn btn-primary" @click="refreshDevices">
                <i class="fas fa-sync-alt me-2"></i>Refresh Devices
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Filter Section -->
    <div class="container mt-4">
      <div class="filter-bar">
        <div class="row g-3">
          <div class="col-md-4">
            <div class="input-group">
              <span class="input-group-text">
                <i class="fas fa-search"></i>
              </span>
              <input
                type="text"
                class="form-control"
                placeholder="Search devices..."
                v-model="searchQuery"
                @input="applyFilters"
              />
            </div>
          </div>
          <div class="col-md-3">
            <select
              class="form-select"
              v-model="statusFilter"
              @change="applyFilters"
            >
              <option value="">All Statuses</option>
              <option value="waiting">Waiting</option>
              <option value="collected">Collected</option>
              <option value="evaluated">Offer Sent</option>
              <option value="accepted">Accepted</option>
              <option value="rejected">Rejected</option>
            </select>
          </div>
          <div class="col-md-3">
            <select
              class="form-select"
              v-model="conditionFilter"
              @change="applyFilters"
            >
              <option value="">All Conditions</option>
              <option value="excellent">Excellent</option>
              <option value="good">Good</option>
              <option value="fair">Fair</option>
              <option value="poor">Poor</option>
            </select>
          </div>
          <div class="col-md-2">
            <button
              class="btn btn-outline-secondary w-100"
              @click="resetFilters"
            >
              <i class="fas fa-times me-2"></i>Clear
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Devices Grid -->
    <div class="container my-4">
      <div class="row">
        <div
          v-for="device in filteredDevices"
          :key="device.id"
          class="col-md-6 col-lg-4 mb-4"
        >
          <div class="card h-100 device-card">
            <!-- Card Header with Status Badge -->
            <div
              class="card-header bg-white d-flex justify-content-between align-items-center py-3"
            >
              <h5 class="mb-0 fw-bold">{{ device.name }}</h5>
              <span
                class="status-badge"
                :class="getStatusBadgeClass(device.status)"
              >
                {{ getStatusText(device.status) }}
              </span>
            </div>

            <!-- Device Image -->
            <div class="card-img-container">
              <img
                :src="deviceStore.getDeviceImage(device)"
                :alt="device.name"
                class="device-image"
              />
            </div>

            <!-- Card Body with Device Details -->
            <div class="card-body d-flex flex-column">
              <div class="description-notes-container">
                <!-- User Description Section -->
                <div class="my-3">
                  <div
                    class="d-flex justify-content-between align-items-center mb-2"
                  >
                    <label class="form-label fw-bold mb-0">
                      <i class="fas fa-comment-alt me-2 text-primary"></i>User
                      Description
                    </label>
                  </div>
                  <div class="user-description p-3 bg-light border rounded">
                    <p class="mb-0 text-muted">
                      {{ device.userDescription || "No description provided" }}
                    </p>
                  </div>
                </div>

                <div class="mb-3">
                  <div
                    class="d-flex justify-content-between align-items-center mb-2"
                  >
                    <label class="form-label fw-bold mb-0">
                      <i class="fas fa-clipboard-check me-2 text-primary"></i
                      >Admin Notes
                    </label>
                  </div>
                  <textarea
                    class="form-control"
                    v-model="device.adminNotes"
                    rows="3"
                    placeholder="Add your evaluation notes about this device..."
                    :disabled="
                      device.status === 'evaluated' ||
                      device.status === 'accepted'
                    "
                  ></textarea>
                </div>
              </div>

              <!-- Spacer to push the rest to the bottom -->
              <div class="flex-grow-1"></div>

              <!-- Price Offer Section -->
              <div class="mt-3">
                <label class="form-label fw-bold">
                  {{
                    device.status === "evaluated" ||
                    device.status === "accepted"
                      ? "Offered Price"
                      : "Price Offer"
                  }}
                </label>

                <!-- Show input field only when no offer has been sent yet -->
                <div
                  class="input-group mb-3"
                  v-if="
                    device.status !== 'evaluated' &&
                    device.status !== 'accepted'
                  "
                >
                  <span class="input-group-text">$</span>
                  <input
                    type="number"
                    class="form-control"
                    placeholder="Enter price offer"
                    v-model="device.estimatedPrice"
                  />
                </div>

                <!-- Show static price display when offer has been sent -->
                <div v-else class="bg-light p-2 rounded border d-flex">
                  <span class="ps-2">$</span>
                  <span class="ps-2 fw-bold">{{ device.estimatedPrice }}</span>
                </div>
              </div>

              <!-- Device Condition -->
              <div
                class="mt-3"
                v-if="
                  device.status !== 'evaluated' && device.status !== 'accepted'
                "
              >
                <label class="form-label fw-bold">Device Condition</label>
                <select class="form-select" v-model="device.condition">
                  <option value="null">Select condition...</option>
                  <option value="excellent">excellent</option>
                  <option value="good">good</option>
                  <option value="fair">fair</option>
                  <option value="poor">poor</option>
                </select>
              </div>
              <div class="mt-3" v-else>
                <label class="form-label fw-bold">Device Condition</label>
                <div class="bg-light p-2 rounded border">
                  <span
                    class="condition-badge"
                    :class="getConditionClass(device.condition)"
                  >
                    {{ device?.condition }}
                  </span>
                </div>
              </div>

              <!-- Device Actions -->
              <div class="mt-3">
                <button
                  class="btn btn-primary w-100"
                  @click="sendOffer(device.id)"
                  :disabled="
                    device.status === 'evaluated' ||
                    device.status === 'accepted'
                  "
                >
                  <i class="fas fa-paper-plane me-2"></i>
                  {{
                    device.status === "evaluated" ? "Offer Sent" : "Send Offer"
                  }}
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Empty State -->
      <div v-if="filteredDevices.length === 0" class="empty-state">
        <div class="text-center py-5">
          <i class="fas fa-box-open fa-3x text-muted mb-3"></i>
          <h4>No devices found</h4>
          <p class="text-muted">Try adjusting your search or filter criteria</p>
          <button class="btn btn-primary" @click="resetFilters">
            <i class="fas fa-redo me-2"></i>Reset Filters
          </button>
        </div>
      </div>

      <!-- Pagination -->
      <div class="pagination-wrapper mt-4" v-if="totalPages > 1">
        <nav aria-label="Page navigation">
          <ul class="pagination justify-content-center">
            <li class="page-item" :class="{ disabled: currentPage === 1 }">
              <a
                class="page-link"
                href="#"
                @click.prevent="changePage(currentPage - 1)"
              >
                <i class="fas fa-chevron-left"></i>
              </a>
            </li>
            <li
              v-for="page in totalPages"
              :key="page"
              class="page-item"
              :class="{ active: page === currentPage }"
            >
              <a class="page-link" href="#" @click.prevent="changePage(page)">{{
                page
              }}</a>
            </li>
            <li
              class="page-item"
              :class="{ disabled: currentPage === totalPages }"
            >
              <a
                class="page-link"
                href="#"
                @click.prevent="changePage(currentPage + 1)"
              >
                <i class="fas fa-chevron-right"></i>
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </div>

    <!-- Toast Container for Notifications -->
    <div class="toast-container">
      <div
        v-for="toast in toasts"
        :key="toast.id"
        class="toast"
        :class="{ show: toast.visible }"
        role="alert"
        aria-live="assertive"
        aria-atomic="true"
      >
        <div class="toast-header" :class="'bg-' + toast.type + ' text-white'">
          <strong class="me-auto">{{ toast.title }}</strong>
          <button
            type="button"
            class="btn-close btn-close-white"
            @click="closeToast(toast.id)"
          ></button>
        </div>
        <div class="toast-body">
          {{ toast.message }}
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
#admin-dashboard {
  background-color: #f8f9fa;
  min-height: 100vh;
}

.header-section {
  background-color: #ffffff;
  padding: 2rem 0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
  margin-bottom: 1.5rem;
}

.filter-bar {
  background-color: #ffffff;
  border-radius: 0.5rem;
  padding: 1.5rem;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.device-card {
  border: none;
  border-radius: 0.75rem;
  overflow: hidden;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
  transition:
    transform 0.3s ease,
    box-shadow 0.3s ease;
}

.device-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.15);
}

.card-img-container {
  height: 200px;
  display: flex;
  align-items: center;
  justify-content: center;
  background-color: #f8f9fa;
  padding: 1rem;
}

.device-image {
  max-height: 100%;
  max-width: 100%;
  object-fit: contain;
}

.status-badge {
  padding: 0.4rem 0.8rem;
  border-radius: 1rem;
  font-size: 0.8rem;
  font-weight: 600;
  color: #ffffff;
}

.condition-badge {
  display: inline-block;
  padding: 0.4rem 0.8rem;
  border-radius: 1rem;
  font-weight: 600;
}

.toast-container {
  position: fixed;
  top: 20px;
  right: 20px;
  z-index: 1060;
}

.toast {
  min-width: 300px;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.15);
  opacity: 0;
  transform: translateY(-20px);
  transition:
    opacity 0.3s ease,
    transform 0.3s ease;
}

.toast.show {
  opacity: 1;
  transform: translateY(0);
}

.page-link {
  color: #4361ee;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 0.25rem;
  transition: all 0.2s ease;
}

.page-link:hover {
  background-color: #4361ee;
  color: #ffffff;
}

.page-item.active .page-link {
  background-color: #4361ee;
  border-color: #4361ee;
}

.btn-primary {
  background-color: #4361ee;
  border-color: #4361ee;
  color: #ffffff;
}

.btn-primary:hover:not(:disabled) {
  background-color: #3a56d4;
  border-color: #3a56d4;
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(67, 97, 238, 0.3);
}

.btn-primary:disabled {
  background-color: #a8b1ff;
  border-color: #a8b1ff;
  cursor: not-allowed;
}

.empty-state {
  background-color: #ffffff;
  border-radius: 0.75rem;
  padding: 3rem 1rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
}

@media (max-width: 768px) {
  .card-img-container {
    height: 150px;
  }

  .filter-bar {
    padding: 1rem;
  }
}

.device-card {
  height: 100%; /* Make all cards same height */
  display: flex;
  flex-direction: column;
}

.user-description {
  background-color: #f8f9fa;
  border: 1px solid #e9ecef;
  border-radius: 0.5rem;
  font-style: italic;
}

.condition-excellent {
  background-color: #28a745;
  color: white;
}

.condition-good {
  background-color: #17a2b8;
  color: white;
}

.condition-fair {
  background-color: #ffc107;
  color: #343a40;
}

.condition-poor {
  background-color: #dc3545;
  color: white;
}
</style>
