from flask import Flask, render_template, request , redirect
from flask import Blueprint
from controllers.sesion_controller import sesions
from models.member import Member
from models.booking import Booking
import repositories.member_repositories as member_repositories
import repositories.sesion_repositories as sesion_repositories
import repositories.booking_repositories as booking_repositories

members_blueprint = Blueprint("members", __name__ )

@members_blueprint.route("/members")
def members():
    members = member_repositories.select_all()
    sesions = sesion_repositories.select_all()
    return render_template('member/members.html', members = members, sesions = sesions)

@members_blueprint.route("/member/<member_id>/bookings/<sesion_id>")
def confirm_booking(member_id,sesion_id):
    # memberId = member_repositories.select(member_id)
    # sesionId = sesion_repositories.select(sesion_id)
    booking = Booking(member_id,sesion_id)
    booking_repositories.create_booking(booking)
    return redirect("/bookings/bookings")

@members_blueprint.route('/members/addnewmember')
def new_members():
    members = member_repositories.select_all()
    return render_template('member/addnewmember.html', members = members)

@members_blueprint.route("/members/addnewmember", methods=['POST'])
def create_member():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    membership = request.form['membership']
    active_status = request.form['active_status']
    member= Member(first_name, last_name, membership, active_status)
    member_repositories.create_member(member)
    return redirect("/members")

@members_blueprint.route("/member/<id>/edit")
def edit_member(id):
    member = member_repositories.select(id)
    return render_template('member/edit.html', member = member)

@members_blueprint.route("/members/<id>", methods = ['POST'])   
def update_member(id):

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    membership = request.form['membership']
    active_status = request.form['active_status']
    member = Member(first_name,last_name,membership,active_status,id)

    member_repositories.update(member)
    return redirect('/members')

# @members_blueprint.route('/members/<id>/bookings')