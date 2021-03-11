"""
Fernando Andres Chavez Gavaldon
Busqueda en profundidad
"""

vuelos = [] # 0: (0: desde, 1: hacia, 2: distancia), 1: visitado
stack = []

#Vector donde se guardan los vuelos que hay
#El 0 es por si ya se visito el lugar,
#Tamaño del vector de []
def add_fly(desde, hacia, d):
	vuelos.append( [(desde, hacia, d), 0])

#Saber si hay vuelos
def fly(desde="los angeles", hacia="mexico"):
	d = ruta(desde, hacia)
	if d is not None:
		stack.append(d)
		return

	d = buscar(desde)
	if d is not None:
		stack.append(d)
		fly(d[1], hacia)
	else:
		if stack:
			d = stack[-1]
			stack.pop()
			fly(d[0], hacia)

def ruta(desde="los angeles", hacia="mexico"):
	for vuelo in vuelos:
		if vuelo[0][0] == desde and vuelo[0][1] == hacia:
			return vuelo[0]
	return None

def buscar(desde="los angeles"):
	for vuelo in vuelos:
		if vuelo[0][0] == desde and vuelo[1] == 0:
			vuelo[1] = 1
			return vuelo[0]
	return None


"""Inicio del Main"""


#Declaracion de los vuelos
add_fly("Los Angeles".lower(),	"Mexico".lower(),	3000)
add_fly("Chicago".lower(),		"Denver".lower(),	1000)
add_fly("Nueva York".lower(),	"Chicago".lower(),	1000)
add_fly("Nueva York".lower(),	"Denver".lower(),	1900)
add_fly("Nueva York".lower(),	"Toronto".lower(),	800)
add_fly("Toronto".lower(),		"Calgary".lower(),	1500)
add_fly("Toronto".lower(),		"Los Angeles".lower(),	1800)
add_fly("Toronto".lower(),		"Chicago".lower(),	500)
add_fly("Denver".lower(),		"Urbana".lower(),	1000)
add_fly("Denver".lower(),		"Houston".lower(),	1500)
add_fly("Houston".lower(),		"Los Angeles".lower(),	1500)
add_fly("Denver".lower(),		"Los Angeles".lower(),	1000)

print(len(vuelos))

print("Ingrese los nombres de las ciudades que se te pide")
desde = None
hacia = None

while True:
	desde = str(input('Desde: ')).lower()
	hacia = str(input('Hacia: ')).lower()
	if not(0 == len(desde)) and not(0==len(hacia)):
		break
	print("No se ingreso la ciudad Desde o la ciudad de destino(\"Hacia\")")


fly(desde, hacia)
distance = 0
for vuelo in stack:
	print('"{}" hacia'.format(vuelo[0]), end=' ')
	distance += vuelo[2]
if not stack:
   	print("No hay forma de llegar, no hay vuelos en {} o no se puede llegar hasta {}".format(desde,hacia))
else:
	print('"{}"'.format(hacia))
	print('La distancia es {} millas'.format(distance))