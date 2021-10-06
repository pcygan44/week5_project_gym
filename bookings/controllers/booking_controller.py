from flask import Flask, render_template, request, redirect
from flask import Blueprint
from controllers.sesion_controller import sesions
from controllers.member_controller import members
from models.sesion import Sesion
from models.booking import Booking

import repositories.booking_repositories as booking_repositories
import repositories.sesion_repositories as sesion_repositories
import repositories.member_repositories as  member_repositories

bookings_blueprint = Blueprint("bookings", __name__)

@bookings_blueprint.route("/bookings/bookings")
def select_sesion():
    sesions = sesion_repositories.select_all()
    return redirect ('/sesions')
