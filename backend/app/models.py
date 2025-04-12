import enum
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(30), nullable=False, unique=True)
    password = db.Column(db.String(30), nullable=False)
    phone_number = db.Column(db.String(30))
    is_admin = db.Column(db.Boolean, nullable=False, default=False)
    profile_image_url = db.Column(db.String(80))
    address_id = db.Column(db.Integer, db.ForeignKey("address.id"))
    address = db.relationship("Address", backref="user")
    devices = db.relationship("Device", backref="user")

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "phoneNumber": self.phone_number,
            "isAdmin": self.is_admin,
            "profileImageUrl": self.profile_image_url,
            "address": self.address.to_json(),
            "devices": [device.to_json() for device in self.devices],  # type: ignore
        }


class Address(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    street = db.Column(db.String(30))
    city = db.Column(db.String(30))
    country = db.Column(db.String(30))
    zip_code = db.Column(db.String(30))

    def to_json(self):
        return {
            "id": self.id,
            "street": self.street,
            "city": self.city,
            "country": self.country,
            "zipCode": self.zip_code,
        }


class DeviceCondition(enum.Enum):
    EXCELLENT = "excellent"
    GOOD = "good"
    FAIR = "fair"
    POOR = "poor"


class DeviceStatus(enum.Enum):
    WAITING = "waiting"
    COLLECTED = "collected"
    EVALUATED = "evaluated"
    ACCEPTED = "accepted"
    REJECTED = "rejected"


class Device(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

    condition = db.Column(db.Enum(DeviceCondition))
    status = db.Column(db.Enum(DeviceStatus))
    estimated_price = db.Column(db.Float)
    admin_notes = db.Column(db.String(10000))

    user_description = db.Column(db.String(10000), nullable=False)
    image_url = db.Column(db.String(80), nullable=False)
    upload_date = db.Column(db.DateTime, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

    def to_json(self):
        return {
            "id": self.id,
            "name": self.name,
            "condition": self.condition.value if self.condition else None,
            "status": self.status.value if self.status else None,
            "estimatedPrice": self.estimated_price,
            "adminNotes": self.admin_notes,
            "userDescription": self.user_description,
            "imageUrl": self.image_url,
            "uploadDate": self.upload_date.isoformat() if self.upload_date else None,
            "userId": self.user_id,
        }
