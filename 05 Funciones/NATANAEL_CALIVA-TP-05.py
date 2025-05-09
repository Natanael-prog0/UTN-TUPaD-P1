
# TP 5 - Listas - UTN a distancia

# 1) Lista con los números del 1 al 100 que sean múltiplos de 4
multiples_de_4 = list(range(4, 101, 4))
print("1) Múltiplos de 4 del 1 al 100:", multiples_de_4)

# 2) Lista con cinco elementos y mostrar el penúltimo
gustos = ["pizza", "helado", "cine", "viajar", "leer"]
print("2) Penúltimo elemento de la lista:", gustos[-2])

# 3) Lista vacía, agregar tres palabras con append
lista_vacia = []
lista_vacia.append("hola")
lista_vacia.append("python")
lista_vacia.append("listas")
print("3) Lista con palabras agregadas:", lista_vacia)

# 4) Reemplazar el segundo y último valor de la lista “animales”
animales = ["perro", "gato", "conejo", "pez"]
animales[1] = "loro"
animales[-1] = "oso"
print("4) Lista animales modificada:", animales)

# 5) Crea una lista llamada numeros con los elementos [8, 15, 3, 22, 7].

#Busca el valor máximo de la lista usando max(numeros), que en este caso es 22.

#Elimina ese valor máximo de la lista con remove(), es decir, elimina el 22.

#Imprime la lista resultante, que será [8, 15, 3, 7].

# 6) Lista con números del 10 al 30 (incluido), saltos de 5, mostrar los dos primeros
lista_6 = list(range(10, 31, 5))
print("6) Primeros dos elementos:", lista_6[:2])

# 7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos”
autos = ["sedan", "polo", "suran", "gol"]
autos[1:3] = ["fiesta", "focus"]
print("7) Lista autos modificada:", autos)

# 8) Lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15
dobles = []
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)
print("8) Lista dobles:", dobles)

# 9) Modificar la lista “compras”
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]
compras[2].append("jugo")  # a)
compras[1][1] = "tallarines"  # b)
compras[0].remove("pan")  # c)
print("9) Lista compras modificada:", compras)

# 10) Lista anidada con elementos específicos
lista_anidada = [
    15,
    True,
    [25.5, 57.9, 30.6],
    False
]
print("10) Lista anidada:", lista_anidada)
