import os

from flask import Blueprint, json, jsonify, request
from flask_login import current_user, login_required
from datetime import datetime
from sqlalchemy.exc import SQLAlchemyError

from .config import UPLOAD_FOLDER_PATH
from .util import save_file

from .models import Device, db, DeviceCondition, DeviceStatus

devices = Blueprint("devices", __name__)


@devices.get("/")
@login_required
def get_devices():
    """List all devices for normal users or all devices for admins"""
    try:
        if current_user.is_admin:
            # Admin can get all devices
            all_devices = Device.query.all()
        else:
            # Normal user gets their own devices
            all_devices = current_user.devices

        return jsonify([device.to_json() for device in all_devices])

    except SQLAlchemyError:
        return jsonify(
            {"error": "An unexpected error occurred. Please try again later."}
        ), 500


@devices.post("/")
@login_required
def add_device():
    """Submit a new device (only normal users can add)"""
    try:
        if current_user.is_admin:
            return jsonify({"error": "Admins cannot add devices"}), 403

        form_data = request.form.get("device")

        if not form_data:
            return jsonify({"error": "Missing device data"}), 400

        device_json = json.loads(form_data)

        name = device_json["name"]
        type = device_json["type"]
        defects = device_json["defects"]
        user_description = device_json["userDescription"]
        image = request.files.get("image")

        # Ensure required fields are present for adding a device
        if not name or not user_description or not type or not defects or not image:
            return jsonify(
                {
                    "error": "Missing required fields: name, type, defects, userDescription, or image"
                }
            ), 400

        image_url = save_file(image)

        if not image_url:
            return jsonify({"error": "Invalid image file"}), 400

        # Create the device
        device = Device(
            name=name,  # type: ignore
            type=type,  # type: ignore
            defects=defects,  # type: ignore
            user_description=user_description,  # type: ignore
            image_url=image_url,  # type: ignore
            upload_date=datetime.now(),  # type: ignore
            user_id=current_user.id,  # type: ignore
        )

        db.session.add(device)
        db.session.commit()

        return jsonify(
            {
                "message": "Device added successfully",
                "device": device.to_json(),
            }
        ), 201

    except SQLAlchemyError:
        return jsonify(
            {"error": "An unexpected error occurred. Please try again later."}
        ), 500


@devices.put("/<int:id>")
@login_required
def update_device(id):
    """Update device (Admins can update any device, users can only update their own)"""
    try:
        device = Device.query.get(id)

        if not device:
            return jsonify({"error": "Device not found"}), 404

        # Admin can update any device
        if current_user.is_admin:
            pass  # No restriction for admin

        # Normal users can only update their own devices
        elif device.user_id != current_user.id:
            return jsonify({"error": "Unauthorized"}), 403

        # Get the JSON data from the request body
        data = request.get_json()

        # Update fields
        try:
            if "condition" in data:
                device.condition = DeviceCondition(data["condition"])
            if "status" in data:
                device.status = DeviceStatus(data["status"])
        except ValueError:
            return jsonify({"error": "Invalid status or condition value"}), 400
        if "estimatedPrice" in data:
            device.estimated_price = float(data["estimatedPrice"])
        if "adminNotes" in data:
            device.admin_notes = data["adminNotes"]

        db.session.commit()

        return jsonify(
            {
                "message": "device updated successfully",
                "device": device.to_json(),
            }
        ), 200

    except SQLAlchemyError:
        return jsonify(
            {"error": "An unexpected error occurred. Please try again later."}
        ), 500


@devices.delete("/<int:id>")
@login_required
def delete_device(id):
    """Delete a device (only the user who added it can delete it)"""
    try:
        device = Device.query.get(id)

        if not device:
            return jsonify({"error": "Device not found"}), 404

        if device.user_id != current_user.id:
            return jsonify({"error": "You can only delete your own devices"}), 403

        db.session.delete(device)
        db.session.commit()

        # delete device's stored image
        if device.image_url:
            # Extract filename from the url
            filename = os.path.basename(device.image_url)
            file_path = os.path.join(UPLOAD_FOLDER_PATH, filename)

            if os.path.exists(file_path):
                os.remove(file_path)

        return jsonify({"message": "Device deleted successfully"}), 200

    except SQLAlchemyError:
        return jsonify(
            {"error": "An unexpected error occurred. Please try again later."}
        ), 500
