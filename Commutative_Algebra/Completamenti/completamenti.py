
def completion_mod_2(n):
    """ Calcola il completamento degli interi modulo 2^n """
    completions = []
    for i in range(n):
        completions.append(2 ** i)
    return completions

# Numero di approssimazioni
n = 5
completion = completion_mod_2(n)

print(f"Approssimazioni del completamento degli interi rispetto a 2^{n}:")
for i, c in enumerate(completion):
    print(f"Modulo 2^{i+1}: {c}")
