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
def index():
    return render_template('page/home.html')

# -- user
@app.route('/user/')
@app.route('/user/<name>')
def user(name='Javi'):
    age = 37
    tupla = [ 1,2,3,4 ]
    return render_template('page/user.html', name=name, age=age, tupla=tupla)

# -- exec
if __name__ == '__main__':
    app.run(debug=True, port=8000)
