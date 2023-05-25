# Assignment 1:
# Create a loop that removes the vowels from the following names list: ['Jim', 'John', 'Marc', 'Danny', 'Peter'] . Add the results to a new list.

#%%
vowels = "aeoui"

#%%
names_list = ['Jim', 'John', 'Marc', 'Danny', 'Peter']
new_names_list = []


for name in names_list:
    for letter in name:
        if letter.lower() in vowels:
            new_name = name.replace(letter, "")

    new_names_list.append(new_name)
    
#%%
new_name