"""

Algoritmo burbuja

"""


def bucles(a):
    n = len(a)

    # Bucle padre
    for i in range(n - 1):
        # Bucle hijo
        for j in range(0, n - i - 1):
            # Comparar elementos adyacentes y hacer intercambio si es necesario
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]

def main():
    a = [8, 3, 1, 19, 14]
    bucles(a)
    print("Lista ordenada:", a)

if __name__ == "__main__":
    main()
