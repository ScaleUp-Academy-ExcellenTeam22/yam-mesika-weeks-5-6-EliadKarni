import os
"""
That's the way.
By: Eliad Karni.

The project receive a file path from the user and prints a list of the file in the received directory,
which their names starts with PREFIX value.

used websites help:
os usage: Stuck Overfolw -> https://stackoverflow.com/questions/2759323/how-can-i-list-the-contents-of-a-directory-in-python.
"""
#------------------------------- consts section -------------------------------
PREFIX = "deep"

#------------------------------ function section ------------------------------
def get_files_list(path:str):
    """
    The function receives a directory path, and returns a list of
    file in the directory which their names starts with PREFIX (const value).
    :param path
    :return list of files in directory which their name starts with PREFIX.
    """
    return [file for file in os.listdir(path) if file.startswith(PREFIX)]

#-------------------------------- main section --------------------------------
print(get_files_list(input("please enter dir path: ")))