from wtforms import Form
from wtforms import StringField, TextField, HiddenField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import validators

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('Honeypot debe estar vacío.')

class CommentForm(Form):
    username = StringField(
        'Username',
        [
            validators.Required(message='Username is require'),
            validators.length(min=2, max=25, message='Username is not valid!')
        ]
    )
    email = EmailField(
        'Correo',
        [
            validators.Required(message='Email is require'),
            validators.Email(message='Email is not valid'),
        ]
    )
    comment = TextField(
        'Comment',
        [
            validators.Required(message='Comment is require'),
        ]
    )
    honeypot = HiddenField(
        '',
        [
            length_honeypot
        ]
    )


class LoginForm(Form):
    username = StringField('username',
        [
            validators.Required(message='El username es requerido')
        ]
    )
    password = PasswordField('password',
        [
            validators.Required(message='El password es requerido')
        ]
    )

class RegisterUserForm(Form):
    username = TextField('Username', [
        validators.Required(message = 'El username es requerido')
    ])
    email = EmailField('Email', [
        validators.Required(message = 'El email es requerido'),
        validators.Email(message = 'El email no es válido')
    ])
    password = PasswordField('Password', [
        validators.Required(message = 'El password es requerido')
    ])
