#%%
import os

#%%
folder_names = input("Insert the names of the folders (seperate by ' '):\n")
folder_names_list = folder_names.split(" ")

# %%
current_files_folders = os.listdir()

for folder in folder_names_list:
    if folder not in current_files_folders:
        os.mkdir(folder)
        print(f"Created folder {folder}")
    else:
        print(f"Folder {folder} already exists")

# %%
