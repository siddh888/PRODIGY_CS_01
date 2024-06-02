def caesar_cipher(text, shift, mode='encrypt'):
    result = ""
    if mode == 'decrypt':
        shift = -shift
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

def main():
    while True:
        mode = input("Do you want to encrypt or decrypt? (enter 'encrypt' or 'decrypt', or 'exit' to quit): ").lower()
        if mode not in ['encrypt', 'decrypt', 'exit']:
            print("Invalid choice. Please enter 'encrypt', 'decrypt', or 'exit'.")
            continue
        if mode == 'exit':
            break
        text = input("Enter the message: ")
        shift = int(input("Enter the shift value: "))
        result = caesar_cipher(text, shift, mode)
        print(f"The {mode}ed text is: {result}")

if __name__ == "__main__":
    main()
