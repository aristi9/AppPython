#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-
import MySQLdb
import sys

 #Ejecutamos la consulta

print "Content-Type: text/html"
print
print """ <html>
			    <head>
			    </head>
			    <body>
            <h1>Lista de productos</h1>
            <hr>
            <table>
              <tr>
              <td>id</td>
              <td>nombre</td>
              <td>precio</td>
              </tr>
      """
con = MySQLdb.connect(host='localhost', user='root', passwd='conexion', db='productos')
cur = con.cursor()
sql = 'SELECT * FROM producto;'
cur.execute(sql)
con.commit()
numrows = int(cur.rowcount)
#recorremos la lista de productos y la visualizamos en la tabla
for x in range(0,numrows):
  row = cur.fetchone()
  print """<tr>
  """
  print """
  		<td>""", row[0], """</td>
      <td>""", row[1], """</td>
      <td>""", row[2], """</td>
      """
  print """</tr>"""
con.close()
print """
      </table><br><br>
      <button type='button' onclick="location.href='index.py'">Inicio</button>
			</body>
		</html>
	"""