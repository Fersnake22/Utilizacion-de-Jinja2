from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)


@app.route('/')
def nueva_palabra():
   return render_template('diccionario.html')

@app.route('/significadoec',methods = ['POST', 'GET'])
def significadoec():
   if request.method == 'POST':
      try:
         palabra = request.form['palabra']
         significado = request.form['significado']
         
         with sql.connect("diccionario_slang.db") as con:
            cur = con.cursor()
            
            cur.execute("INSERT INTO diccionario (palabra,significado) VALUES (?,?)",(palabra,significado) )
            
            con.commit()
            msg = "Palabra agregada"
      except:
         con.rollback()
         msg = "Error"
      
      finally:
         return render_template("resultado.html", msg = msg)
         con.close()

# Para observar las palabra ingresadas
@app.route('/lista')
def lista():
   con = sql.connect("diccionario_slang.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from diccionario")
   
   rows = cur.fetchall();
   return render_template("lista.html",rows = rows)

if __name__ == '__main__':
   app.run(debug = True)