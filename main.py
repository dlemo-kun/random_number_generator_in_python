import random

num_iteraciones = None
range = None

def generar_numeros_aleatorios(num_iteraciones, range):
    # This function generates random numbers and print them.
    # It takes two arguments: num_iteraciones (number of iterations) and range (range of random numbers).
    for _ in range(num_iteraciones):
        numero_aleatorio = random.randint(range[0], range[1])
        print(numero_aleatorio)

def def_num_iteraciones():
    # This function sets the number of iterations and range for generating random numbers.
    # It uses global variables num_iteraciones and range.
    global num_iteraciones, range
    if num_iteraciones is None or num_iteraciones > 2**16 or num_iteraciones < 2**16 * -1:
        num_iteraciones = int(input("Number of iterations: "))
        def_num_iteraciones()
    elif range is None or range > [2**16, 2**16] or range < [2**16 * -1, 2**16 * -1]:
        range = [int(input("Minimum value: ")), int(input("Maximum value: "))]
        def_num_iteraciones()
    else:
        if range[0] > range[1]:
            range = [range[1], range[0]]
        generar_numeros_aleatorios(num_iteraciones, range)

# Call the function to start the process of defining iterations and range.
def_num_iteraciones()

input('Press "Enter" to exit...')