# Trabajo Práctico 4: Estructuras Repetitivas

# 1) Imprimir números del 0 al 100 (uno por línea)
for i in range(101):
    print(i)

# 2) Contar la cantidad de dígitos de un número ingresado por el usuario
numero = input("Ingresa un número entero: ")
print("Cantidad de dígitos:", len(numero.strip('-')))

# 3) Sumar todos los enteros entre dos valores dados (excluyéndolos)
a = int(input("Ingrese el primer número: "))
b = int(input("Ingrese el segundo número: "))
menor = min(a, b)
mayor = max(a, b)
suma = sum(range(menor + 1, mayor))
print("Suma entre los valores:", suma)

# 4) Sumar números ingresados por el usuario hasta que ingrese 0
suma = 0
while True:
    num = int(input("Ingresa un número (0 para terminar): "))
    if num == 0:
        break
    suma += num
print("Suma total:", suma)

# 5) Juego de adivinar un número entre 0 y 9
import random
numero_secreto = random.randint(0, 9)
intentos = 0
while True:
    intento = int(input("Adivina el número (0-9): "))
    intentos += 1
    if intento == numero_secreto:
        break
print(f"¡Correcto! Lo lograste en {intentos} intentos.")

# 6) Imprimir todos los números pares entre 0 y 100 en orden decreciente
for i in range(100, -1, -2):
    print(i)

# 7) Sumar todos los números entre 0 y un número positivo dado
n = int(input("Ingrese un número entero positivo: "))
if n >= 0:
    print("Suma:", sum(range(n + 1)))
else:
    print("Número no válido.")

# 8) Ingresar 100 números e indicar cantidad de pares, impares, negativos y positivos
pares = impares = negativos = positivos = 0
cantidad = 100  # cambiar este valor para pruebas más cortas
for _ in range(cantidad):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
    if num < 0:
        negativos += 1
    elif num > 0:
        positivos += 1
print(f"Pares: {pares}, Impares: {impares}, Negativos: {negativos}, Positivos: {positivos}")

# 9) Calcular la media de 100 números ingresados por el usuario
suma = 0
cantidad = 100  # cambiar este valor para pruebas más cortas
for _ in range(cantidad):
    num = int(input("Ingrese un número: "))
    suma += num
print("Media:", suma / cantidad)

# 10) Invertir los dígitos de un número ingresado por el usuario
numero = input("Ingresa un número para invertir sus dígitos: ")
if numero.startswith('-'):
    invertido = '-' + numero[:0:-1]
else:
    invertido = numero[::-1]
print("Número invertido:", invertido)
