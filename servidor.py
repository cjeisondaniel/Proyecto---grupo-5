from sqlite3.dbapi2 import Error
from flask import *  
import sqlite3  
  


from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

baselogin= [
    {"user":"useruno",
     "password":"useruno",
    },
    {"user":"userdos",
     "password":"userdos"},
    {"user":"usertres",
     "password":"usertres"}
    ]

@app.route('/')
def home1():
    return render_template("index.html")

#Al iniciar el servidor reenvia a la página inicial de index

@app.route('/usuario',methods=['POST','GET'])
def usua():
     if request.method=='GET':
        try:
            with sqlite3.connect("CentroMedico.db") as con:
                Usuario = 1234
                con.row_factory=sqlite3.Row #Hacer diccionario de lo que busco en la BD
                cur = con.cursor()
                consulta=cur.execute("SELECT rol from Usuario where Cedula=?",[Usuario]).fetchone()
                Rol=consulta[0]
                
                if Rol=="Paciente":             
                    consulta2=cur.execute("Select Nombre, Apellido, Correo from Paciente Where cedula=?",[Usuario]).fetchone()
                    Nombre=consulta2[0]
                    Apellido=consulta2[1]
                    Correo=consulta2[2]
                    if consulta2 != None:
                        return render_template("usuario.html",nombre=Nombre,apellidos=Apellido,correoelctronico=Correo,perfil=Rol)
                
                elif Rol=="Medico":
                    consulta2=cur.execute("Select Nombre, Apellido, Correo from Medico Where cedula=?",[Usuario]).fetchone()
                    Nombre=consulta2[0]
                    Apellido=consulta2[1]
                    Correo=consulta2[2]                                
                    if consulta2 != None:
                        return render_template("usuario.html",nombre=Nombre,apellidos=Apellido,correoelctronico=Correo,perfil=Rol)

        except Error: 
            return render_template("usuario.html")
            
            

@app.route('/login',methods=['POST','GET'])
def login():         
    return render_template("registro.html")
#busca los datos de usuario y contraseña encontrados en la base de datos y los reenvía a la página de usuario o a la página de login en el caso que no los encuentre   
          
    
@app.route("/ingresardatos", methods=['POST','GET'])
def ingresardatos():
    nombre = request.form['usulog']
    apellido = request.form['contralog']
    cedula = request.form['contralog']
    correo = request.form['contralog']
    telefono = request.form['contralog']
    password = request.form['contralog']
            
""" with sqlite3.connect("employee.db") as con:  
                cur = con.cursor()  
                cur.execute("INSERT into usuario (nombre, apellido, cedula,correo,telefono,password) values (?,?,?)",(nombre,apellido,cedula,correo,telefono,password))  
                con.commit()  
                msg = "Employee successfully Added"  
        except:  
            con.rollback()  
            msg = "We can not add the employee to the list"  
            return render_template("interfazusuario.html")
        finally:  
            return render_template(# usuario ingresado con éxito" "success.html",msg = msg)  
            con.close()  
"""
#Ingresa los datos ingresados en el login a la tabla de la base de datos con el nombre de usuario    
    


@app.route("/dashboardadmin",methods=['GET','POST'])
def dashboardadmin():
    if request.method=='POST':
         con = sqlite3.connect("employee.db")  
         con.row_factory = sqlite3.Row  
         cur = con.cursor()  
         cur.execute("select * from usuario")  
         rows = cur.fetchall()  
         return render_template("admin.html",rows = rows)
    else:
        msg = "No se han encontrado ningún dato" 
        
#Toma los datos del medico o paciente y los coloca en la interfaz de admin




@app.route('/listadolistas',methods=['GET','POST'])
def listado_listas():
    if request.method=='POST':
        usuario = request.form['usuarios']
        con = sqlite3.connect("employee.db")  
        con.row_factory = sqlite3.Row  
        cur = con.cursor()  
        cur.execute("select nombre, fechacita, hora  from lista natural join usuario where usulog = nombre")  
        rows = cur.fetchall()  
        return render_template("listadodecitas.html",rows = rows)
    else:
        msg = "No hay ningúna cita pendiente" 
 



@app.route('/detallecitamedico',methods=['GET','POST'])
def detalle_cita():
    if request.method=='POST':
        nombre = request.form['usulog']
        con = sqlite3.connect("employee.db")  
        con.row_factory = sqlite3.Row  
        cur = con.cursor()  
        cur.execute("select nombre, especialidad, turno  from citapaciente natural join usuario where usulog = nombre")  
        rows = cur.fetchall()  
        return render_template("Detalle_citamedico.html",rows = rows)
    else:
        msg = "No se han encontrado citas establecidas" 
#Se toma de la tabla citapaciente los campos de nombre especialdiad y turno y se los manda a la pagina de detalle decita medico

@app.route('/detallecitapaciente',methods=['GET','POST'])
def detalle_cita_paciente():
    if request.method=='POST':
        nombre = request.form['usulog']
        con = sqlite3.connect("employee.db")  
        con.row_factory = sqlite3.Row  
        cur = con.cursor()  
        cur.execute("select nombre, especialidad, turno, resumen  from paciente natural join usuario where usulog = nombre")  
        rows = cur.fetchall()  
        return render_template("Detallescitapaciente.html",rows = rows)
    else:
        msg = "No se han encontrado el usuario " 

#Se toma de la tabla paciente los campos de nombre especialdiad y turno y se los manda a la pagina de detalle decita medico



@app.route('/asignarcita',methods=['GET','POST'])
def detalle_cita_asiganar():
    if request.method=='POST':
        nombre = request.form['usulog']
        con = sqlite3.connect("employee.db")  
        con.row_factory = sqlite3.Row  
        cur = con.cursor()  
        cur.execute("select especialidad, paciente from asignarcita where user=nombre")  
        rows = cur.fetchall()  
        return render_template("Detalle_cita2_medico.html",rows = rows)
    else:
        msg = "No se han encontrado el usuario " 
#Se toma de la tabla de asignar cita los campos de especialdiad y nombre paciente y se los manda a la pagina de asignarcitamedico





@app.route("/perfilusuario")  
def view():  
    con = sqlite3.connect("employee.db")  
    con.row_factory = sqlite3.Row  
    cur = con.cursor()  
    cur.execute("select * from usuario")  
    rows = cur.fetchall()  
    return render_template("usuario.html",rows = rows)

#Busca los datos que se encuentran en la tabla usuario y los envía a la página usuario.


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)