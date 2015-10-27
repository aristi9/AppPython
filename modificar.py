#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
import MySQLdb
import sys
#Importamos modulos para el manejo del CGI
import cgi, cgitb

print "Content-Type: text/html"
print
print """      <html>
			<head>
			</head>
			<body>
                    <h1>Modifique el precio del producto</h1>
                    <hr>
                    <form action="/cgi-bin/AppPython/modificar.py" method='post'>
                         <p>Inserte el nombre del producto que quiera modificar</p>
                         <input type='text' name='nombre' required>
                         <p>Inserte el nuevo precio</P>
                         <input type='number' name='precio' required><br><br>
                         <input type ='submit' value='Modificar Producto'>
                    </form>
                    <button type='button' onclick="location.href='index.py'">Inicio</button>
               </body>
               </html>
"""
# Creamos una instancia del FieldStorage
valor = cgi.FieldStorage()
# Recogemos los datos de los campos
nombreProducto = valor.getvalue("nombre")
precioProducto = valor.getvalue("precio")
con = MySQLdb.connect(host='localhost', user='root', passwd='conexion', db='productos')

cur = con.cursor()
sql = "UPDATE producto SET precio = %i WHERE nombre= '%s'" % (int(precioProducto),nombreProducto)
cur.execute(sql)
con.commit()

con.close()