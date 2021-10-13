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

@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['usulog']
        contrauser = request.form['contralog']
        for usuario in baselogin:
            if usuario["user"]==user and usuario["password"]==contrauser:
                return redirect(url_for("user",usr=user))
                break            
        return render_template("registro.html")
    
        
@app.route("/<usr>")
def user(usr):
    return f"<h1{usr}</h1"    
    

@app.route("/ingresardatos", methods=['POST','GET'])
def ingresardatos():
    nombre = request.form['usulog']
    apellido = request.form['contralog']
    cedula = request.form['contralog']
    correo = request.form['contralog']
    telefono = request.form['contralog']
    password = request.form['contralog']
        
    #insert into usuario values (nombre,apellido,cedula,correo,telefono,passoword)
    
    
    

@app.route('/registro',methods=['GET','POST'])
def registro():
    if request.method=='POST':
        # Handle POST Request here
        return render_template('registro.html')
        return render_template('statics/css/style.css')
    return render_template('registro.html')
    return render_template('statics/css/style.css')

@app.route("/dashboardadmin",methods=['GET','POST'])
def dashboardadmin():
    if request.method=='POST':
        return render_template('admin.html')
    return render_template('admin.html')

@app.route('/listadolistas',methods=['GET','POST'])
def listado_listas():
    if request.method=='POST':
        return render_template('listadolistas.html')
    return render_template('listadolistas.html')

@app.route('/detallecita',methods=['GET','POST'])
def detalle_cita():
    if request.method=='POST':
        return render_template('detalle_cita.html')
    return render_template('detalle_cita.html')

@app.route('/resultadobus',methods=['GET','POST'])
def reultado_busquedas():
    if request.method=='POST':
        return render_template('resultadobus.html')
    return render_template('resultadobus.html')

@app.route('/perfiluser',methods=['GET','POST'])
def perfil_user():
    if request.method=='POST':
        return render_template('perfil_user.html')
    return render_template('perfil_user.html')


if __name__ == '__main__':
    #DEBUG is SET to TRUE. CHANGE FOR PROD
    app.run(port=5000,debug=True)