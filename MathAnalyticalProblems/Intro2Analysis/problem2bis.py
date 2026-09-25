import math

def function(x):
    return math.exp(-x) * math.cos(math.pi * x)

def riemann_sum(n):
    sum = 0
    for i in range(n + 1):
        sum += math.sqrt(1 + math.exp(-2 * i))
    return sum

def main():
    n = int(input("Inserisci il numero di termini per la somma di Riemann (n): "))

    approximation = riemann_sum(n)
    print(f"L'approssimazione della somma con {n} termini di Riemann è: {approximation}")

if __name__ == "__main__":
    main()
