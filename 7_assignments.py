# Assignment 1: Define a function that returns the contents (e.g. in m3) of a box. 
# It takes 3 parameters: (1) Length, (2) width and (3) heigth
##############
#%%
def calc_volume(length: float, width: float, height:float) -> float:
    '''
    Calculates the volume of a box

    Parameters:
    * length
    * height
    * width

    Returns:
    * content
    '''
    content = length * height * width

    return content

#%%
calc_volume(3, 5, 10)


# %%
from typing import List
# Assignment 2: Define a function that accepts a lists, capitalizes every name in the list, and retuns this capitalized list. 
# You can use: ['Jim', 'John', 'Marc', 'Danny', 'Peter']
###############

def capitalize_names(names_list: list) -> List:
    '''
    Function that capitalizes each name in a list

    Parameters:
    * names_list

    Returns:
    * names_list_capitalized
    '''

    names_list_capitalized = []

    for name in names_list:
        name_capitalized = name.capitalize()
        names_list_capitalized.append(name_capitalized)
