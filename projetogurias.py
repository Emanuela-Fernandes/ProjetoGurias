from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import CadastraUsuarioForm, LoginUsuarioForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projetoguriais.db'
app.config['SECRET_KEY'] = 'd77a98b1c04bc37e50787352e80323e3'

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    passaword = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    datadenascimento = db.Column(db.Date(), nullable =False)

class Visitante(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    datadenascimento = db.Column(db.Date(), nullable =False)
    escrevaRelato = db.Column(db.String(1000))



    def __repr__(self):
        return '<User %r>' % self.username
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/login')
def login():
    form=LoginUsuarioForm()
    return render_template('pages/login.html', formulario=form)
@app.route('/cadastro', methods=['GET', 'Post'])
def cadastro():

    form= CadastraUsuarioForm()

    return render_template('pages/cadastro.html', formulario=form)
@app.route('/lute')
def lute():
    return render_template('pages/lute.html')
@app.route('/acompanhamento')
def acompanhamento():
    return render_template('pages/acompanhamento.html')

if __name__ == '__main__':
    app.run(debug=True, port = 5555)
