import random

# Word list for the game
word_list = [
    'python', 'java', 'swift', 'hangman', 'programming', 'developer', 'code', 'computer',
    'software', 'algorithm', 'function', 'variable', 'keyboard', 'internet', 'network', 'security'
]

# Function to get a random word
def get_random_word():
    return random.choice(word_list)
