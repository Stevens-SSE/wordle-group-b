dictionary_File = "words.txt"
Word_Length = 5


def read_words(word_length=Word_Length) -> str:
    """

     :rtype: object
     """
    file = open(dictionary_File, "r")
    dictionary_list = []
    for word in file:
        word = word.strip()
        if len(word) == Word_Length:
            dictionary_list.append(word)
    return dictionary_list
