def caesar_cipher(text, shift, mode='encrypt'):
    result = ''
    
    # Determine the shift direction based on the mode
    if mode == 'decrypt':
        shift = -shift
    
    # Process each character in the input text
    for char in text:
        if char.isalpha():  # Check if the character is a letter
            ascii_offset = 65 if char.isupper() else 97
            new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            result += new_char
        else:
            result += char  # Non-alphabetic characters remain unchanged
    
    return result

def main():
    print("Caesar Cipher Program")
    mode = input("Do you want to encrypt or decrypt the message? (Type 'encrypt' or 'decrypt'): ").strip().lower()
    text = input("Enter your message: ")
    shift = int(input("Enter the shift value (an integer): "))
    
    if mode not in ['encrypt', 'decrypt']:
        print("Invalid mode selected. Please choose 'encrypt' or 'decrypt'.")
        return
    
    result = caesar_cipher(text, shift, mode)
    print(f"The resulting text is: {result}")

if __name__ == "__main__":
    main()
