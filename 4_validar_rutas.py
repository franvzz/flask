# -- imports
from flask import Flask
from flask import request

# -- my app
app = Flask(__name__)

# -- home
@app.route('/') # -- route
def index(): # -- def
    return 'Home' # -- return

# -- about
@app.route('/about') # -- route
def about(): # -- def
    return 'About Us' # -- return

# -- params
@app.route('/params') # -- route
def params(): # -- def
    name = request.args.get('name', 'Mi valor por default para "name"')
    lastname = request.args.get('lastname', '')
    return 'El param es {} {}'.format(name, lastname) # -- return

# -- slug
@app.route('/slug/') # -- route without param
@app.route('/slug/<int:id>/') # -- route without param
@app.route('/slug/<name>/') # -- route with param
@app.route('/slug/<name>/<lastname>') # -- route with param
def slug(id='', name='', lastname=''): # -- def
    return 'El param es {} {} {}'.format(id, name, lastname) # -- return


# -- exec (obj) server in port 5000
# app.run()

# -- exec (obj) server with debug & in specific port ...
# -- debug = TRUE -> modo developer, muestra cambios instante
# -- debug = FALSE -> modo production, no muestra cambios instante
if __name__ == '__main__':
    app.run(debug = True, port = 8000)
