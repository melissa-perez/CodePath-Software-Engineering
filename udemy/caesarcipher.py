from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(text, shift_by, direction):
  text_length = len(text)
  message = []

  if direction == "encode":
    for i in range(text_length):
      if text[i] in alphabet:
        found_char = alphabet.index(text[i])
        message.append(alphabet[(found_char + shift_by) % 26])
      else:
        message.append(text[i])
  elif direction == "decode":
    for i in range(text_length):
      if text[i] in alphabet:
        found_char = alphabet.index(text[i])
        message.append(alphabet[(found_char - shift_by) % 26])
      else:
        message.append(text[i])
  
  message = "".join(message)  
  print(f"The encoded text is {message}." if direction == "encode" else f"The decoded text is {message}.")

is_restart = True
while is_restart:
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  caesar(text, shift, direction)

  restart = input("Would you like to try a different word? Enter yes to go again:\n")
  
  if restart != "yes":
    is_restart = False
    print("End of program.")