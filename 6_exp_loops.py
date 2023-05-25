#%%
from math import pi, pow
diameters_list = [10, 20, 30, 40]

circle_sizes = []

for diameter in diameters_list:
    radius = diameter / 2
    size = pow(radius, 2) * pi
    circle_sizes.append(size)

# %%
for idx, diameter in enumerate(diameters_list):
    print(idx)
    print(diameter)

# %%
under_age = []
ages_list = [11, 45, 78, 39, 114, 90, 17]

for age in ages_list:
    if age < 18:
        under_age.append(age)
# %%
[age for age in ages_list if age < 18]
# %%
names_list = ["arie", "dirk", "jaap", "gert", "arnold"]

names_list_new = [name.capitalize().replace("a", "😞") for name in names_list]
names_list_new
# %%
