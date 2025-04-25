<script setup>
import { ref, onMounted, computed } from "vue";
import { deviceStore } from "@/store/deviceStore.js";
import { Modal } from "bootstrap";
import { toastStore } from "@/store/toastStore.js";

// Refs for modals and selected device
const selectedDeviceId = ref(null);
const selectedDevice = ref(null);

const devices = computed(() => deviceStore.devices);

// Device details modal handling
const showDeviceDetails = (deviceId) => {
  selectedDeviceId.value = deviceId;
  selectedDevice.value = deviceStore.devices.get(deviceId);

  const modal = new Modal(document.getElementById("deviceDetailsModal"));
  modal.show();
};

// Tracking modal handling
const showTracking = (deviceId) => {
  selectedDeviceId.value = deviceId;
  selectedDevice.value = deviceStore.devices.get(deviceId);

  const modal = new Modal(document.getElementById("trackingModal"));
  modal.show();
};

// Accept offer functionality
const acceptOffer = (deviceId) => {
  deviceStore.devices.get(deviceId).status = "accepted";

  const modal = Modal.getInstance(
    document.getElementById("deviceDetailsModal"),
  );
  if (modal) modal.hide();

  deviceStore
    .deleteDevice(deviceId)
    .then((response) => {
      if (!response.ok) {
        toastStore.showToast("Failed", "Failed to accept offer", "danger");
        return;
      }

      toastStore.showToast(
        "Offer Accepted",
        `You've successfully accepted the offer for your ${deviceStore.devices.get(deviceId).name} at $${deviceStore.devices.get(deviceId).estimatedPrice}.`,
        "success",
      );
    })
    .catch((e) => console.error(e));
};

// Reject offer functionality
const rejectOffer = (deviceId) => {
  deviceStore.devices.get(deviceId).status = "rejected";

  const modal = Modal.getInstance(
    document.getElementById("deviceDetailsModal"),
  );
  if (modal) modal.hide();

  deviceStore
    .updateDevice(deviceId, deviceStore.devices.get(deviceId))
    .then((response) => {
      if (!response.ok) {
        toastStore.showToast("Failed", "Failed to reject offer", "danger");
        return;
      }

      toastStore.showToast(
        "Offer Rejected",
        `You've rejected the offer for your ${deviceStore.devices.get(deviceId).name}. We'll be in touch with next steps.`,
        "danger",
      );
    })
    .catch((e) => console.error(e));
};

// Helper methods
const getDeviceIcon = (deviceName) => {
  return deviceName.toLowerCase().includes("macbook") ||
    deviceName.toLowerCase().includes("laptop")
    ? "fas fa-laptop"
    : "fas fa-mobile-alt";
};

const getStatusClass = (status) => {
  const statusMap = {
    waiting: "status-waiting",
    collected: "status-collected",
    evaluated: "status-evaluated",
    accepted: "status-accepted",
    rejected: "status-rejected",
  };
  return statusMap[status] || "";
};

const conditionBadgeClass = (condition) => {
  const map = {
    null: "",
    excellent: "bg-success text-white",
    good: "bg-info text-white",
    fair: "bg-warning text-dark",
    poor: "bg-danger text-white",
  };
  return map[condition] || "bg-secondary";
};

const getStatusAlertClass = (status) => {
  const alertMap = {
    waiting: "alert-primary",
    collected: "alert-warning",
    evaluated: "alert-success",
    accepted: "alert-info",
    rejected: "alert-danger",
  };
  return alertMap[status] || "alert-secondary";
};

const getStatusIcon = (status) => {
  const iconMap = {
    waiting: "fas fa-hourglass-half",
    collected: "fas fa-truck",
    evaluated: "fas fa-clipboard-check",
    accepted: "fas fa-check-circle",
    rejected: "fas fa-times-circle",
  };
  return iconMap[status] || "fas fa-info-circle";
};

const getStatusText = (status) => {
  const textMap = {
    waiting: "Waiting for Courier",
    collected: "Collected by Courier",
    evaluated: "Evaluated",
    accepted: "Accepted",
    rejected: "Rejected",
  };
  return textMap[status] || "Unknown";
};

const getCurrentDateTime = () => {
  return new Date().toLocaleString();
};

// Lifecycle hooks
onMounted(() => {
  // Set up modal event listeners
  document
    .getElementById("deviceDetailsModal")
    .addEventListener("hidden.bs.modal", () => {
      selectedDeviceId.value = null;
      selectedDevice.value = null;
    });

  document
    .getElementById("trackingModal")
    .addEventListener("hidden.bs.modal", () => {
      selectedDeviceId.value = null;
      selectedDevice.value = null;
    });
});
</script>

<template>
  <!-- Hero Section -->
  <div class="bg-light py-5">
    <div class="container">
      <div class="row align-items-center justify-content-center">
        <div class="col-lg-8 text-center">
          <h1 class="fw-bold text-primary mb-3">Track Your Devices</h1>
          <p class="lead text-secondary mb-4">
            Monitor the status of your submitted devices and make decisions in
            real-time
          </p>
          <router-link
            to="/upload"
            class="btn btn-primary btn-lg px-4 py-2 shadow-sm w-75"
          >
            <i class="fas fa-upload me-2"></i> Upload New Device
          </router-link>
        </div>
      </div>
    </div>
  </div>
  <!-- Empty State when no devices are present -->
  <div v-if="devices.size === 0" class="container my-5">
    <div class="empty-state">
      <div class="text-center py-5">
        <i class="fas fa-box-open fa-3x text-muted mb-3"></i>
        <h4>No devices found</h4>
        <p class="text-muted">
          You haven't submitted any devices for recycling yet
        </p>
        <router-link to="/upload" class="btn btn-primary">
          <i class="fas fa-upload me-2"></i>Upload New Device
        </router-link>
      </div>
    </div>
  </div>

  <!-- Devices List with Status -->
  <div v-else class="container my-5">
    <h2 class="fw-bold text-center text-primary mb-4 section-header">
      Your Devices
    </h2>
    <div class="row justify-content-center">
      <div class="col-md-10 col-lg-8">
        <div class="card-list">
          <!-- Device Card for each device -->
          <div
            v-for="[id, device] of devices"
            :key="id"
            class="card mb-3 device-card"
          >
            <div class="card-body d-flex align-items-center p-3">
              <div class="icon-wrapper">
                <i :class="getDeviceIcon(device.name)" class="device-icon"></i>
              </div>

              <div class="flex-grow-1">
                <div
                  class="d-flex justify-content-between align-items-center mb-2"
                >
                  <h5 class="mb-0 fw-bold">{{ device.name }}</h5>
                  <span
                    class="device-status"
                    :class="getStatusClass(device.status)"
                  >
                    <i :class="getStatusIcon(device.status)" class="me-1"></i>
                    {{ getStatusText(device.status) }}
                  </span>
                </div>

                <div class="d-flex justify-content-between align-items-center">
                  <div>
                    <span
                      class="badge rounded-pill me-2"
                      :class="conditionBadgeClass(device.condition)"
                    >
                      {{ device.condition }}
                    </span>
                    <span
                      v-if="
                        ['evaluated', 'accepted', 'rejected'].includes(
                          device.status,
                        )
                      "
                      class="text-muted small"
                    >
                      Est. Value: ${{ device.estimatedPrice }}
                    </span>
                    <span v-else class="text-muted small fst-italic">
                      <i class="fas fa-hourglass-half me-1"></i>Pending
                      evaluation
                    </span>
                  </div>
                  <div>
                    <button
                      class="btn btn-sm btn-outline-primary me-2"
                      @click="showDeviceDetails(id)"
                    >
                      <i class="fas fa-info-circle me-1"></i>
                      Details
                    </button>
                    <button
                      class="btn btn-sm btn-primary"
                      @click="showTracking(id)"
                    >
                      <i class="fas fa-truck me-1"></i>
                      Track
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>

  <!-- Device Details Modal -->
  <div
    class="modal fade"
    id="deviceDetailsModal"
    tabindex="-1"
    aria-hidden="true"
  >
    <div class="modal-dialog modal-dialog-centered modal-lg">
      <div class="modal-content" v-if="selectedDevice">
        <div class="modal-header">
          <h5 class="modal-title">Device Evaluation Result</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="row">
            <div class="col-md-5 text-center">
              <img
                :src="deviceStore.getDeviceImage(selectedDevice)"
                class="img-fluid rounded shadow-sm mb-3"
                alt="Device Image"
              />
              <div
                v-if="
                  ['evaluated', 'accepted', 'rejected'].includes(
                    selectedDevice.status,
                  )
                "
                class="price-badge mb-3"
              >
                ${{ selectedDevice.estimatedPrice }}
              </div>
              <div v-else class="alert alert-info mb-3 px-4 py-3 rounded-3">
                <i class="fas fa-hourglass-half me-2"></i>
                <span class="fw-semibold">Evaluation in progress</span>
                <p class="small mb-0 mt-1">
                  Price will be available after our technician assesses your
                  device.
                </p>
              </div>
              <div class="text-center mb-3">
                <span
                  class="badge rounded-pill px-3 py-2"
                  :class="conditionBadgeClass(selectedDevice.condition)"
                >
                  {{ selectedDevice?.condition }} Condition
                </span>
              </div>
            </div>

            <div class="col-md-7">
              <h4 class="mb-3">{{ selectedDevice.name }}</h4>

              <div
                class="alert"
                :class="getStatusAlertClass(selectedDevice.status)"
              >
                <i
                  :class="getStatusIcon(selectedDevice.status)"
                  class="me-2"
                ></i>
                Status:
                <strong>{{ getStatusText(selectedDevice.status) }}</strong>
              </div>

              <div class="bg-light rounded p-3 mb-4">
                <div class="device-detail-item mb-3">
                  <h6 class="fw-bold">User Description</h6>
                  <p class="detail-content">
                    {{ selectedDevice.userDescription }}
                  </p>
                </div>

                <div class="device-detail-item mb-3">
                  <h6 class="fw-bold">Known defects</h6>
                  <p class="detail-content">{{ selectedDevice.defects }}</p>
                </div>

                <div class="device-detail-item border-bottom pb-3">
                  <h6 class="fw-bold">Added On</h6>
                  <p class="detail-content">{{ selectedDevice.uploadDate }}</p>
                </div>
              </div>

              <div v-if="selectedDevice.adminNotes" class="mb-4">
                <h6 class="fw-bold mb-2">Technician Notes</h6>
                <p class="detail-content">{{ selectedDevice.adminNotes }}</p>
              </div>
            </div>
          </div>
        </div>
        <div class="modal-footer justify-content-center">
          <div v-if="selectedDevice.status === 'evaluated'">
            <button
              class="btn btn-lg btn-success me-2"
              @click="acceptOffer(selectedDeviceId)"
            >
              <i class="fas fa-check me-2"></i> Accept Offer
            </button>
            <button
              class="btn btn-lg btn-outline-danger"
              @click="rejectOffer(selectedDeviceId)"
            >
              <i class="fas fa-times me-2"></i> Reject Offer
            </button>
          </div>
          <button
            v-else
            type="button"
            class="btn btn-secondary px-4"
            data-bs-dismiss="modal"
          >
            <i class="fas fa-times me-1"></i> Close
          </button>
        </div>
      </div>
    </div>
  </div>

  <!-- Tracking Modal -->
  <div class="modal fade" id="trackingModal" tabindex="-1" aria-hidden="true">
    <div class="modal-dialog modal-dialog-centered modal-lg">
      <div class="modal-content" v-if="selectedDevice">
        <div class="modal-header">
          <h5 class="modal-title">Track Your Device</h5>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
            aria-label="Close"
          ></button>
        </div>
        <div class="modal-body">
          <div class="text-center mb-4">
            <h4>{{ selectedDevice.name }}</h4>
          </div>

          <div class="tracking-progress">
            <div
              class="tracking-step"
              :class="{
                active: [
                  'waiting',
                  'collected',
                  'evaluated',
                  'accepted',
                  'rejected',
                ].includes(selectedDevice.status),
              }"
            >
              <div class="step-icon">
                <i class="fas fa-box"></i>
              </div>
              <div class="step-label">Requested</div>
            </div>
            <div
              class="tracking-step"
              :class="{
                active: [
                  'collected',
                  'evaluated',
                  'accepted',
                  'rejected',
                ].includes(selectedDevice.status),
              }"
            >
              <div class="step-icon">
                <i class="fas fa-truck"></i>
              </div>
              <div class="step-label">Collected</div>
            </div>
            <div
              class="tracking-step"
              :class="{
                active: ['evaluated', 'accepted', 'rejected'].includes(
                  selectedDevice.status,
                ),
              }"
            >
              <div class="step-icon">
                <i class="fas fa-clipboard-check"></i>
              </div>
              <div class="step-label">Evaluated</div>
            </div>
            <div
              class="tracking-step"
              :class="{
                active: ['accepted', 'rejected'].includes(
                  selectedDevice.status,
                ),
              }"
            >
              <div class="step-icon">
                <i class="fas fa-check-circle"></i>
              </div>
              <div class="step-label">Completed</div>
            </div>
          </div>

          <div class="modal-tracking-status border-top pt-3 mt-4">
            <h5 class="mb-3">Current Status:</h5>
            <div :class="'alert ' + getStatusAlertClass(selectedDevice.status)">
              <i :class="getStatusIcon(selectedDevice.status)" class="me-2"></i>
              <strong>{{ getStatusText(selectedDevice.status) }}</strong>
            </div>
            <p class="text-muted small">
              Last updated: {{ getCurrentDateTime() }}
            </p>
          </div>
        </div>
        <div class="modal-footer justify-content-center">
          <button
            type="button"
            class="btn btn-secondary px-4"
            data-bs-dismiss="modal"
          >
            <i class="fas fa-times me-1"></i> Close
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
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

.device-card {
  border-radius: 15px;
  border: none;
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
  border-left: 5px solid var(--bs-primary);
}

.device-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 24px rgba(0, 0, 0, 0.1);
  background-color: #f0f4ff;
}

.icon-wrapper {
  background-color: #f8f9fa;
  width: 50px;
  height: 50px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  margin-right: 15px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.device-icon {
  font-size: 1.5rem;
  color: var(--bs-primary);
}

/* Status indicators */
.device-status {
  display: inline-block;
  padding: 4px 10px;
  border-radius: 30px;
  font-size: 0.8rem;
  font-weight: 600;
}

/* Tracking progress section */
.tracking-progress {
  position: relative;
  display: flex;
  justify-content: space-between;
  margin: 2rem 0;
}

.tracking-progress::after {
  content: "";
  position: absolute;
  top: 25px;
  left: 0;
  width: 100%;
  height: 3px;
  background-color: #e9ecef;
  z-index: 0;
}

.tracking-step {
  position: relative;
  z-index: 1;
  text-align: center;
  min-width: 120px;
}

.step-icon {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  background-color: #e9ecef;
  display: flex;
  align-items: center;
  justify-content: center;
  margin: 0 auto 10px;
  transition: all 0.3s ease;
}

.tracking-step.active .step-icon {
  background-color: var(--bs-primary);
  box-shadow: 0 0 0 5px rgba(13, 110, 253, 0.2);
}

.tracking-step.active .step-icon i {
  color: white;
}

.price-badge {
  display: inline-block;
  background: linear-gradient(135deg, #4361ee 0%, #4895ef 100%);
  padding: 0.5rem 1.5rem;
  border-radius: 50px;
  box-shadow: 0 4px 15px rgba(67, 97, 238, 0.3);
  position: relative;
  overflow: hidden;
}

.price-badge::before {
  content: "";
  position: absolute;
  top: -10px;
  right: -10px;
  background: rgba(255, 255, 255, 0.2);
  width: 40px;
  height: 40px;
  border-radius: 50%;
}
/* Device detail styling */
.device-detail-item {
  margin-bottom: 1rem;
}

.detail-content {
  background-color: white;
  padding: 0.75rem;
  border-radius: 8px;
  margin-bottom: 0;
  border-left: 3px solid var(--bs-primary);
  white-space: pre-line; /* Preserves line breaks */
  word-break: break-word; /* Prevents overflow */
}

/* Optional: Add a max height with scroll for very long descriptions */
.detail-content.long-text {
  max-height: 150px;
  overflow-y: auto;
}
/* Modal header styling */
.modal-header {
  background-image: linear-gradient(120deg, #4361ee, #4895ef);
  border-bottom: none;
}

.modal-header .modal-title {
  color: white;
  font-weight: 600;
}

@media (max-width: 768px) {
  .tracking-step {
    min-width: 80px;
    font-size: 0.85rem;
  }

  .step-icon {
    width: 40px;
    height: 40px;
  }
}

@media (max-width: 576px) {
  .tracking-progress {
    flex-direction: column;
    align-items: flex-start;
  }

  .tracking-progress::after {
    width: 3px;
    height: 100%;
    top: 0;
    left: 25px;
  }

  .tracking-step {
    width: 100%;
    margin-bottom: 20px;
    display: flex;
    align-items: center;
    text-align: left;
  }

  .step-icon {
    margin: 0 15px 0 0;
  }
}

.empty-state {
  background-color: #ffffff;
  border-radius: 0.75rem;
  padding: 3rem 1rem;
  box-shadow: 0 5px 15px rgba(0, 0, 0, 0.08);
}
</style>
