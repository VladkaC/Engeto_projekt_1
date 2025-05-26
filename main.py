"""
projekt_1.py: první projekt do Engeto Online Python Akademie

author: Vladěna Ceplechová
email: VladenaC@seznam.cz
"""

TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',

    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',

    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

USERS = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"}

SELECTION = ["1", "2", "3"]
SEPARATOR = "-" * 45

username = input("username: ")
password = input("password: ")

if username in USERS and password == USERS[username] :
    print(SEPARATOR)
    print(f"Welcome to the app, {username}")
    print("We have 3 texts to be analyzed.")
    print(SEPARATOR)

    text_number = input(f"Enter a number btw. 1 and 3 to select:") 
    print(SEPARATOR)

    if text_number in SELECTION:
        words_list = TEXTS[int(text_number) - 1].replace(".","").replace(",", "").split()

        words_len = len(words_list)
        words_titlecase = 0
        word_lowercase = 0
        word_upper = 0
        words_number = 0
        sum_number = 0
        word_len = []

        for word in words_list:
            word_len.append(len(word))

            if word.isupper():
                word_upper += 1
            elif word.istitle():
                words_titlecase += 1
            elif word[0].islower() and not word.isdigit():
                word_lowercase += 1   
            else:
                words_number += 1
                sum_number += int(word)
     
        print(f"There are {words_len} words in the selected text.")
        print(f"There are {words_titlecase} titlecase words.")      
        print(f"There are {word_upper} uppercase words.")      
        print(f"There are {word_lowercase} lowercase words.")      
        print(f"There are {words_number} numeric strings.")      
        print(f"The sum of all the numbers {sum_number}")      
        print(SEPARATOR)      
        print(" LEN | OCCURENCES                     | NR.")      
        print(SEPARATOR)      
        
        for length in range(1, max(word_len)+1):
            count = word_len.count(length)
            stars = '*' * count
            print(f" {length:>3} | {stars.ljust(30)} | {count}") 

    else:
        print("Wrong number selected, terminating the program..")

else:
    print("unregistered user, terminating the program..")    