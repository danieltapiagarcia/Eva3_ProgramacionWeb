from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET','POST'])
def ejercicio1():
    if request.method == 'POST':
        nota1 = float(request.form['nota1'])
        nota2 = float(request.form['nota2'])
        nota3 = float(request.form['nota3'])
        asistencia = float(request.form['asistencia'])

        promedio = (nota1 + nota2 + nota3) / 3

        if promedio >= 40 and asistencia >= 75:
            estado ="Aprobado"
        else:
            estado ="Reprobado"

        print("Formulario enviado")
        return render_template('ejercicio1.html', promedio = promedio, estado=estado)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':

        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        cantidad1 = len(nombre1)
        cantidad2 = len(nombre2)
        cantidad3 = len(nombre3)

        if cantidad1 >= cantidad2 and cantidad1 >= cantidad3:
            nombre_largo = nombre1
            cantidad_caracteres = cantidad1

        elif cantidad2 >= cantidad1 and cantidad2 >= cantidad3:
            nombre_largo = nombre2
            cantidad_caracteres = cantidad2

        else:
            nombre_largo = nombre3
            cantidad_caracteres = cantidad3

        return render_template('ejercicio2.html', nombre_largo=nombre_largo,
            cantidad_caracteres=cantidad_caracteres
        )



    return render_template('ejercicio2.html')


if __name__ == '__main__':
    app.run(debug=True)