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

def obtener_moneda():
    cantidad=float(request.form.get('cantidad'))
    valor_monedaOrigen=request.form.get("moneda_origen") #PEN
    valor_monedaDestino=request.form.get("moneda_destino")
    return cantidad, valor_monedaOrigen, valor_monedaDestino

def handleConvertir():
    cantidad, valor_monedaOrigen, valor_monedaDestino=obtener_moneda()
    moneda=getMoneda()["conversion_rates"]
    return  cantidad, moneda[valor_monedaOrigen], moneda[valor_monedaDestino]
  
def handleCalcular():
   cantidad, monedaOrigen, monedaDestino=handleConvertir()
   resultado = cantidad / monedaOrigen * monedaDestino
   return resultado

@app.route('/', methods=['GET', 'POST'])
def index():
    datos=getMoneda()
    rest=None
    cantidad_convertir=request.form.get('cantidad', "")

    if(request.method=='POST'):
       resultado=handleCalcular()
       rest=resultado
      
    return render_template('index.html',
                            data=datos,
                            result=f"{(round(rest, 2) if rest else ""):,}".replace(","," "),
                            moneda_origen=request.form.get("moneda_origen"),
                            moneda_destino=request.form.get("moneda_destino"),
                            cantidad=cantidad_convertir)

# Definir el PORT de escucha
if __name__ == '__main__':
    app.run()