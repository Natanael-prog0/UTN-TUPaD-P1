# TP7 - RECURSIVIDAD
# Tecnicatura Universitaria en Programación

# ==========================================
# EJERCICIO 1: FACTORIAL RECURSIVO
# ==========================================

def factorial(n):
    """
    Calcula el factorial de un número usando recursividad.
    Caso base: factorial(0) = factorial(1) = 1
    Caso recursivo: factorial(n) = n * factorial(n-1)
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def ejercicio_1():
    """Calcula y muestra el factorial de números del 1 hasta el número ingresado"""
    print("=== EJERCICIO 1: FACTORIAL ===")
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 1:
            print("Por favor ingrese un número mayor a 0")
            return
        
        print(f"\nFactoriales del 1 al {numero}:")
        for i in range(1, numero + 1):
            print(f"{i}! = {factorial(i)}")
    except ValueError:
        print("Error: Ingrese un número válido")

# ==========================================
# EJERCICIO 2: FIBONACCI RECURSIVO
# ==========================================

def fibonacci(n):
    """
    Calcula el valor de Fibonacci en la posición n.
    Caso base: fib(0) = 0, fib(1) = 1
    Caso recursivo: fib(n) = fib(n-1) + fib(n-2)
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def ejercicio_2():
    """Muestra la serie de Fibonacci hasta la posición especificada"""
    print("\n=== EJERCICIO 2: FIBONACCI ===")
    try:
        posicion = int(input("Ingrese la posición hasta donde mostrar Fibonacci: "))
        if posicion < 0:
            print("Por favor ingrese un número no negativo")
            return
        
        print(f"\nSerie de Fibonacci hasta la posición {posicion}:")
        for i in range(posicion + 1):
            print(f"F({i}) = {fibonacci(i)}")
    except ValueError:
        print("Error: Ingrese un número válido")

# ==========================================
# EJERCICIO 3: POTENCIA RECURSIVA
# ==========================================

def potencia(base, exponente):
    """
    Calcula base^exponente usando recursividad.
    Caso base: base^0 = 1
    Caso recursivo: base^n = base * base^(n-1)
    """
    if exponente == 0:
        return 1
    elif exponente > 0:
        return base * potencia(base, exponente - 1)
    else:
        # Para exponentes negativos: base^(-n) = 1 / base^n
        return 1 / potencia(base, -exponente)

def ejercicio_3():
    """Prueba la función de potencia recursiva"""
    print("\n=== EJERCICIO 3: POTENCIA ===")
    try:
        base = float(input("Ingrese la base: "))
        exponente = int(input("Ingrese el exponente: "))
        
        resultado = potencia(base, exponente)
        print(f"\n{base}^{exponente} = {resultado}")
    except ValueError:
        print("Error: Ingrese números válidos")

# ==========================================
# EJERCICIO 4: DECIMAL A BINARIO
# ==========================================

def decimal_a_binario(n):
    """
    Convierte un número decimal a binario usando recursividad.
    Caso base: si n == 0, devuelve "0"
    Caso recursivo: convierte n//2 y concatena con n%2
    """
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

def ejercicio_4():
    """Convierte números decimales a binario"""
    print("\n=== EJERCICIO 4: DECIMAL A BINARIO ===")
    try:
        numero = int(input("Ingrese un número decimal positivo: "))
        if numero < 0:
            print("Por favor ingrese un número positivo")
            return
        
        if numero == 0:
            binario = "0"
        else:
            binario = decimal_a_binario(numero)
        
        print(f"\n{numero} en binario es: {binario}")
    except ValueError:
        print("Error: Ingrese un número válido")

# ==========================================
# EJERCICIO 5: PALÍNDROMO RECURSIVO
# ==========================================

def es_palindromo(palabra):
    """
    Verifica si una palabra es palíndromo usando recursividad.
    Caso base: palabra vacía o de 1 caracter es palíndromo
    Caso recursivo: primer y último caracter iguales Y el resto es palíndromo
    """
    # Convertir a minúsculas para comparación
    palabra = palabra.lower()
    
    # Caso base: cadena vacía o de un solo carácter
    if len(palabra) <= 1:
        return True
    
    # Caso recursivo: comparar primer y último carácter
    if palabra[0] == palabra[-1]:
        return es_palindromo(palabra[1:-1])
    else:
        return False

def ejercicio_5():
    """Verifica si las palabras ingresadas son palíndromos"""
    print("\n=== EJERCICIO 5: PALÍNDROMO ===")
    palabra = input("Ingrese una palabra (sin espacios ni tildes): ").strip()
    
    if es_palindromo(palabra):
        print(f"'{palabra}' ES un palíndromo")
    else:
        print(f"'{palabra}' NO es un palíndromo")

# ==========================================
# EJERCICIO 6: SUMA DE DÍGITOS
# ==========================================

def suma_digitos(n):
    """
    Suma todos los dígitos de un número usando recursividad.
    Caso base: si n < 10, devuelve n
    Caso recursivo: suma el último dígito + suma_digitos del resto
    """
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

def ejercicio_6():
    """Calcula la suma de dígitos de un número"""
    print("\n=== EJERCICIO 6: SUMA DE DÍGITOS ===")
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        if numero < 0:
            print("Por favor ingrese un número positivo")
            return
        
        resultado = suma_digitos(numero)
        print(f"\nLa suma de los dígitos de {numero} es: {resultado}")
    except ValueError:
        print("Error: Ingrese un número válido")

# ==========================================
# EJERCICIO 7: CONTAR BLOQUES DE PIRÁMIDE
# ==========================================

def contar_bloques(n):
    """
    Cuenta el total de bloques en una pirámide.
    Caso base: si n == 1, devuelve 1
    Caso recursivo: n + contar_bloques(n-1)
    """
    if n <= 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

def ejercicio_7():
    """Calcula el total de bloques necesarios para una pirámide"""
    print("\n=== EJERCICIO 7: BLOQUES DE PIRÁMIDE ===")
    try:
        base = int(input("Ingrese el número de bloques en la base: "))
        if base < 1:
            print("Por favor ingrese un número mayor a 0")
            return
        
        total = contar_bloques(base)
        print(f"\nPara una pirámide con base de {base} bloques se necesitan {total} bloques en total")
        
        # Mostrar la estructura de la pirámide
        print("\nEstructura de la pirámide:")
        for i in range(base, 0, -1):
            print(f"Nivel {base-i+1}: {i} bloques")
    except ValueError:
        print("Error: Ingrese un número válido")

# ==========================================
# EJERCICIO 8: CONTAR DÍGITO ESPECÍFICO
# ==========================================

def contar_digito(numero, digito):
    """
    Cuenta cuántas veces aparece un dígito en un número.
    Caso base: si numero == 0, devuelve 0
    Caso recursivo: verifica último dígito y suma con llamada recursiva
    """
    if numero == 0:
        return 0
    
    # Contar si el último dígito coincide
    count = 1 if (numero % 10) == digito else 0
    
    # Llamada recursiva con el resto del número
    return count + contar_digito(numero // 10, digito)

def ejercicio_8():
    """Cuenta las apariciones de un dígito en un número"""
    print("\n=== EJERCICIO 8: CONTAR DÍGITO ===")
    try:
        numero = int(input("Ingrese un número entero positivo: "))
        digito = int(input("Ingrese el dígito a contar (0-9): "))
        
        if numero < 0:
            print("Por favor ingrese un número positivo")
            return
        
        if digito < 0 or digito > 9:
            print("El dígito debe estar entre 0 y 9")
            return
        
        # Caso especial: si el número es 0 y buscamos el 0
        if numero == 0 and digito == 0:
            apariciones = 1
        else:
            apariciones = contar_digito(numero, digito)
        
        print(f"\nEl dígito {digito} aparece {apariciones} veces en el número {numero}")
    except ValueError:
        print("Error: Ingrese números válidos")

# ==========================================
# FUNCIÓN PRINCIPAL - MENÚ
# ==========================================

def menu_principal():
    """Menú principal para ejecutar todos los ejercicios"""
    while True:
        print("\n" + "="*50)
        print("    TP7 - RECURSIVIDAD - MENÚ PRINCIPAL")
        print("="*50)
        print("1. Factorial recursivo")
        print("2. Serie de Fibonacci")
        print("3. Potencia recursiva")
        print("4. Decimal a binario")
        print("5. Verificar palíndromo")
        print("6. Suma de dígitos")
        print("7. Contar bloques de pirámide")
        print("8. Contar dígito específico")
        print("9. Ejecutar todos los ejercicios")
        print("0. Salir")
        print("="*50)
        
        try:
            opcion = int(input("Seleccione una opción: "))
            
            if opcion == 1:
                ejercicio_1()
            elif opcion == 2:
                ejercicio_2()
            elif opcion == 3:
                ejercicio_3()
            elif opcion == 4:
                ejercicio_4()
            elif opcion == 5:
                ejercicio_5()
            elif opcion == 6:
                ejercicio_6()
            elif opcion == 7:
                ejercicio_7()
            elif opcion == 8:
                ejercicio_8()
            elif opcion == 9:
                print("Ejecutando todos los ejercicios...")
                ejercicio_1()
                ejercicio_2()
                ejercicio_3()
                ejercicio_4()
                ejercicio_5()
                ejercicio_6()
                ejercicio_7()
                ejercicio_8()
            elif opcion == 0:
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Intente nuevamente.")
                
        except ValueError:
            print("Error: Ingrese un número válido")
        
        input("\nPresione Enter para continuar...")

# ==========================================
# EJEMPLOS DE PRUEBA
# ==========================================

def ejemplos_prueba():
    """Función para probar rápidamente todas las funciones"""
    print("=== EJEMPLOS DE PRUEBA ===")
    
    # Factorial
    print(f"5! = {factorial(5)}")
    
    # Fibonacci
    print(f"Fibonacci(7) = {fibonacci(7)}")
    
    # Potencia
    print(f"2^8 = {potencia(2, 8)}")
    
    # Decimal a binario
    print(f"10 en binario: {decimal_a_binario(10)}")
    
    # Palíndromo
    print(f"'radar' es palíndromo: {es_palindromo('radar')}")
    print(f"'python' es palíndromo: {es_palindromo('python')}")
    
    # Suma dígitos
    print(f"Suma dígitos de 1234: {suma_digitos(1234)}")
    
    # Contar bloques
    print(f"Bloques pirámide base 4: {contar_bloques(4)}")
    
    # Contar dígito
    print(f"Dígito 2 en 12233421: {contar_digito(12233421, 2)}")

# Ejecutar el programa
if __name__ == "__main__":
    # ejemplos_prueba()
    
    # Ejecutar menú principal
    menu_principal()