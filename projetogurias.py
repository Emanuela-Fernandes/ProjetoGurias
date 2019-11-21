from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from forms import CadastraUsuarioForm, LoginUsuarioForm, DeixeSeuRelatorioForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///projetoguriais.db'
app.config['SECRET_KEY'] = 'd77a98b1c04bc37e50787352e80323e3'

db = SQLAlchemy(app)

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    senha = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    datadenascimento = db.Column(db.Date(), nullable =False)

    def __repr__(self):
        return '<User %r>' % self.username
    

class Relato(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    data = db.Column(db.Date, nullable =False)
    escrevaRelato = db.Column(db.String(1000))



    def __repr__(self):
        return '<User %r>' % self.username


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/login',  methods=['GET', 'Post'])
def login():


    form=LoginUsuarioForm()



    return render_template('pages/login.html', formulario=form)
@app.route('/cadastro', methods=['GET', 'Post'])
def cadastro():

    form= CadastraUsuarioForm()
    if form.validate_on_submit():
        C=Usuario()
        C.username=form.username.data
        C.datadenascimento=form.datadenascimento.data
        C.email=form.email.data
        C.senha=form.senha.data
        db.session.add(C)
        db.session.commit()
    
    return render_template('pages/cadastro.html', formulario=form)

@app.route('/lute',  methods=['GET', 'POST'])
def lute():

    form= DeixeSeuRelatorioForm()
    #print form.validate_on_submit()
    if form.validate_on_submit():
   #     print ('eu entrei aq')
        r=Relato()
        r.username=form.username.data
        r.data=datetime.now()
        r.escrevaRelato=form.escrevaRelato.data
        db.session.add(r)
        db.session.commit()

    return render_template('pages/lute.html', formulario=form)

@app.route('/acompanhamento')
def acompanhamento():
    return render_template('pages/acompanhamento.html')

#@app.route('/mensagens')
#def acompanhamento():
#    return render_template('pages/mensagens.html')

if __name__ == '__main__':
    app.run(debug=True)
