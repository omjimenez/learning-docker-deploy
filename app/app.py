from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "¡Hola, Estamos trabajando en el cotizador y pagina web Taller El Kairos..!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

