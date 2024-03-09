def bolzano_weierstrass(successione):
    # Controllo se la successione è vuota
    if not successione:
        return None
    
    # Inizializzo i valori minimo e massimo
    minimo = successione[0]
    massimo = successione[0]
    
    # Trovo il minimo e il massimo nella successione
    for numero in successione:
        if numero < minimo:
            minimo = numero
        elif numero > massimo:
            massimo = numero
    
    # Se il minimo e il massimo sono uguali, la successione contiene un solo elemento
    if minimo == massimo:
        return [minimo]  # Restituisco una lista con l'unico elemento
    
    # Trovo una sottosuccessione convergente utilizzando il metodo di bisezione
    def trova_sottosuccessione_in_intervallo(inizio, fine):
        if inizio == fine:
            return [successione[inizio]]  # Se inizio e fine coincidono, restituisco una lista con l'unico elemento
        
        # Trovo il punto medio dell'intervallo
        medio = (inizio + fine) // 2
        
        # Trovo una sottosuccessione nel primo e nel secondo intervallo
        sottosuccessione_in_primo_intervallo = trova_sottosuccessione_in_intervallo(inizio, medio)
        sottosuccessione_in_secondo_intervallo = trova_sottosuccessione_in_intervallo(medio + 1, fine)
        
        # Confronto le lunghezze delle sottosuccessioni nei due intervalli
        if len(sottosuccessione_in_primo_intervallo) >= len(sottosuccessione_in_secondo_intervallo):
            return sottosuccessione_in_primo_intervallo
        else:
            return sottosuccessione_in_secondo_intervallo
    
    # Trovo una sottosuccessione convergente nell'intervallo [0, len(successione)-1]
    return trova_sottosuccessione_in_intervallo(0, len(successione)-1)

# Esempio di utilizzo:
successione = [1, 0.5, 0.75, 0.6, 0.65, 0.625, 0.635, 0.63]
sottosuccessione_convergente = bolzano_weierstrass(successione)
print("Una sottosuccessione convergente è:", sottosuccessione_convergente)
