# Tarea 1: Imprime todos los números enteros del 0 al 150
for i in range(151):
    print(i)

# Tarea 2: Imprime todos los múltiplos de 5 entre 5 y 1,000
for i in range(5, 1001, 5):
    print(i)

# Tarea 3: Imprime números enteros del 1 al 100, reemplazando múltiplos de 5 y 10
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

# Tarea 4: Suma de enteros impares del 0 al 500,000
suma_impares = 0
for i in range(1, 500001, 2):
    suma_impares += i
print("La suma de enteros impares es:", suma_impares)

# Tarea 5: Cuenta regresiva de a 4 desde 2018
for i in range(2018, -1, -4):
    print(i)

# Tarea 6: Imprime múltiplos entre lowNum y highNum
lowNum = 2
highNum = 9
mult = 3
for i in range(lowNum, highNum + 1):
    if i % mult == 0:
        print(i)
