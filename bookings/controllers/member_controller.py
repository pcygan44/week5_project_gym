from flask import Flask, render_template, request , redirect
from flask import Blueprint
from models.member import Member
import repositories.member_repositories as member_repositories
import repositories.sesion_repositories as sesion_repositories

members_blueprint = Blueprint("members", __name__ )

@members_blueprint.route("/members")
def members():
    members = member_repositories.select_all()
    return render_template('member/members.html', members = members)


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