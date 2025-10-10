# Caesar Cipher - Simple Version

def encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + key) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + key) % 26 + 97)
        else:
            result += ch
    return result

def decrypt(text, key):
    return encrypt(text, -key)

# --- main program ---
text = input("Enter text: ")
key = int(input("Enter key (0-25): "))
choice = input("Encrypt or Decrypt (e/d): ").lower()

if choice == 'e':
    print("Encrypted text:", encrypt(text, key))
elif choice == 'd':
    print("Decrypted text:", decrypt(text, key))
else:
    print("Invalid choice")
