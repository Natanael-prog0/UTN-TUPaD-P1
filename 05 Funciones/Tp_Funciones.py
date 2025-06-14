import math

# Ejercicio 1
def imprimir_hola_mundo():
    print("Hola Mundo!")

# Ejercicio 2
def saludar_usuario(nombre):
    return f"Hola {nombre}!"

# Ejercicio 3
def informacion_personal(nombre, apellido, edad, residencia):
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}")

# Ejercicio 4
def calcular_area_circulo(radio):
    return math.pi * radio ** 2

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

# Ejercicio 5
def segundos_a_horas(segundos):
    return segundos / 3600

# Ejercicio 6
def tabla_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}:")
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i} = {resultado}")

# Ejercicio 7
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b if b != 0 else "Error: División por cero"
    return (suma, resta, multiplicacion, division)

# Ejercicio 8
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Ejercicio 9
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Ejercicio 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

# PROGRAMA PRINCIPAL
if __name__ == "__main__":
    print("PRÁCTICO 2: FUNCIONES EN PYTHON")
    print("=" * 40)
    
    # Ejercicio 1
    print("\n--- Ejercicio 1 ---")
    imprimir_hola_mundo()
    
    # Ejercicio 2
    print("\n--- Ejercicio 2 ---")
    nombre_usuario = input("Ingresa tu nombre: ")
    saludo = saludar_usuario(nombre_usuario)
    print(saludo)
    
    # Ejercicio 3
    print("\n--- Ejercicio 3 ---")
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = int(input("Ingresa tu edad: "))
    residencia = input("Ingresa tu lugar de residencia: ")
    informacion_personal(nombre, apellido, edad, residencia)
    
    # Ejercicio 4
    print("\n--- Ejercicio 4 ---")
    radio = float(input("Ingresa el radio del círculo: "))
    area = calcular_area_circulo(radio)
    perimetro = calcular_perimetro_circulo(radio)
    print(f"Área del círculo: {area:.2f}")
    print(f"Perímetro del círculo: {perimetro:.2f}")
    
    # Ejercicio 5
    print("\n--- Ejercicio 5 ---")
    segundos = int(input("Ingresa la cantidad de segundos: "))
    horas = segundos_a_horas(segundos)
    print(f"{segundos} segundos equivalen a {horas:.2f} horas")
    
    # Ejercicio 6
    print("\n--- Ejercicio 6 ---")
    numero_tabla = int(input("Ingresa un número para generar su tabla de multiplicar: "))
    tabla_multiplicar(numero_tabla)
    
    # Ejercicio 7
    print("\n--- Ejercicio 7 ---")
    num_a = float(input("Ingresa el primer número: "))
    num_b = float(input("Ingresa el segundo número: "))
    suma, resta, mult, div = operaciones_basicas(num_a, num_b)
    print(f"Suma: {num_a} + {num_b} = {suma}")
    print(f"Resta: {num_a} - {num_b} = {resta}")
    print(f"Multiplicación: {num_a} × {num_b} = {mult}")
    print(f"División: {num_a} ÷ {num_b} = {div}")
    
    # Ejercicio 8
    print("\n--- Ejercicio 8 ---")
    peso = float(input("Ingresa tu peso en kilogramos: "))
    altura = float(input("Ingresa tu altura en metros: "))
    imc = calcular_imc(peso, altura)
    print(f"Tu IMC es: {imc:.2f}")
    
    # Ejercicio 9
    print("\n--- Ejercicio 9 ---")
    temp_celsius = float(input("Ingresa la temperatura en grados Celsius: "))
    temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)
    print(f"{temp_celsius}°C equivalen a {temp_fahrenheit:.2f}°F")
    
    # Ejercicio 10
    print("\n--- Ejercicio 10 ---")
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))
    promedio = calcular_promedio(num1, num2, num3)
    print(f"El promedio de {num1}, {num2} y {num3} es: {promedio:.2f}")
    