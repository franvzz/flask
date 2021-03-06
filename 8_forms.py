#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- import
from flask import (
    Flask,
    render_template,
    request,
    make_response,
    session,
    redirect,
    url_for,
    flash #-- notifies
)
from flask_wtf import CsrfProtect

import forms, json

# -- app
app = Flask(
    __name__,
    # template_folder = 'templates' # -- se puede omitir si se llama "templates"
)
# -- secret key (CsrfProtect)
app.secret_key = 'my_secret_key'
csrf = CsrfProtect(app)

# -- error 404 (page not found)
@app.errorhandler(404)
# @app.errorhandler(401) # -- other error
# @app.errorhandler(401) # -- other error
# @app.errorhandler(500) # -- other error
def page_not_found(e):
    return render_template('page/404.html'), 404 # -- poner error para retornar a cliente

# -- home
@app.route('/')
@app.route('/home/<name>/')
def index(name='Sr. Javi Vazz'):
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
    # -- read session
    if 'username' in session:
        username = session['username']
        print(username)
    # -- login form
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        session['username'] = username
        success_message = 'Welcome {}!'.format(username)
        flash(success_message)
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
    app.run(debug=True, port=8000)
