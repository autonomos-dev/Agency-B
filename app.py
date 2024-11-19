from flask import Flask, request, jsonify, render_template
import main  # Asegúrate de que main.py esté en el mismo directorio

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Renderiza el formulario HTML

@app.route('/submit', methods=['POST'])
def submit():
    brand_task = request.json.get('brand_task')  # Obtiene el parámetro 'brand_task' del cuerpo de la solicitud
    user_task = request.json.get('user_task')    # Obtiene el parámetro 'user_task' del cuerpo de la solicitud
    
    if not brand_task or not user_task:  # Verifica que ambos parámetros estén presentes
        return jsonify({"status": "error", "message": "Faltan parámetros"}), 400  # Devuelve un error si faltan parámetros
    
    result = main.run_logic(brand_task, user_task)  # Llama a la función que ejecuta tu lógica
    return jsonify(result)  # Devuelve el resultado como respuesta en formato JSON

if __name__ == '__main__':
    app.run(debug=True)  # Ejecuta la aplicación en modo de depuración