<script setup>
import { ref, computed } from "vue";
import { devicesStore } from "@/store/store.js";

// UI state
const searchQuery = ref("");
const statusFilter = ref("");
const conditionFilter = ref("");
const currentPage = ref(1);
const itemsPerPage = ref(6);
const toasts = ref([]);

// Get devices as array with IDs
const devicesArray = computed(() => {
  return Object.entries(devicesStore.devices).map(([id, device]) => ({
    id,
    ...device,
    // Ensure estimatedPrice and notes fields exist for editing
    estimatedPrice: device.estimatedPrice || "",
    notes: device.notes || "",
    queryId:
      device.queryId ||
      `query-${Date.now()}-${Math.random().toString(36).substring(2, 9)}`,
  }));
});

// Filter devices based on search and filters
const filteredDevices = computed(() => {
  let result = devicesArray.value;

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
  const filteredCount = Object.values(devicesStore.devices).length;
  return Math.ceil(filteredCount / itemsPerPage.value) || 1;
});

// Send offer to user
function sendOffer(deviceId) {
  const device = devicesStore.devices[deviceId];

  if (!device.estimatedPrice || device.estimatedPrice <= 0) {
    showNotification(
      "Validation Error",
      "Please enter a valid price for the offer.",
      "danger",
    );
    return;
  }

  if (!device.notes) {
    showNotification(
      "Validation Error",
      "Please add evaluation notes before sending the offer.",
      "danger",
    );
    return;
  }

  // Update status to evaluated (offer sent)
  devicesStore.updateDeviceStatus(deviceId, "evaluated");

  // Show notification ONLY when offer is sent
  showNotification(
    "Offer Sent",
    `An offer of $${device.estimatedPrice} has been sent for ${device.name}.`,
    "success",
  );
}

// Update device price
function updateDevicePrice(deviceId, price) {
  if (devicesStore.devices[deviceId]) {
    devicesStore.devices[deviceId].estimatedPrice = price;
  }
}

// Update device notes
function updateDeviceNotes(deviceId, notes) {
  if (devicesStore.devices[deviceId]) {
    devicesStore.devices[deviceId].notes = notes;
  }
}

// Update device condition
function updateDeviceCondition(deviceId, condition) {
  if (devicesStore.devices[deviceId]) {
    devicesStore.devices[deviceId].condition = condition;
  }
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
  showNotification("Data Refreshed", "Device data has been refreshed.", "info");
}

// Helper methods
function getUserInitials(name) {
  if (!name) return "U";
  return name
    .split(" ")
    .map((n) => n[0])
    .join("")
    .toUpperCase();
}

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
  const conditionMap = {
    Excellent: "condition-excellent",
    Good: "condition-good",
    Fair: "condition-fair",
    Poor: "condition-poor",
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
  setTimeout(() => {
    const index = toasts.value.findIndex((t) => t.id === toast.id);
    if (index !== -1) {
      toasts.value[index].visible = false;
      setTimeout(() => {
        toasts.value = toasts.value.filter((t) => t.id !== toast.id);
      }, 500);
    }
  }, 5000);
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
              <option value="Excellent">Excellent</option>
              <option value="Good">Good</option>
              <option value="Fair">Fair</option>
              <option value="Poor">Poor</option>
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
                :src="
                  device.image ||
                  'https://via.placeholder.com/300x200?text=No+Image'
                "
                :alt="device.name"
                class="device-image"
              />
            </div>

            <!-- Card Body with Device Details -->
            <div class="card-body">
              <!-- Device Condition Badge -->
              <div class="mb-3">
                <span
                  class="condition-badge"
                  :class="getConditionClass(device.condition)"
                >
                  {{ device.condition }}
                </span>
              </div>

              <!-- Device Specifications -->
              <div class="device-specs mt-3" v-if="device.specs">
                <h5 class="fw-bold mb-3">Specifications</h5>
                <div
                  class="spec-item"
                  v-for="(value, key) in device.specs"
                  :key="key"
                >
                  <span class="spec-label">{{ key }}</span>
                  <span class="spec-value">{{ value }}</span>
                </div>
              </div>

              <!-- Notes Section -->
              <div class="mt-4">
                <label class="form-label fw-bold">Evaluation Notes</label>
                <textarea
                  class="form-control"
                  v-model="device.notes"
                  rows="3"
                  placeholder="Add notes about the device evaluation..."
                  :disabled="
                    device.status === 'evaluated' ||
                    device.status === 'accepted'
                  "
                  @change="updateDeviceNotes(device.id, device.notes)"
                ></textarea>
              </div>

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
                    @change="
                      updateDevicePrice(device.id, device.estimatedPrice)
                    "
                  />
                </div>

                <!-- Show static price display when offer has been sent -->
                <div v-else class="bg-light p-2 rounded border d-flex">
                  <span class="ps-2">$</span>
                  <span class="ps-2 fw-bold">{{ device.estimatedPrice }}</span>
                </div>
              </div>

              <!-- Device Condition (Admin sets this) -->
              <div
                class="mt-3"
                v-if="
                  device.status !== 'evaluated' && device.status !== 'accepted'
                "
              >
                <label class="form-label fw-bold">Device Condition</label>
                <select
                  class="form-select"
                  v-model="device.condition"
                  @change="updateDeviceCondition(device.id, device.condition)"
                >
                  <option value="">Select condition...</option>
                  <option value="Excellent">Excellent</option>
                  <option value="Good">Good</option>
                  <option value="Fair">Fair</option>
                  <option value="Poor">Poor</option>
                </select>
              </div>
              <div class="mt-3" v-else>
                <label class="form-label fw-bold">Device Condition</label>
                <div class="bg-light p-2 rounded border">
                  <span
                    class="condition-badge"
                    :class="getConditionClass(device.condition)"
                  >
                    {{ device.condition }}
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
/* Keep your existing styles */
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

.device-specs {
  background-color: #f8f9fa;
  border-radius: 0.5rem;
  padding: 1rem;
}

.spec-item {
  display: flex;
  justify-content: space-between;
  padding: 0.25rem 0;
  border-bottom: 1px solid #e9ecef;
}

.spec-item:last-child {
  border-bottom: none;
}

.spec-label {
  color: #6c757d;
  font-weight: 500;
}

.spec-value {
  font-weight: 600;
  color: #212529;
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

/* Updated button styles to match refresh button */
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
</style>
