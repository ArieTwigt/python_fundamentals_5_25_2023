# Assignment 1: Assign a variable that holds the number of days until your next birthday
###############
#%%
from datetime import date

#%%
next_birthday = date(2024, 4, 1)
current_date = date.today()

date_difference = next_birthday - current_date
days_next_birthday = date_difference.days
print(f"My next birthday is in {days_next_birthday} days")

# Assignment 2: Calculate the surface of a circle with a diameter of 10 (radius^ * pi)
###############
# %%
import math

#%%
diameter = 10
radius = diameter / 2

size_circle = math.pow(radius, 2) * math.pi
size_circle_rounded = round(size_circle, 1)
size_circle_rounded


# Assignment 3: Create list that contains the files in your current working directory
###############
# %% 
import os

current_files_folders = os.listdir()
current_files_folders

# Assignment 4: Add a directory with the name our_functions
#############
# %%
os.mkdir("C:/Users/twigt/Downloads/from_python")


# %%
