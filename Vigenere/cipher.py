
#Funcion para Encriptar
def encrypt(plain_text: str, key: str) -> str:
    encrypted_text = []
    key_repeated = (key * (len(plain_text) // len(key) + 1))[:len(plain_text)]
    
    for char, key_char in zip(plain_text, key_repeated):
        codigo = ord(char)
        if 32 <= codigo <= 126:
            shift = ord(key_char) - 31  # ¡Cambio crucial! (31 en lugar de 32)
            nuevo = 32 + (codigo - 32 + shift) % 95
            encrypted_char = chr(nuevo)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    return ''.join(encrypted_text)


def decrypt(encrypted_text: str, key: str) -> str:
    decrypted_text = []
    key_repeated = (key * (len(encrypted_text) // len(key) + 1))[:len(encrypted_text)]
    
    for char, key_char in zip(encrypted_text, key_repeated):
        codigo = ord(char)
        if 32 <= codigo <= 126:
            shift = ord(key_char) - 32
            nuevo = 32 + (codigo - 32 - shift) % 95  # Inverso del cifrado
            decrypted_text.append(chr(nuevo))
        else:
            decrypted_text.append(char)
    return ''.join(decrypted_text)