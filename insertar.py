#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
import MySQLdb
import sys

#Importamos modulos para el manejo del CGI
import cgi, cgitb

print "Content-Type: text/html"
print
print """ <html>
		      <head>
		      </head>
	        <body>
               <h1>Inserte el nuevo producto</h1>
               <hr>
               <form action="/cgi-bin/AppPython/insertar.py" method="get">
                <p>Inserte la marca del producto</p>
                <input type="text" name="nombre" required>
                <p>Inserte el precio del producto</P>
                <input type="number" name="precio" required><br><br>
                <input type ="submit" value="Insertar Producto">
               </form>
               <button type="button" onclick="location.href='index.py'">Inicio</button>
          </body>
          </html>
          """

# Creamos una instancia del FieldStorage
valor = cgi.FieldStorage()
# Recogemos los datos de los campos
nombreProducto = valor.getvalue('nombre')
precioProducto = valor.getvalue('precio')

con = MySQLdb.connect(host='localhost', user='root', passwd='conexion', db='productos')
cur = con.cursor()
if nombreProducto is not None and precioProducto is not None:
     sql = "INSERT into producto(nombre,precio) VALUES ('%s',%i)" % (nombreProducto, int(precioProducto))
     cur.execute(sql)
     con.commit()

con.close()