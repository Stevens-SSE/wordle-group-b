import random

from hw03_jaiminkumarbhupeshkumar_desai_ui import *
from hw03_jaiminkumarbhupeshkumar_desai_dictionary import *

Max_Attempt: int = 6  # how many attempts allowed
EXPECTED_WORD_LENGTH = 5

given_word: list = []
input_word = "___"

possible_words = read_words()

while input_word != "":
    expected_word = random.choice()
    given_word.clear()
    attempt: int = 1

    while attempt <= Max_Attempt:

        input_word = get_input(attempt)

        if input_word == expected_word:
            congratulate()
            break

        if input_word in given_word:
            warn_repeat_word()
            continue

    if len(input_word) != EXPECTED_WORD_LENGTH:
        warn_word_length(len(expected_word))
        continue

    if not input_word.isalpha():
        warn_incorrect_letters()
        continue

    attempt += 1
    given_word.append(input_word)

    letter_count: dict = {}
    appraisal = []

    for letter in expected_word:
        if letter in letter_count.keys():
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1

    for index in range(EXPECTED_WORD_LENGTH):
        if input_word[index] == expected_word[index]:
            appraisal.append(' ')
            letter_count[expected_word[index]] -= 1
        else:
            appraisal.append('"')

    for index in range(EXPECTED_WORD_LENGTH):
        if input_word[index] != expected_word[index] and input_word[index] in letter_count:
            if letter_count[input_word[index]] > 0:
                letter_count[input_word[index]] -= 1
                appraisal[index] = "'"

        print_mismatch(''.join(appraisal))

    else:
        warn_max_attempts(Max_Attempt)
