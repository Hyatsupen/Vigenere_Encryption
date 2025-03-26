from cipher import encrypt, decrypt
from file_utils import process_file
from utils import validate_key

def show_menu():
    print("\n=== MENU VIGENÈRE ===")
    print("1. Cifrar/Descifrar manualmente")
    print("2. Cifrar/Descifrar archivo (txt)")
    print("3. Salir")

def manual_mode():
    action = input("¿Cifrar (C) o Descifrar (D)? ").upper()
    if action not in ("C", "D"):
        print("Opción no válida.")
        return
    
    text = input("Texto: ")
    key = validate_key(input("Clave: "))
    
    result = encrypt(text, key) if action == "C" else decrypt(text, key)
    print(f"\nResultado: {result}")

def main():
    while True:
        show_menu()
        choice = input("Seleccione una opción (1-3): ")
        
        if choice == "1":
            manual_mode()
        elif choice == "2":
            process_file()
        elif choice == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

if __name__ == "__main__":
    main()