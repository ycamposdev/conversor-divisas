import requests
from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)
API_Exchange="https://v6.exchangerate-api.com/v6/b173cea5e2936d72157593c8/latest/USD"

def getMoneda():
    try:
      response = requests.get(API_Exchange)
      return response.json()
    except:
     return None

def handleConvertir():
   cantidad=float(request.form.get('cantidad'))
   monedaOrigen=request.form.get("moneda_origen") #PEN
   monedaDestino=request.form.get("moneda_destino")
   resultado = cantidad / getMoneda()["conversion_rates"][monedaOrigen] * getMoneda()["conversion_rates"][monedaDestino]
   return resultado

@app.route('/', methods=['GET', 'POST'])
def index():
    datos=getMoneda()
    rest=None
    cantidad_enviada=request.form.get('cantidad', "")

    if(request.method=='POST'):
       resultado=handleConvertir()
       rest=resultado

    return render_template('index.html',
                            data=datos,
                            result=(round(rest, 2) if rest else ""),
                            moneda_origen=request.form.get("moneda_origen"),
                            moneda_destino=request.form.get("moneda_destino"),
                            cantidad=cantidad_enviada)

# Definir el PORT de escucha
if __name__ == '__main__':
    app.run(debug=True, port=5000)