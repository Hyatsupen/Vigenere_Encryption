
#Pasar datos a formato String
def process_text(text: str) -> str:
    
    return text  


#Especificaciones de Error
def validate_key(key: str) -> str:
    """Valida que la clave tenga al menos 2 caracteres ASCII imprimibles."""
    if len(key) < 2:
        raise ValueError("La clave debe tener al menos 2 caracteres.")
    
    if not all(32 <= ord(c) <= 126 for c in key):
        raise ValueError("La clave solo puede contener caracteres ASCII imprimibles (32-126).")
    
    return key