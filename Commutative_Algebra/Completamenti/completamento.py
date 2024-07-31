def completion_ideal(A, I, n):
    """ Calcola il completamento dell'anello A rispetto all'ideale I fino a I^n """
    completions = []
    for i in range(1, n + 1):
        completions.append(f"{A}/{I}^{i}")
    return completions

# Esempio pratico con A = Z[x] e I = (x)
A = "Z[x]"
I = "(x)"
n = 5

completion = completion_ideal(A, I, n)

print(f"Approssimazioni del completamento di {A} rispetto a {I}:")
for c in completion:
    print(c)

