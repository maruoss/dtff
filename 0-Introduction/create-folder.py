# This script creates a folder in the RESEARCH_PATH environment variable, with
# the folder name being given by user input

# %%
import os

# %%
# Set environment variable manually ONLY FOR THIS SESSION (will not change system-wide env. variables!)
# os.environ["RESEARCH_PATH"] = r"C:\Users\Mathiass\Documents\Projects"

# %%
# Check for RESEARCH_PATH
if os.environ.get("RESEARCH_PATH") is not None:
    print("Reading in RESEARCH_PATH variable...")
else:
    raise TypeError("RESEARCH_PATH is not set. Please specify this environment variable in your system")

# %%
# Get environment variable from os
research_path = os.environ.get("RESEARCH_PATH")

# %%
# Name of folder to create has to be specified by user
folder_name = input("Enter folder name: ")

# Join directory and folder name to a path
path = os.path.join(research_path, folder_name)

# %%
# Try to make folder, else print out error in a cleaner way
try: 
    os.mkdir(path)
    print(f"Folder {folder_name} has been created in directory {research_path}")
except OSError as error: 
    print(error)  



# %%
