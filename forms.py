from flask_wtf import Flaskform


class CadastroUsuarioForm(Flaskform)
    username = StringField(
        'Usuário',
        validators=[DataRequerired(), Length(min=2, max=80)]
    )
    email = StringField (
        'Email'
        validators[DataRequerired()]
    )
    repita_senha = PassawordField (
        'Repita a Senha'
        validators[DataRequerired(), EqualTo(senha)]
    )
    botao = SubmitField('Cadastrar')
        
