from flask import Flask

app = Flask(__name__)

@app.route('/')
def hola_mundo():
    return '<h1>Bienvenido Flask</h1><p>El servidor esta en ejecución.</p>'

@app.route("/categorias")
def categoria():
    return "<h1>Estas son las categorias</h1>"

# Definir el PORT de escucha
if __name__ == '__main__':
   
    app.run(debug=True, port=5000)