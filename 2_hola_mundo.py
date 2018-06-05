from flask import Flask

app = Flask(__name__) # -- new obj

@app.route('/') # -- wrap
def index(): # -- def
    return 'Hola mundo' # -- return

# -- exec (obj) server in port 5000
# app.run()

# -- exec (obj) server with debug & in specific port ...
# -- debug = TRUE -> modo developer, muestra cambios instante
# -- debug = FALSE -> modo production, no muestra cambios instante
if __name__ == '__main__':
    app.run(debug = True, port = 8000)
