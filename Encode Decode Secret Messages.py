# Encode or Decode Secret Messages
def caesar (start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
           position = alphabet.index(char)
           new_position = position + shift_amount
           end_text += alphabet[new_position] 
        else:
            end_text += char
    print(f"Here's the {direction}d result: {end_text}")
      
from english import alphabet  
# from art import logo (uncomment if you want to print the logo)
# print(logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower() 
    shift = int(input("Type the shift number:\n"))
   # What if the user enters a shift that is greater than the 
   # number of letters in the alphabet? Read explanation below
    shift = shift % 26  
    
    caesar(start_text= text, shift_amount= shift, cipher_direction= direction)
    restart = input("Type 'Yes' if you want to go again. otherwise type 'no'.\n")
    if restart =="no":
        should_end = True
        print("Goodbye. Visit again to encode or decode.")
        