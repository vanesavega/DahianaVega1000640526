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
    # ----------------- validación -------------------------------------
    if cantidad <= 0:  #validamos que  el parámetro Cantidad sea positivo y mayor que 0
        return []  
    if cantidad == 1:
        return [0]  # Si solo se necesita un número, retorna [0]

    # ----------------- función -------------------------------------
    fibonacci = [0, 1]  # Los dos primeros números de la secuencia
    for _ in range(2, cantidad):
        fibonacci.append(fibonacci[-1] + fibonacci[-2]) #calcula la serie de fibonacci
    return fibonacci

def main():
    saludo()
    cantidad = 20
    numeros_fibonacci = generar_fibonacci(cantidad) #se ejecuta la funcion usando como parámetro el número 20
    print(" -> ".join(map(str, numeros_fibonacci)))  #le da formato a la salida de los datos

if __name__ == "__main__":
    main()
