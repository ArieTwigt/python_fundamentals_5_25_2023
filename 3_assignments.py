# Assignment 1
##############

#%% create a dictionary of a person
person_1 = {"name": "James", 
            "age": 50}

# %%
person_1['age']

# Assignment 2
##############
# %%
family_dict = {} # create an empty dictionary
family_dict['name'] = 'Jones'
family_dict['members'] = []

#%%
family_dict['members']


# %% add a member
family_dict['members'].append(person_1)

# %% create additional persons
person_2= {"name": "mary", 
           "age": 30}
person_3= {"name": "jim", 
           "age": 40}
person_4= {"name": "winston", 
           "age": 50}
person_5= {"name": "marc", 
           "age": 60}

#%%
family_dict['members'].append(person_2)
family_dict['members'].append(person_3)
family_dict['members'].append(person_4)
family_dict['members'].append(person_5)

#%%
family_dict['members'][2]['hobbies'] = ['Chess', 'Walking']

#%%
family_dict



# %%
family_dict['members'][2]['hobbies'][1]
# %%
