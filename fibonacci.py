def saludo():
    print("¡Hola! este codigo muestra los primeros 10 números de la secuencia de Fibonacci :")

def generar_fibonacci(cantidad):
    """
    Genera una lista con los primeros números de la serie de Fibonacci usando como parámtero Cantidad.
    PARAMETROS:
        cantidad (int): La cantidad de números a generar.
    RETORNA:
        lista: Una lista con los números de la secuencia de Fibonacci.
    """
    
    fibonacci = [0, 1]  # Los dos primeros números de la secuencia
    for _ in range(2, cantidad):
        fibonacci.append(fibonacci[-1] + fibonacci[-2]) #calcula la serie de fibonacci
    return fibonacci

def main():
    saludo()
    numeros_fibonacci = generar_fibonacci(20) #se ejecuta la funcion usando como parámetro el número 20
    print(numeros_fibonacci) # da la serie de fibonacci hasta el número 20

if __name__ == "__main__":
    main()
