#%%
import os

current_file = "my_script.py"
current_files_folders = os.listdir()

if current_file in current_files_folders:
    file_exists = True
else:
    file_exists = False

#%%
if file_exists:
    print("Doe er iets mee")