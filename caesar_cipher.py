def encrypt(text,shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift -97) % 26 + 97)
        else:
            result += char
    return result
def decrypt(text,shift):
    return encrypt(text, -shift)

def main():
    choice = input("Enter 'e' to encrypt, 'd' to decrypt: ")
    message = input("Enter your message: ")
    shift = int(input("Enter shift vaule: "))

    if choice == 'e':
        print("Encrypted:", encrypt(message, shift))
    elif choice == 'd':
        print("Decrypted:", decrypt(message, shift))
    else:
        print("Invalid choice")
if __name__ == "__main__":
    main()
