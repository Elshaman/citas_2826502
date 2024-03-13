from . import app, db
from .models import Medico, Paciente 
from flask import render_template, request

#crear ruta para ver los medicos 
@app.route("/medicos")
def get_all_medicos():
    medicos = Medico.query.all()
    return render_template("medicos.html" , medicos=medicos )

#crear ruta pacientes
@app.route("/pacientes")
def get_all_pacientes():
    pacientes = Paciente.query.all()
    return render_template("pacientes.html" , pacientes=pacientes )

#crear ruta traer el medico por id(get)
@app.route("/medicos/<int:id>")
def get_medico_by_id(id):
    medico = Medico.query.get(id)
    return render_template("medico.html", 
                            med = medico )

#crear ruta para crear nuevo medico
@app.route("/medicos/create" , methods = [ 'GET' , 'POST'] )
def create_medico():
    #######
    ####  mostrar el formulario: metodo GET
    #######
    if( request.method == 'GET' ):
        #el usuario ingreso con navegador con http://localhost:5000/medicos/create
        especialidades = [
            "Cardiologia", 
            "Pediatria", 
            "Oncologia"
        ]
        return render_template("medico_form.html", 
                                especialidades = especialidades )
  
    #####
    ## Cuando el usuario presiona el boton guardar
    ## los datos del formulario viajan al servidor
    ## utilizando el metodo POST

    elif(request.method == 'POST'):
        #cuando se presiona 'guardar'
        #crear un objeto de tipo medico
        new_medico = Medico(nombre = request.form["nombre"],  
                            apellidos = request.form["apellidos"],
                            tipo_identificacion = request.form["ti"],
                            numero_identificacion = request.form["ni"], 
                            registro_medico = request.form["rm"], 
                            especialidad = request.form["es"]
                            )
        #añadirlo a la sesion sqlalchemy
        db.session.add(new_medico)
        db.session.commit()
        return "medico registrado" 


