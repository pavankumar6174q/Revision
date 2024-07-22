#LIFE SPAN CODE

# age = int(input("age :"))
# n = 90
# r = 90 - age
# days = r * 365
# months = r * 12
# weeks = r * 52
# print(f"if you live upto 90 years of age you have {days} days, {weeks} weeks and {months} months left")

#TIP CALCULATOR

# Total = float(input("enter the total amount :  "))
# ppl = int(input('enter the total ppl :  '))
# tip = int(input('enter the tip amount like 10%, 12% "or" 15% : '))


# tip_per = tip/100 + 1 
# each_person_cost = Total/ppl * tip_per
# print(each_person_cost)


# #ODD OR EVEN
# n = int(input('enter the number :  '))
# if n%2 == 0:
#     print("its and even number")
# else:
#     print('its an odd number')

# print("Thank you for choosing Python Pizza Deliveries!")
# size = input() # What size pizza do you want? S, M, or L
# add_pepperoni = input() # Do you want pepperoni? Y or N
# extra_cheese = input() # Do you want extra cheese? Y or N
# # 🚨 Don't change the code above 👆
# # Write your code below this line 👇
# bill = 0
# if size == "S":
#   bill += 15
#   if add_pepperoni == "Y":
#         bill += 2

# elif size == "M":
#   bill += 20
#   if add_pepperoni == "Y":
#     bill += 3
# elif size == "L":
#   bill += 25
#   if add_pepperoni == "Y":
#     bill += 3
# if extra_cheese == "Y":
#   bill += 1
# print(f"Thank you for choosing Python Pizza Deliveries! Your final bill is: ${bill}.")

#==============================================================================================================
#TREASURE LOCATOR

# line1 = ["⬜️","️⬜️","️⬜️"]
# line2 = ["⬜️","⬜️","️⬜️"]
# line3 = ["⬜️️","⬜️️","⬜️️"]

# #now creating a single list of the above mentioned lists into a list named map
# map = [line1, line2, line3]
# print("Hiding your treasure! X marks the spot.")
# position = input() # Where do you want to put the treasure?


# # here we are assigning a letter variable to the first positon of our input
# #for example our input is A1 the letter will be assigned to A cause we are taking its position 
# #position[0] of A1 is A
# letter = position[0].lower()

# # here we are creating a separate list which helps us map the thing better
# abc = ["a", "b", "c"]

# #now we can use the above abc list to get the position of the letter in the map
# # like image we have 3 columns a is first column and b is second like that
# letter_index = abc.index(letter) # this helps us to select the column according to the input position
# number_index = int(position[1]) - 1 # this is the line in which we take the second position of the input and then subtract it with 1 
# map[number_index][letter_index] = "X"  # then we can link them in the map

# print(f"{line1}\n{line2}\n{line3}")


#==============================================================================================================


# # ROCK PAPER SCISSORS
# import random
# options = ['rock', 'paper', 'scissors']
# user = int(input('select 0 for rock, 1 for paper, 2 for scissors\n'))





# if user > 2:
#     print("enter the correct number")
#     print("you lose")
# else:
#     print(options[user])
#     computer = random.randint(0,2)
#     print(options[computer])

#     if user ==0 and computer == 2:
#         print("you win")
#     elif user == 2 and computer == 0:
#         print("you lose")
#     elif user> computer:
#         print("you win")
#     elif user< computer:
#         print("you lose")
#     elif user == computer:
#         print("its a draw")
            



#==============================================================================================================

#PRIME CHECKER

# def prime_checker( number):
#     is_prime = True
#     for i in range(2, number):
#         if number %i == 0:
#             is_prime = False
#     if is_prime:
#         print('its a prime ')
#     else:
#         print('its not a prime number')
# n = int(input("enter number:  "))
# prime_checker(number = n)


#==============================================================================================================

#PASSWORD GENERATOR

#Password Generator Project
# import random
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
# symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# print("Welcome to the PyPassword Generator!")
# nr_letters= int(input("How many letters would you like in your password?\n")) 
# nr_symbols = int(input(f"How many symbols would you like?\n"))
# nr_numbers = int(input(f"How many numbers would you like?\n"))

# #Eazy Level - Order not randomised:
# #e.g. 4 letter, 2 symbol, 2 number = JduE&!91
# passw = ''
# for i in range(0, nr_letters):
#     passw += random.choice(letters)
# for j in range(0, nr_numbers):
#     passw += random.choice(numbers)
# for k in range(0, nr_symbols):
#     passw += random.choice(symbols)
# print(f'easy pass is : {passw}')


# #Hard Level - Order of characters randomised:
# #e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# password = []
# for i in range(0, nr_letters):
#     password.append(random.choice(letters))
# for i in range(0, nr_numbers):
#     password.append(random.choice(numbers))
# for i in range(0, nr_symbols):
#     password.append(random.choice(symbols))
# random.shuffle(password)

# hard = ''
# for i in password:
#     hard += i
# print(hard)

#==============================================================================================================

#HANG MAN GAME

#Step 4

# import random

# stages = ['''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  / \  |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#  /    |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|\  |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#  /|   |
#       |
#       |
# =========''', '''
#   +---+
#   |   |
#   O   |
#   |   |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#   O   |
#       |
#       |
#       |
# =========
# ''', '''
#   +---+
#   |   |
#       |
#       |
#       |
#       |
# =========
# ''']

# #Step 5

# import random

# from hangman_words import word_list

# #TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# #Delete this line: word_list = ["ardvark", "baboon", "camel"]
# chosen_word = random.choice(word_list)
# word_length = len(chosen_word)

# end_of_game = False
# lives = 6

# #TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

# #Testing code
# print(f'Pssst, the solution is {chosen_word}.')

# #Create blanks
# display = []
# for _ in range(word_length):
#     display += "_"

# while not end_of_game:
#     guess = input("Guess a letter: ").lower()

#     #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
#     if guess in display:
#         print("You have already entered this letter")
#     #Check guessed letter
#     for position in range(word_length):
#         letter = cenen
#         print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
#         if letter == guess:
#             display[position] = letter

#     #Check if user is wrong.
#     if guess not in chosen_word:
#         #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
#         print(f'your guess is {guess}, it is not in the word')
#         lives -= 1
#         if lives == 0:
#             end_of_game = True
#             print("You lose.")

#     #Join all the elements in the list and turn it into a String.
#     print(f"{' '.join(display)}")

#     #Check if user has got all letters.
#     if "_" not in display:
#         end_of_game = True
#         print("You win.")

#     #TODO-2: - Import the stages from hangman_art.py and make this error go away.
#     print(stages[lives])


#==============================================================================================================

#CAESAR CIPHER

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Combine the encrypt() and decrypt() functions into a single function called caesar(). 
def caesar(plain_text, shift_amount, direction):
  cipher_text = ""
  if direction == "decode":
    shift_amount *= -1
    
  for letter in plain_text:
    position = alphabet.index(letter)
    new_position = position + shift_amount
    cipher_text += alphabet[new_position]
  print(f"The {direction}ed text is {cipher_text}")

# def encrypt(plain_text, shift_amount):
#   cipher_text = ""
#   for letter in plain_text:
#     position = alphabet.index(letter)
#     new_position = position + shift_amount
#     cipher_text += alphabet[new_position]
#   print(f"The encoded text is {cipher_text}")

# def decrypt(cipher_text, shift_amount):
#   plain_text = ""
#   for letter in cipher_text:
#     position = alphabet.index(letter)
#     new_position = position - shift_amount
#     plain_text += alphabet[new_position]
#   print(f"The decoded text is {plain_text}")

# if direction == "encode":
#   encrypt(plain_text=text, shift_amount=shift)
# elif direction == "decode":
#   decrypt(cipher_text=text, shift_amount=shift)

#TODO-2: Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(plain_text=text, shift_amount=shift,direction= direction)