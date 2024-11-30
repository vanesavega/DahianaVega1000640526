def saludo():
    print("¡Hola! este codigo muestra los primeros 10 números de la secuencia de Fibonacci :")

def generar_fibonacci(cantidad):
    fibonacci = [0, 1]
    for _ in range(2, cantidad):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return fibonacci

def main():
    saludo()
    numeros_fibonacci = generar_fibonacci(10)
    print(numeros_fibonacci)

if __name__ == "__main__":
    main()
