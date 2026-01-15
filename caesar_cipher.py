def caesar_cipher(text, shift, mode):
    result = ""

    shift = shift % 26

    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')

            if mode == "encrypt":
                result += chr((ord(char) - base + shift) % 26 + base)
            elif mode == "decrypt":
                result += chr((ord(char) - base - shift) % 26 + base)
        else:
            result += char 

    return result


message = input("Enter your message: ")
shift_value = int(input("Enter shift value: "))
choice = input("Type 'encrypt' or 'decrypt': ").lower()

if choice in ["encrypt", "decrypt"]:
    output = caesar_cipher(message, shift_value, choice)
    print(f"Result: {output}")
else:
    print("Invalid choice! Please type 'encrypt' or 'decrypt'.")
