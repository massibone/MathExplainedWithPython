'''
Obiettivo del Progetto
Codifica di un messaggio: Aggiungendo bit di parità per creare un codice di Hamming.
Introduzione di un errore: Modificando un bit nel codice.
Decodifica e correzione: Identificazione e correzione dell'errore introdotto.
'''
def calculate_parity_bits(data):
    n = len(data)
    parity_bits = 0
    
    # Determine the number of parity bits needed
    while (2**parity_bits) < (n + parity_bits + 1):
        parity_bits += 1
    
    return parity_bits

def insert_parity_bits(data):
    n = len(data)
    parity_bits = calculate_parity_bits(data)
    total_bits = n + parity_bits
    encoded_data = ['0'] * total_bits

    j = 0
    k = 1
    for i in range(1, total_bits + 1):
        if i == 2**j:
            j += 1
        else:
            encoded_data[i - 1] = data[-k]
            k += 1

    return ''.join(encoded_data)

def set_parity_bits(encoded_data):
    n = len(encoded_data)
    parity_bits = calculate_parity_bits(encoded_data)
    encoded_data = list(encoded_data)

    for i in range(parity_bits):
        parity_pos = 2**i
        parity_sum = 0
        for j in range(1, n + 1):
            if j & parity_pos == parity_pos:
                parity_sum ^= int(encoded_data[j - 1])
        
        encoded_data[parity_pos - 1] = str(parity_sum)
    
    return ''.join(encoded_data)

def hamming_encode(data):
    encoded_data = insert_parity_bits(data)
    encoded_data = set_parity_bits(encoded_data)
    return encoded_data

def introduce_error(encoded_data, error_pos):
    encoded_data = list(encoded_data)
    encoded_data[error_pos] = '1' if encoded_data[error_pos] == '0' else '0'
    return ''.join(encoded_data)

def detect_and_correct_error(encoded_data):
    n = len(encoded_data)
    parity_bits = calculate_parity_bits(encoded_data)
    error_pos = 0

    for i in range(parity_bits):
        parity_pos = 2**i
        parity_sum = 0
        for j in range(1, n + 1):
            if j & parity_pos == parity_pos:
                parity_sum ^= int(encoded_data[j - 1])
        
        error_pos += parity_pos if parity_sum != 0 else 0
    
    if error_pos != 0:
        print(f"Error detected at position: {error_pos}")
        encoded_data = list(encoded_data)
        encoded_data[error_pos - 1] = '1' if encoded_data[error_pos - 1] == '0' else '0'
    
    return ''.join(encoded_data)

def hamming_decode(encoded_data):
    decoded_data = []
    parity_bits = calculate_parity_bits(encoded_data)
    total_bits = len(encoded_data)
    
    j = 0
    for i in range(1, total_bits + 1):
        if i != 2**j:
            decoded_data.append(encoded_data[i - 1])
        else:
            j += 1
    
    return ''.join(decoded_data)

# Esempio di utilizzo
message = "1011"  # Messaggio di 4 bit
print(f"Original Message: {message}")

# Codifica
encoded_message = hamming_encode(message)
print(f"Encoded Message: {encoded_message}")

# Introduzione di un errore
encoded_message_with_error = introduce_error(encoded_message, 3)
print(f"Encoded Message with Error: {encoded_message_with_error}")

# Rilevamento e correzione dell'errore
corrected_message = detect_and_correct_error(encoded_message_with_error)
print(f"Corrected Message: {corrected_message}")

# Decodifica
decoded_message = hamming_decode(corrected_message)
print(f"Decoded Message: {decoded_message}")
