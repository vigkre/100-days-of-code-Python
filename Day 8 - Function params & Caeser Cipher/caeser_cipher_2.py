alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
def decrypt(original_text: str, shift_amount: int):
    decrypted_text = ""
    for letter in original_text:
        shift_position = alphabet.index(letter) - shift_amount
        shift_position %= len(alphabet)
        decrypted_text += alphabet[shift_position]
    print(decrypted_text)


def encrypt(original_text: str, shift_amount: int):
    encrypted_text = ""
    for letter in original_text:
        shift_position = alphabet.index(letter) + shift_amount
        shift_position %= len(alphabet)
        encrypted_text += alphabet[shift_position]
    print(encrypted_text)

# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.
def caesar(original_text: str, shift_amount: int, direction: str):
    output_text = ""
    if direction == "decode":
        shift_amount *= -1

    for letter in original_text:
        shift_position = alphabet.index(letter) + shift_amount
        shift_position %= len(alphabet)
        output_text += alphabet[shift_position]
    print(f"Here is the {direction}d result: {output_text}")

caesar(original_text=text, shift_amount=shift, direction=direction)
