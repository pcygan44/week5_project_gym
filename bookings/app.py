from flask import Flask, render_template

from controllers.sesion_controller import sesions_blueprint
from controllers.member_controller import members_blueprint

app = Flask(__name__)

app.register_blueprint(sesions_blueprint)
app.register_blueprint(members_blueprint)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sesions')
def sesions():
    return render_template('sesion/sesions.html')

@app.route('/members')
def members():
    return render_template('member/members.html')

@app.route('/sesions/addnew')
def create_sesion():
    return render_template('sesion/addnew.html')

@app.route('/members/addnewmember')
def create_nember():
    return render_template ('member/addnewmember.html')

@app.route('/sesions/<id>/edit')
def edit_sesion(id):
    return render_template('sesion/edit.html')

@app.route('/sesions/<id>')
def update_sesion(id):
    return render_template('/sesion')


@app.route('/members/<id>/edit')
def edit_member(id):
    return render_template('/members')

@app.route('/members/<id>')
def update_member(id):
    return render_template('/members')



if __name__ == '__main__':
    app.run(debug=True)