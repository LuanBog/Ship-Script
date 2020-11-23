import random
import sys

VOWELS = ["a", "e", "i", "o", "u"]

def make_ship_name(person1, person2):
    person1_index = 0

    for letter in person1:
        if letter in VOWELS:
            break 

        person1_index += 1

    return person1[:person1_index+1] + person2[person1_index:]

def ship(person1, person2):
    ship_percentage = random.randint(0, 100)   
    ship_name = make_ship_name(person1, person2)
    phrase = ""

    phrases = {"100": ["it's meant to be! ;D", "omg, the best! ;D", "get married!!! ;D"],
              "90": ["it will work :D", "They could work :D"],
              "50": ["possible :O", "50 50 :O", "it may possibly work :O"],
              "30": ["doesn't look promising, but it's still possible :)", "looks- not good but not that bad :)"],
              "10": ["doesn't look like it would work, chief :/", "ehhh, no :/"],
              "0": ["I'm sorry but no ;/", "just no, just no, just no ;/"]}

    for key, value in phrases.items():
        if ship_percentage >= int(key):
            phrase = random.choice(value)
            break

    return "{} x {} is {}% ( {} ) = {}".format(person1, person2, ship_percentage, phrase, ship_name)
    
if __name__ == "__main__":
    person1 = sys.argv[1]
    person2 = sys.argv[2]

    try:
        print("")
        print(ship(person1, person2))
        print("\n\n- Script by Luan")
    except Exception as e:
        print("Something went wrong ;c\nCommand is: python ship.py <Person 1> <Person 2> \nError: {}".format(e))
