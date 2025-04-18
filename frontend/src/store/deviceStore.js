import { reactive } from "vue";
import { api } from "@/store/api.js";

export const deviceStore = reactive({
  devices: new Map(),

  setDevices(devices) {
    deviceStore.devices.clear();
    devices.forEach((device) => {
      deviceStore.devices.set(device.id, device);
    });
  },

  async addDevice(deviceId, device, imageFile) {
    const formData = new FormData();

    formData.append("device", JSON.stringify(device));
    formData.append("image", imageFile);

    try {
      const response = await fetch(`${api}/devices`, {
        method: "POST",
        body: formData,
        credentials: "include",
      });

      if (!response.ok) {
        throw "failed to add device";
      }

      const data = await response.json();

      this.devices.set(deviceId, data.device);
    } catch (e) {
      console.error(e);
    }
  },

  async refreshDevices() {
    try {
      const response = await fetch(`${api}/devices`, {
        method: "GET",
        credentials: "include",
      });

      if (!response.ok) {
        throw "failed to load devices";
      }

      const data = await response.json();

      this.setDevices(data.devices);
      return { ok: true };
    } catch (e) {
      console.error(e);
      return { ok: false };
    }
  },

  getDeviceImage(device) {
    if (device && device.imageUrl) {
      return api + device.imageUrl;
    }

    return "/Eco-Dispose/assets/devices/device.png";
  },

  async updateDevice(deviceId, device) {
    try {
      const response = await fetch(`${api}/devices/${deviceId}`, {
        method: "PUT",
        body: JSON.stringify(device),
        headers: { "Content-Type": "application/json" },
        credentials: "include",
      });

      if (!response.ok) {
        throw "failed to update device";
      }

      const data = await response.json();

      this.devices.set(deviceId, data.device);
      return { ok: true };
    } catch (e) {
      console.error(e);
      return { ok: false };
    }
  },

  async deleteDevice(deviceId) {
    try {
      const response = fetch(`${api}/devices/${deviceId}`, {
        method: "DELETE",
        credentials: "include",
      });

      if (!response.ok) {
        throw "failed to delete device";
      }

      // this.devices.delete(deviceId);
    } catch (e) {
      console.error(e);
    }
  },
});
