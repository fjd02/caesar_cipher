text = input("Introduce the message: ")
while True:
    try:
        shift = int(input("Introduce the shift: "))
        break
    except ValueError:
        print("You must introduce a number.")

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
    encrypted_text = ''

    for char in message.lower():
        if char in alphabet:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]
        else:
            encrypted_text += char
            
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

caesar(text, shift)