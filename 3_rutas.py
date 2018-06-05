# -- imports
from flask import Flask
from flask import request

# -- my app
app = Flask(__name__)

# -- home
@app.route('/') # -- wrap
def index(): # -- def
    return 'Home' # -- return

# -- about
@app.route('/about') # -- wrap
def about(): # -- def
    return 'About Us' # -- return

# -- params
@app.route('/params') # -- wrap
def params(): # -- def
    name = request.args.get('name', 'No tiene param "name"')
    ap_paterno = request.args.get('ap_paterno', '')
    return 'El param es {} {}'.format(name, ap_paterno) # -- return

# -- exec (obj) server in port 5000
# app.run()

# -- exec (obj) server with debug & in specific port ...
# -- debug = TRUE -> modo developer, muestra cambios instante
# -- debug = FALSE -> modo production, no muestra cambios instante
if __name__ == '__main__':
    app.run(debug = True, port = 8000)
