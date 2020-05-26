#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: Allan F Souza
import hashlib
from flask import Flask,request,jsonify,redirect,render_template,flash
app = Flask(__name__,template_folder='view')
ADMIN_SA = "123"

def hashMd5(codeStr):
  h = hashlib.md5()
  h.update(str(codeStr).encode('utf-8'))
  return h.hexdigest()


@app.route('/login/<hashAdmin>', methods=["GET","POST"])
def login(hashAdmin):
 nome =  None
 senha = None
 trava = False
 error = ' '
  
 if hashAdmin ==  hashMd5(ADMIN_SA):
  try:
   if request.method == 'POST':
    senha =  request.form['senha']
    email =  request.form['email']
    print("Email:",email)
    print("Senha:",senha)
    
    if hashMd5(senha) == hashMd5(ADMIN_SA ):
      trava = True  
      error = "Credenciais Valida"
      print("SENHA",hashMd5(senha))
      print("HASH",hashMd5(ADMIN_SA))
      return redirect("/index/"+ hashMd5(ADMIN_SA))
      
    else:
      trava = False 
      error = "Credenciais Invalida"
      
   return render_template('login.html', titulo='Login do Administrador',erro=error,trava=trava)
      

  except Exception as err:
     IOerro = "Erro de login! Tente novamente mais tarde"+str(err)
     return render_template('index.html',titulo='Login do Administrador',erro = "Insira suas Credenciais",hashOne=hashAdmin )
     




@app.route('/', methods=["GET","POST"])
def index_default():
 admin = None
 senha = None
 try: 
  if request.method == 'POST':
     admin =  request.form['admin']
     senha =  request.form['senha']
     
     if admin == "admin" and hashMd5(senha) == hashMd5(ADMIN_SA):
       return redirect("/login/"+hashMd5(senha))
       
  return render_template('admin.html',title="Permissão",admin="admin")

 except Exception as err:
    return render_template('admin.html',title="Permissão",admin="admin")
    

  
  
  

@app.route('/index/<hashon>')
def index(hashon):
 if hashon == hashMd5(ADMIN_SA):
  return render_template('showIndex.html',hashOne=hashon)




@app.route('/info/<hashAdmin>')
def info_proteus(hashAdmin):
  return render_template('info.html',hashOne=hashAdmin)
    


@app.route('/forms/<hashAdmin>')
def forms(hashAdmin):
  return render_template('forms.html',hashOne=hashAdmin)
    




#Operação de soma Operador * operando = obs não tem um exemplo
@app.route('/vs1/soma')
def soma():
    a =0
    b = 0
    if request.method == 'GET':
        a = int(request.args["a"])
        b = int(request.args["b"])
    return redirect("http://localhost:5000/info/{0}".format(a*b), code=302)
    

@app.route('/info/<obj>')
def info(obj):
    return jsonify({"c":obj})


    
@app.route('/vs1/post', methods=['POST', 'GET'])   
def post():
    nome =  None
    senha = None
    if request.method == 'POST':
        senha =  int(request.form['senha'])
        nome  =  request.form['nome']
        print("NOME:",nome)
        print("Senha:",senha)
        if senha == 123456:
           print("Senha correta")
        else:
           print ("senha invalida " )  
        
    return jsonify({"Nome":nome})
    
       

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port,debug=True)
  
  
