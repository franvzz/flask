from flask import Flask

app = Flask(__name__) # -- new obj

@app.route('/') # -- wrap
def index(): # -- def
    return 'Hola mundo' # -- return

# -- exec (obj) server in port 5000
app.run()
