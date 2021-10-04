from flask import Flask, render_template

from controllers.sesion_controller import sesions_blueprint


app = Flask(__name__)

app.register_blueprint(sesions_blueprint)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sesions')
def sesions():
    return render_template('sesion/sesions.html')

@app.route('/sesion/addnew')
def create_sesion():
    return render_template('sesion/addnew.html')


if __name__ == '__main__':
    app.run(debug=True)