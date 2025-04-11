from flask import Blueprint, jsonify, request
from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from sqlalchemy import select
from sqlalchemy.exc import IntegrityError

from .models import Address, User, db

auth = Blueprint("auth", __name__)
login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    return db.session.execute(
        select(User).where(User.id == user_id)
    ).scalar_one_or_none()


@login_manager.unauthorized_handler
def unauthorized():
    return jsonify({"message": "not allowed"}), 401


@auth.post("/register")
def register():
    first_name = request.form.get("firstName")
    last_name = request.form.get("lastName")
    email = request.form.get("email")
    password = request.form.get("password")

    if not first_name or not last_name or not email or not password:
        return jsonify({"message": "missing required fields"}), 400

    try:
        # Create and save the address first
        address = Address()
        db.session.add(address)
        db.session.flush()  # Flush to get the address ID without committing

        user = User(
            first_name=first_name,  # type: ignore
            last_name=last_name,  # type: ignore
            email=email,  # type: ignore
            address_id=address.id,  # type: ignore
        )
        user.set_password(password)

        db.session.add(user)
        db.session.commit()

        return jsonify(
            {
                "message": "registered successfully",
                "user": user.to_json(),
            }
        ), 201

    except IntegrityError:
        db.session.rollback()
        return jsonify({"error": "email already in use"}), 409


@auth.post("/login")
def login():
    email = request.form.get("email")
    password = request.form.get("password")

    if not email or not password:
        return jsonify({"error": "missing email or password"}), 400

    user = db.session.execute(
        select(User).where(User.email == email)
    ).scalar_one_or_none()

    if user is None:
        return jsonify({"message": "user not found"}), 404

    if not user.check_password(password):
        return jsonify({"message": "wrong credentials"}), 401

    login_user(user)

    return jsonify(
        {
            "message": f"logged in as {user.first_name}",
            "user": user.to_json(),
        }
    ), 200


@auth.get("/profile")
@login_required
def profile():
    return jsonify({"user": current_user.to_json()}), 200


@auth.post("/edit")
@login_required
def edit():
    try:
        data = request.json

        if data is None:
            return jsonify({"error": "no data provided"}), 400

        # TODO: handle changing profile picture
        if "firstName" in data:
            current_user.first_name = data["firstName"]
        if "lastName" in data:
            current_user.last_name = data["lastName"]
        if "phoneNumber" in data:
            current_user.phone_number = data["phoneNumber"]

        user_address = data["address"]

        if user_address:
            if "street" in user_address:
                current_user.address.street = user_address["street"]
            if "country" in user_address:
                current_user.address.country = user_address["country"]
            if "city" in user_address:
                current_user.address.city = user_address["city"]
            if "zipCode" in user_address:
                current_user.address.zip_code = user_address["zipCode"]

        db.session.commit()

        return jsonify(
            {
                "message": "user details updated successfully",
                "user": current_user.to_json(),
            }
        ), 200
    except IntegrityError:
        db.session.rollback()
        # this shouldn't happen but just in case XD
        return jsonify({"error": "invalid user state"}), 409


@auth.post("/logout")
@login_required
def logout():
    logout_user()
    return jsonify({"message": "logged out successfully"}), 200
