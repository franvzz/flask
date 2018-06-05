#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- import
import forms, json
# -- threading (ejecutar en segundo plano)
import threading
# -- flask imports
from flask import (
    Flask,
    render_template,
    request,
    make_response,
    session,
    redirect,
    url_for,
    flash, #-- notifies
    g, # -- para variables globales, la variable dura lo que dura el request
    copy_current_request_context, # -- para ejecutar en segundo plano
)
# -- para emails
# from flask_mail import Mail, Message
# -- CSRFProtect
from flask_wtf import CSRFProtect
# -- config DevelopmentConfig
from config import DevelopmentConfig
# -- models
from models import (
    db,
    User
)

# -- app
app = Flask(
    __name__,
    # template_folder = 'templates' # -- se puede omitir si se llama "templates"
)
# -- secret key (CsrfProtect)
# app.secret_key = SECRETE_KEY
# csrf = CsrfProtect(app)
# -- app config
app.config.from_object(DevelopmentConfig)
csrf = CSRFProtect()

# -- instanciar Mail
# mail = Mail()
# def send_email(user_email, username):
    # -- enviar correo
    # msg = Message(
          # -- subject
    #     'Gracias por registrarse',
          # -- to
    #     sender = app.config['MAIL_USERNAME'],
          # -- recipients
    #     recipients = [
    #         user_email # -- user que se acaba de registrar
    #     ]
    # )
    # -- msg en html
    # msg.html = render_template(
    #     'email/register.html',
    #     username = username
    # )
    # -- enviar msg
    # mail.send(msg)


# -- error 404 (page not found)
@app.errorhandler(404)
# @app.errorhandler(401) # -- other error
# @app.errorhandler(401) # -- other error
# @app.errorhandler(500) # -- other error
def page_not_found(e):
    return render_template('page/404.html'), 404 # -- poner error para retornar a cliente

# -- before request "hook" (se ejecuta antes del request)
@app.before_request
def before_request():
    g.test = 'before_request here...'
    # -- si user not in session
    if 'username' not in session and request.endpoint in ['comment']:
        return redirect(url_for('login')) # -- nombre de la funcion "def" a la cual redirigimos
    elif 'username' in session and request.endpoint in ['login', 'user_register']:
        return redirect(url_for('index')) # -- nombre de la funcion "def" a la cual redirigimos

# -- after_request "hook" (se ejecuta despues del request)
@app.after_request
def after_request(response):
    # print(response)
    print(g.test)
    return response # -- siempre retornar response

# -- home
@app.route('/')
@app.route('/home/<name>/')
def index(name='Sr. Javi Vazz'):
    print(g.test)
    return render_template('page/home.html',
        name=name,
    )

# -- user
@app.route('/user/')
@app.route('/user/<name>')
def user(name='Javi'):
    age = 37
    tupla = [ 1,2,3,4 ]
    return render_template('page/user.html',
        name=name,
        age=age,
        tupla=tupla
    )

# -- client
@app.route('/clients/')
def clients():
    name = 'Sr. Javi Vazz'
    clients_list = [ 'Hospital San Pedro', 'Plaza La Silla', 'Grante Inmobiliaria' ]
    return render_template('page/clients.html',
        name=name,
        clients_list=clients_list
    )

# -- comments
@app.route('/comments/', methods = [ 'GET', 'POST' ])
def comments():
    name = 'Sr. Javi Vazz'
    comment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else:
        print('Error en formulario')

    return render_template('page/comments.html',
        name = name,
        form = comment_form
    )

# -- login
@app.route('/login/', methods = [ 'GET', 'POST' ])
def login():
    # -- login form
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        # -- values
        username = login_form.username.data
        password = login_form.password.data
        # -- get user
        user = User.query.filter_by(
            username=username
        ).first()
        # -- validate login user
        if user is not None and user.verify_password(password):
            success_message = 'Welcome {}!'.format(username)
            session['username'] = username
            return redirect(url_for('index'))
        else:
            error_message = 'Usuario o contraseña no válida!'
        # -- flash message
        flash(error_message)
    # -- return
    return render_template('page/login.html',
        form = login_form
    )


@app.route('/ajax-login', methods = [ 'POST' ])
def ajax_login():
    # print(request.form)
    username = request.form['username']
    # password = request.form['password']
    response = {
        'status' : 200,
        'username': username,
        'id': 1
    }
    return json.dumps(response)


@app.route('/logout/')
def logout():
    if 'username' in session:
        session.pop('username')
    return redirect(url_for('login')) # -- nombre de la funcion "def" a la cual redirigimos

@app.route('/user/register/', methods = ['GET', 'POST'])
def user_register():
    register_user_form = forms.RegisterUserForm(request.form)
    if request.method == 'POST' and register_user_form.validate():
        # -- obj a guardar
        user = User(
            # username = register_user_form.username.data,
            # email = register_user_form.email.data,
            # password = register_user_form.password.data,
            # -- mismo orden en db (model)
            register_user_form.username.data,
            register_user_form.email.data,
            register_user_form.password.data,
        )
        # -- connect db
        db.session.add(user)
        # -- save in db
        db.session.commit()

        # -- para poder ejecutar en segundo plano con flask
        # @copy_current_request_context
        # def send_message(email, username):
        #     send_email(email, username)

        # -- send email en segundo plano
        # sender = threading.Thread(
        #     name='mail_sender',
        #     target=send_email,
        #     args(
        #         user.email,
        #         user.username
        #     )
        # )
        # sender.start()

        # -- flash message
        success_message = "El usuario ha sido registrado."
        flash(success_message)
    # -- return
    return render_template(
        'user/register.html',
        form = register_user_form
    )

# -- Cookies
@app.route('/cookies/', methods = [ 'GET', 'POST' ])
def cookies():
    # myCookie = request.cookies.get('myCookie', 'Undefined') #-- si no se encuentra "myCookie" retorna "Undefined"
    response = make_response(
        render_template('page/cookies.html')
    )
    response.set_cookie('myCookie', 'mi valor de cookie')
    return response


# -- exec
if __name__ == '__main__':
    # -- csrf init config
    csrf.init_app(app)
    # -- mail init config
    # mail.init_app(app)
    # -- db init config
    db.init_app(app)
    # -- context ...
    with app.app_context():
        # -- create tables...
        db.create_all()
    # -- run app
    app.run(
        port=8000 # -- run app in port 8000
    )
