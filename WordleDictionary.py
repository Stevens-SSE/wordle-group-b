# importing the module
import os

dictionary_File = "words.txt"
def read_words(word_length=Word_Length) -> str:
    """
     :rtype: object
     """
    file = open(dictionary_File, "r")
    filename = 'words.txt'
    try:
        with open(filename) as f_obj:
            contents = f_obj.read()
    except FileNotFoundError:
        msg = "Sorry, the file " + filename + "does not exist."
        print(msg)  # Sorry, the file words.txt does not exist.
    return dictionary_File

