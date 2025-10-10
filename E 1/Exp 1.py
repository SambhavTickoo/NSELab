#!/usr/bin/env python3
# combined_ciphers.py
# Simple interactive tool: Caesar and Vigenere (encrypt/decrypt)
# Run: python3 combined_ciphers.py

def caesar_encrypt_char(ch, key):
    if ch.isupper():
        return chr((ord(ch) - ord('A') + key) % 26 + ord('A'))
    if ch.islower():
        return chr((ord(ch) - ord('a') + key) % 26 + ord('a'))
    return ch

def caesar_encrypt(text, key):
    return ''.join(caesar_encrypt_char(ch, key) for ch in text)

def caesar_decrypt(text, key):
    return caesar_encrypt(text, -key)

def normalize_key_letters(key):
    # return list of shifts for alphabetic characters in key (A/a -> 0)
    return [ord(c.upper()) - ord('A') for c in key if c.isalpha()]

def vigenere_process(text, key_shifts, mode='encrypt'):
    if not key_shifts:
        raise ValueError("Key must contain at least one letter.")
    out = []
    ki = 0
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shift = key_shifts[ki % len(key_shifts)]
            if mode == 'decrypt':
                shift = -shift
            out.append(chr((ord(ch) - base + shift) % 26 + base))
            ki += 1
        else:
            out.append(ch)
    return ''.join(out)

def vigenere_encrypt(text, key):
    ks = normalize_key_letters(key)
    return vigenere_process(text, ks, 'encrypt')

def vigenere_decrypt(text, key):
    ks = normalize_key_letters(key)
    return vigenere_process(text, ks, 'decrypt')

def main():
    print("=== Caesar & Vigenere Cipher - Simple Tool ===")
    print("Choose cipher / Cipher chuno:")
    print("  1) Caesar")
    print("  2) Vigenere")
    choice = input("Enter 1 or 2: ").strip()

    if choice not in ('1','2'):
        print("Invalid choice. Exit.")
        return

    mode = input("Encrypt or Decrypt? (e/d) : ").strip().lower()
    if mode not in ('e','d'):
        print("Invalid mode. Exit.")
        return
    is_encrypt = (mode == 'e')

    text = input("Enter text (plaintext or ciphertext) / Text dalo: ")

    if choice == '1':
        # Caesar
        try:
            key = int(input("Enter numeric key (0-25) / Key daalo: ").strip())
        except Exception:
            print("Invalid key. Must be an integer 0-25. Exit.")
            return
        key = key % 26
        if is_encrypt:
            out = caesar_encrypt(text, key)
            print("\nEncrypted (Caesar):", out)
        else:
            out = caesar_decrypt(text, key)
            print("\nDecrypted (Caesar):", out)

    else:
        # Vigenere
        key = input("Enter alphabetic key (e.g. LEMON) / Key daalo: ").strip()
        if not any(c.isalpha() for c in key):
            print("Invalid key. Must contain letters. Exit.")
            return
        if is_encrypt:
            out = vigenere_encrypt(text, key)
            print("\nEncrypted (Vigenere):", out)
        else:
            out = vigenere_decrypt(text, key)
            print("\nDecrypted (Vigenere):", out)

    print("\nDone. (Agar aur chahiye toh batao!)")

if __name__ == '__main__':
    main()
