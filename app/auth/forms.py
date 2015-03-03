from wtforms import StringField, PasswordField, BooleanField, SubmitField,\
                    ValidationError
from wtforms.validators import Required, Email
from flask.ext.wtf import Form
from ..models import User

class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Contraseña', validators=[Required()])
    remember_me = BooleanField('Mantenerme conectado', default=True)
    submit = SubmitField('Ingresar')

class RegistrationForm(Form):
    name = StringField('Nombre', validators=[Required()])
    email = StringField('Email', validators=[Required(), Email()])
    password = PasswordField('Contraseña', validators=[Required()])
    submit = SubmitField('Registrarme')

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email ya registrado') 
