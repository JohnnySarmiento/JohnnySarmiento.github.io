from flask import Flask, render_template, request
import sympy as sp

# Crear la aplicación Flask
app = Flask(__name__)

# Ruta principal para mostrar el formulario
@app.route('/')
def index():
    return render_template('index.html')  # Esto mostrará el formulario

# Ruta para procesar la función y calcular el área bajo la curva
@app.route('/calcular', methods=['POST'])
def calcular_area_bajo_la_curva():
    # Recibir los datos del formulario
    funcion = request.form['funcion']
    limite_inferior = float(request.form['limite_inferior'])
    limite_superior = float(request.form['limite_superior'])

    # Definir la variable simbólica y la función
    x = sp.Symbol('x')
    try:
        # Convertir la entrada del usuario a una función simbólica
        funcion_simbolica = sp.sympify(funcion)
        
        # Calcular la integral definida
        area = sp.integrate(funcion_simbolica, (x, limite_inferior, limite_superior))
        
        # Convertir a decimal y fracción
        area_decimal = float(area)  # Forma decimal
        area_fraccion = sp.nsimplify(area)  # Forma exacta como fracción

        # Enviar los resultados al HTML
        return render_template(
            'resultados.html', 
            funcion=funcion, 
            limite_inferior=limite_inferior, 
            limite_superior=limite_superior,
            area_fraccion=area_fraccion, 
            area_decimal=area_decimal
        )
    except Exception as e:
        # Si ocurre un error, mostrarlo al usuario
        return f"Error: {str(e)}. Verifique que la función y los límites sean válidos."

# Ejecutar la aplicación en el servidor
if __name__ == "__main__":
    app.run(debug=True)
