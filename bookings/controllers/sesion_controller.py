from flask import Flask, render_template, request , redirect
from flask import Blueprint
from models.sesion import Sesion
from models.member import Member
import repositories.sesion_repositories as sesion_repositories
import repositories.member_repositories as member_repositories

sesions_blueprint = Blueprint("sesions", __name__ )

@sesions_blueprint.route("/sesions")
def sesions():
    sesions = sesion_repositories.select_all()
    return render_template("sesion/sesions.html", sesions = sesions)


@sesions_blueprint.route("/sesions/addnew")    
def new_sesions():
    sesions = sesion_repositories.select_all()
    return render_template("/sesion/addnew.html", sesions = sesions )
    

@sesions_blueprint.route("/sesions/addnew", methods=['POST'])
def create_sesion():
    # print (request.form, '----------------------------')
    sesion_name = request.form['sesion_name']
    duration = request.form['duration']
    sesion_date = request.form['sesion_date']
    sesion_time = request.form['sesion_time']
    capacity = request.form['capacity']
    active_status = request.form['active_status']
    # member = member_repositories.select(member.id)
    sesion = Sesion(sesion_name, duration, sesion_date, sesion_time, capacity, active_status)
    sesion_repositories.create_sesion(sesion)
    return redirect("/sesions")
    # return render_template("sesion/addnew.html", sesions = sesions)   #redirect("/sesions")

@sesions_blueprint.route("/sesion/<id>/edit")
def edit_sesion(id):
    sesion = sesion_repositories.select(id)
    return render_template('sesion/edit.html', sesion = sesion )

@sesions_blueprint.route("/sesions/<id>", methods=['POST'])
def update_sesion(id):

    sesion_name = request.form['sesion_name']
    duration = request.form['duration']
    sesion_date = request.form['sesion_date']
    sesion_time = request.form['sesion_time']
    capacity = request.form['capacity']
    active_status = request.form['active_status']
    sesion = Sesion(sesion_name ,duration,sesion_date,sesion_time,capacity,active_status,id)

    sesion_repositories.update(sesion)
    return redirect ('/sesions')

@sesions_blueprint.route("/sesions/<id>/booked")
def show_booked(id):
    members = sesion_repositories.show_booked(id)
    
    return render_template('/sesion/booked.html',members = members)