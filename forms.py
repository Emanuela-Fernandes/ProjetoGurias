from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class CadastraUsuarioForm(FlaskForm):
    username = StringField(
        'Nome:',
        validators=[DataRequired(), Length(min=2, max=80)]
    )
    email = StringField (
        'E-mail:',
        validators=[DataRequired(), Email()]
    )
    
    senha = PasswordField (
        'Senha:',
        validators=[DataRequired(), Length(min=2, max=80)]
    )
    
    botao = SubmitField('Cadastrar')
        
class LoginUsuarioForm(FlaskForm):
    email = StringField (
        'E-mail:',
        validators=[DataRequired(), Email()]
    )
    senha = PasswordField (
        'Senha:',
        validators=[DataRequired()]
    )
    botao = SubmitField('Fazer Login')

class DeixeSeuRelatorioForm(FlaskForm):
    username = StringField(
        'Nome:',
        validators=[DataRequired(), Length(min=2, max=80)]
    )
   
    escrevaRelato = StringField(
        'Escreva seu relato:',
        validators=[DataRequired(), Length(min=2, max=3000)]
    )
    botao = SubmitField('Enviar')

