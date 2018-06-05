#!/usr/bin/env python
# -*- coding: utf-8 -*-

# -- import
from flask import Flask
from flask import render_template

# -- app
app = Flask(
    __name__,
    template_folder = 'templates' # -- se puede omitir si se llama "templates"
)

# -- home
@app.route('/')
@app.route('/<name>/')
def index(name='Sr. Javi Vazz'):
    return render_template('page/home.html', name=name)

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

# -- exec
if __name__ == '__main__':
    app.run(debug=True, port=8000)
