# TP 6 - Estructuras de Datos Complejas
# Programación 1 - Tecnicatura Universitaria en Programación a Distancia
# Autor: Natanael Funes
# Descripción: Resolución de ejercicios sobre estructuras de datos complejas sin uso de objetos.

# 1) Crear el diccionario inicial y agregar nuevas frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

# 2) Actualizar precios de algunas frutas
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

# 3) Crear una lista con solo los nombres de las frutas
lista_frutas = list(precios_frutas.keys())
print("Lista de frutas:", lista_frutas)

# 4) Agenda telefónica simple
agenda = {}
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i+1}: ")
    telefono = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = telefono
consulta = input("Consultá un nombre para ver su teléfono: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Ese contacto no está registrado.")

# 5) Contador de palabras y palabras únicas
frase = input("Ingresá una frase: ").lower()
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)
conteo_palabras = {}
for palabra in palabras:
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1
print("Frecuencia de palabras:", conteo_palabras)

# 6) Promedios de 3 alumnos
notas_alumnos = {}
for i in range(3):
    nombre = input(f"Nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Nota {j+1} de {nombre}: ")) for j in range(3))
    notas_alumnos[nombre] = notas
for alumno, notas in notas_alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"Promedio de {alumno}: {promedio:.2f}")

# 7) Operaciones con sets de estudiantes
parcial1 = set(input("Aprobados Parcial 1 (separados por coma): ").split(","))
parcial2 = set(input("Aprobados Parcial 2 (separados por coma): ").split(","))
print("Aprobaron ambos:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)

# 8) Stock de productos
stock = {}
producto = input("Producto a consultar/agregar: ")
if producto in stock:
    cantidad = int(input("Cantidad a agregar: "))
    stock[producto] += cantidad
else:
    cantidad = int(input("Producto nuevo. Ingresá cantidad: "))
    stock[producto] = cantidad
print("Stock actual:", stock)

# 9) Agenda de actividades por día y hora
agenda_eventos = {
    ('Lunes', '10:00'): 'Reunión de equipo',
    ('Martes', '14:00'): 'Clase de Python'
}
dia = input("Ingresá día: ")
hora = input("Ingresá hora: ")
evento = agenda_eventos.get((dia, hora), "No hay actividad registrada.")
print(f"Actividad en {dia} a las {hora}: {evento}")

# 10) Invertir diccionario de capitales
paises_capitales = {
    'Argentina': 'Buenos Aires',
    'Brasil': 'Brasilia',
    'Chile': 'Santiago'
}
capitales_paises = {capital: pais for pais, capital in paises_capitales.items()}
print("Capitales como claves:", capitales_paises)
