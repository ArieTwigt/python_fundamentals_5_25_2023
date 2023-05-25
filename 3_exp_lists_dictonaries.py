#%% hobbies list
hobbies_list = ["Cycling", "Reading"]
hobbies_list

# %%
hobbies_list.append("Football")
hobbies_list.append("Chess")
hobbies_list

#%% remove "Football"
if "Football" in hobbies_list:
    hobbies_list.remove("Football")
    print("Removed Football")
else:
    print("Football not in hobbies")

hobbies_list


#%% Change the value of "Cycling" to "Mountainbiking"
hobbies_list.replace("Cycling", "Mountainbiking")

#%%
idx = hobbies_list.index("Cycling")
hobbies_list[idx] = "Mountainbiking"

#%% multiple values
idx = hobbies_list.index("Chess")
hobbies_list[idx] = "Go"




# %%
if value == "Chess"
then "Go"


[x if x != "Chess" else "Go" for x in hobbies_list]


new_list = []

for x in hobbies_list:
    if x != "Chess":
        new_list.append(x)
    else:
        new_list.append("Go")

#%%
hobbies_tuple = ("Chess", "Reading")

#%%
hobbies_tuple[0] = "Go"
# %%
hobbies_tuple.index("Reading")
# %%
