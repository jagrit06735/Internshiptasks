def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result
def encrypt_file(filename, shift):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        encrypted_content = caesar_cipher(content, shift)

        with open("encrypted_" + filename, "w", encoding="utf-8") as file:
            file.write(encrypted_content)

        print("File encrypted successfully!")

    except FileNotFoundError:
        print("File not found.")

def decrypt_file(filename, shift):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            content = file.read()
        decrypted_content = caesar_cipher(content, -shift)
       
        with open("decrypted_" + filename, "w", encoding="utf-8") as file:
            file.write(decrypted_content)

        print("File decrypted successfully!")

    except FileNotFoundError:
        print("File not found.")
def main():
    print("===== File Encryption/Decryption Tool =====")
    print("1. Encrypt File")
    print("2. Decrypt File")

    choice = input("Enter choice (1/2): ")
    filename = input("Enter file name (with extension): ")
    shift = int(input("Enter shift value (e.g., 3): "))

    if choice == "1":
        encrypt_file(filename, shift)
    elif choice == "2":
        decrypt_file(filename, shift)
    else:
        print("Invalid choice.")
if __name__ == "__main__":
    main()