from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({"mensaje": "Microservicio corriendo", "version": "1.0"})

@app.route('/salud')
def salud():
    return jsonify({"estado": "OK"})

@app.route('/saludo/<nombre>')
def saludo(nombre):
    return jsonify({"mensaje": f"Hola, {nombre}! Bienvenido al microservicio."})

@app.route('/version')
def version():
    return jsonify({"version": "1.0.0", "autor": "trini13", "descripcion": "Microservicio de prueba DevOps"})

@app.errorhandler(404)
def no_encontrado(error):
    return jsonify({"error": "Ruta no encontrada", "codigo": 404}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)