# -*- coding: utf8 -*-
import random
import json

# quotes = [
#     "Ecoutez-moi, Monsieur Shakespeare, nous avons beau être ou ne pas être, nous sommes !", 
#     "On doit pouvoir choisir entre s'écouter parler et se faire entendre."
# ]

# characters = [
#     "alvin et les Chipmunks", 
#     "Babar", 
#     "betty boop", 
#     "calimero", 
#     "casper", 
#     "le chat potté", 
#     "Kirikou"
# ]

# for el in characters:
#     characters[characters.index(el)] = el.capitalize()
    
def read_values_from_json(file, key):
    values = []
    with open(file) as f:
        data = json.load(f)
        for entry in data:
            values.append(entry[key])
    return values 

# Give a json and return a list
def clean_strings(sentences):
    cleaned = []
    # Store quotes on a list. Create an empty list and add each sentence one by one.
    for sentence in sentences:
        # Clean quotes from whitespace and so on
        clean_sentence = sentence.strip()
        # don't use extend as it adds each letter one by one!
        cleaned.append(clean_sentence)
    return cleaned

def get_random_item_in(my_list):
    # TODO: get a random item
    index = random.randint(0,len(my_list)-1)
    # get an item from a list. For the moment, just get the first one.
    # TODO: show the quote

    return my_list[index]

# Return a random value from a json file
def random_value(source_path, key):
    all_values = read_values_from_json(source_path, key)
    clean_values = clean_strings(all_values)
    return get_random_item_in(clean_values)


# Return a random value from a json file
def random_character():
    return random_value('characters.json', 'character')

def random_quote():
    return random_value('quotes.json', 'quote')

# user_answer = 'A'
# while user_answer != 'B':
#     print(random_character()+" a dit : "+ random_quote())
#     user_answer = input('Tapez entrée pour découvrir une autre citation ou B pour quitter le programme.')


######################
#### INTERACTION ######
######################

# Print a random sentence.

def print_random_sentence():
    rand_quote = random_quote()
    rand_character = random_character()
    print(">>>> {} a dit : {}".format(rand_character, rand_quote))

def main_loop():
    while True:
        print_random_sentence()
        message = ('Voulez-vous voir une autre citation ?'
                   'Pour sortir du programme, tapez [B].')
        choice = input(message).upper()
        if choice == 'B':
            break
            # This will stop the loop!

if __name__ == '__main__':
    main_loop()