## Assignment 1: Append .Jr. to the current full_name variable which will result in Erling Haaland Jr.
################

#%%

#%% 
print("Loading from database")
first_name = "Erling"
last_name  = "Haaland"
full_name = f"{first_name} {last_name}"
print("Converting data")

# %%
full_name = f"{full_name} .Jr"

#%% Replace the first name of Erling Haaland (Erling) to only the abbreviation of his first hame. 
# #This should result in: E. Haaland Jr.


# %%
full_name

## Assignment 2:
##################

#%%
# split string into list
full_name_list = full_name.split(" ")

# get the first value of the list ("Erling") 
first_name = full_name_list[0]

# get the first letter from the value ("E")
first_letter = first_name[0] 

# replace the current first value of the list ("Erling") for the first letter
# with a period ("E.")
full_name_list[0] = first_letter + "."

# join the list with seperate strings into a single string
full_name_new = " ".join(full_name_list)
full_name_new



# Assignment 3
###############
#%%
# Create a variable called nationality with the value "Norway". 
# Use this variable to create the string (sentence) "E. Haaland .Jr - Nationality: Norway". Print out the sentence.
nationality = "Norway"
sentence = f"{full_name_new} - Nationality: {nationality}"
print(sentence)
# %%
