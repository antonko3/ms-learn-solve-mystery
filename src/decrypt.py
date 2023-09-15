print("Hello, Contosoville!")
# This is a comment that won't be interpreted as a command
# Associate the variable 'town' with the value "Contosoville"
town = "Contosoville"

# Print a message about the secret location
print( "The town I am looking for is " + town )

# Define a power (function) to chant a phrase
def chant( phrase ):
    # Glue three copies together and print it as a message
    print( phrase + phrase + phrase )

# Invoke the power to chant on the phrase "Contosoville!"
chant( "Contosoville! " )


# Investigate the alphabet - reduced only to UPPERCASE
alphabet_size = ord("Z") - ord("A") + 1
print(f"The alphabet size is {alphabet_size}")
first_letter_code = ord("A")
print(f"The first letter code is {first_letter_code}")

def lasso_letter(letter, shift_amount):
    # turn to uppercase ASCII
    letter_code = ord(letter.upper())
    # Zero the ASCII scale, A => n0
    letter_code = letter_code - first_letter_code
    # Shift to cipher
    letter_code = letter_code + shift_amount
    # Loop the alphabet
    letter_code = letter_code % alphabet_size
    # Restore scale to ASCII
    letter_code = letter_code + first_letter_code
    # Turn code to the deciphered letter
    letter = chr(letter_code)
    return letter

# Test lasso_letter
print( lasso_letter( 'n', 13 ) )

def lasso_word(word, shift_amount):
    # Add a variable foe storing a decoded word in progress
    decoded_word = ""
    for letter in word:
        decoded_letter = lasso_letter(letter, shift_amount)
        decoded_word = decoded_word + decoded_letter
    return decoded_word

def lasso_word(word, shift_amount):
    # Add a variable foe storing a decoded word in progress
    decoded_word = ""
    for letter in word:
        letter = lasso_letter(letter, shift_amount)
    return word

def lasso_word(word, shift_amount):
    word = [lasso_letter(letter, shift_amount) for letter in word]
    word = ''.join(word)
    return word

# Test lasso_word
word = "terra"
shift = 13

print(f"'{word}' @ {shift} is '{lasso_word(word, shift)}'")
print()

message = {
    "ncevy" : 13, 
    "gpvsui" : 25, 
    "ugflgkg" : -18, 
    "wjmmf" : -1
}
for word in message.keys():
    print(f"Decoding '{word}' @ {message[word]} gives: {lasso_word(word, message[word])}")