from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'd77a98b1c04bc37e50787352e80323e3'

@app.route('/index')
def index():
    return render_template('index.html')
@app.route('/login')
def login():
    return render_template('pages/login.html')
@app.route('/cadastro')
def cadastro():
    return render_template('pages/cadastro.html')
@app.route('/lute')
def lute():
    return render_template('pages/lute.html')
@app.route('/acompanhamento')
def acompanhamento():
    return render_template('pages/acompanhamento.html')
if __name__ == '__main__':
    app.run(debug=True)
