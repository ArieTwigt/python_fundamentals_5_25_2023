# Assignment: 1 Create a conditional statement that indicates if your name starts with an "A or not
###############

#%% 
name = input("Wat is your name?")

first_letter = name[0]

if first_letter == "A":
    print(f"Your name begins with an A! {name}")
else:
    print(f"Your names does not begin with an A: {name}")

# Assignment 2: Create a conditional statement that indicates if your name begins 
# with a vowel. If it does, change it into a non-vowel and otherwise. For example: Arie –> Brie or Rose –> Aose
################

# %%
import string
import random

name = input("Insert your name:\n")
vowels = list("aeoui")
non_vowels = string.ascii_lowercase
non_vowels = [letter 
              for letter 
              in list(string.ascii_lowercase)
              if letter not in vowels]

random_vowel = random.choice(vowels)
random_non_vowel = random.choice(non_vowels).upper()   

first_letter = name[0]

if first_letter.lower() in vowels:
    new_name = name.replace(first_letter, random_non_vowel)
    print(new_name)
else:
    new_name = name.replace(first_letter, random_vowel)
    print(new_name)


# Assignment 3: Create a conditional statement that 
# indicates if your age is between 18 and 68.
###############

#%%
from datetime import date

current_birthday = 1990
current_year = date.today().year

age = current_year - current_birthday

if age > 18 and age < 65:
    print("Werken met je bast")
else:
    print("Relaxed")

# %%
