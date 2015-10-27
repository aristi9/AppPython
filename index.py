#!C:\Python27\python.exe
# -*- coding: UTF-8 -*-

print "Content-Type: text/html"
print
print """ <html>
		<head>
			<meta charset= "UTF-8"/>
			<title>Ejemplo Python</title>
		</head>
		<body>
			<div>
				<h1>Ejemplo Python</h1>
			</div>
			<hr>
			<div>
				<form action="seleccionar.py">
					<input type = 'submit' value='Seleccionar producto'></form>
				<form action="modificar.py">
					<input type =  'submit' value='Modificar producto'></form>
				<form action="insertar.py">
					<input type = 'submit' value='Insertar producto'></form>
			</div>
		</body>
		</html>
	"""