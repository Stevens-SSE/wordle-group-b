import collections
import random
import logging
import string
from collections import  OrderedDict

class wordle:
    # of get() and set() method in
    # normal function

    def __init__(self, words=5):
        self.word = words
        return self.word

    # getter method

    def get_words(self,wordle):
        print("getter method")
        self.word = wordle
        return self.word

    # setter method

    def set_words(self, wordle):
        print("setter method")
        self.word = wordle
        return self.word

    def valid_words(self):
        with open('words.txt', 'r+') as f_pointer:
            content = f_pointer.read().split('\n')
            f_pointer.close()
            words = []
            for word in content:
                if len(word) != 5:
                    continue
                words.append(word)
            return words

    def words_list_to_file(list):
        with open('valid_words.txt', 'w') as f_pointer:
            f_pointer.writelines([str(i) + '\n' for i in list])
            try:
                with open(filename) as f_pointer:
                    contents = f_pointer.read()
            except FileNotFoundError:
                msg = "Sorry, the file " + f_pointer + "does not exist."
                print(msg)  # Sorry, the file John.txt does not exist.
            f_pointer.close()

    def order(trials, user_input):  # function making file for storing in csv
        letter_list = OrderedDict()
        alphabet = [str(i) for i in 'abcdefghijklmnopqrstuvwxyz']  # comparing every to every letters
        for letter in alphabet:
            letter_list[letter] = [0, 0, 0, 0, 0]  #all index frequency
        while trials > 0:
            user_input = input('Enter a word: ')  #each nd every trials
            for index in range(len(user_input)):
                temp = letter_list[user_input[index]]
                index = index + 1
            trials -= 5
            for letter in letter_list:
                different_letters = ('%s -> %s' % (letter, letter_list[letter]))  # seperate letter and occurence

            with open('letterFrequency.csv', 'w') as csv_files:  # adding in csv files
                writer = csv.DictWriter(csv_files, fieldnames=letter_list.keys())  # writing into csv files the letters
                # and occurance
                writer.writeheader()
                writer.writerows(letter_list)  # outputs
                try:
                    with open(filename) as csv_files:
                        contents = csv_files.read()
                except FileNotFoundError:
                    msg = "Sorry, the file " + csv_files + "does not exist."
                    print(msg)  # Sorry, the file John.txt does not exist.
                    csv_files.close()

    def get_input_from_user(trial):
        prompt_message = 'Enter a word: ' if trial > 5 else 'Reenter a word: '
        return input(prompt_message)

    def check_if_entered_word_is_valid(word):
        return word.isalpha() and len(word) == 5


    def has_user_guessed_the_right_word(word, codeword):
        return word == codeword

    def log_to_file(level, message):
        logging.basicConfig(filename='app.log', filemode='a+', format='%(levelname)s - %(message)s', level=logging.DEBUG)
        if level == 'info':
            logging.info(message)
        elif level == 'error':
            logging.error(message)
        else:
            logging.warning(message)

    def get_spot_name(spot_val):
        if spot_val:
            if spot_val == 'NA':
             return '"'

            return ''

        return '`'


    def position_check_for_letters(user_input, codeword):
        arr = list(user_input)
        code_arr = list(codeword)
        result = []
        for letter_index in range(len(codeword)):
            user_word_letter = arr[letter_index]
            if user_word_letter not in code_arr:
                result.append('NA')
                continue
            if user_word_letter != code_arr[letter_index]:
                result.append(False)
                continue
                result.append(True)

                return result


def validate_letter_position(positions, user_input):
    for i in range(len(positions)):
        decider = positions[i]
        user_char = user_input[i]
        print('%s%s' % (user_char, get_spot_name(decider)))

def get_word():
    with open('words.txt', 'r+') as file_pointer:
        content = file_pointer.read().split('\n')
        random_word = content[random.randint(0, len(content) - 1)]
        word = random_word if len(random_word) > 0 and len(random_word) == 5 else get_word()
        file_pointer.close()
        log_to_file('info', 'got files from words.txt!!!')
        return word

def find_words(self, words):
    words_list = collections.deque()
    Rows_count = 0
    if (wordle != ""):
        List = open("words.txt", "r+")
        Rows = List.read().splitlines()
        for line in Rows:
            if words in Rows:
                list.append(Rows_count)
            print(list)
        else:
            words_list = open("words.txt", "r+")
            for i in range(50):
                line = List.read().splitlines()
                words_list.append(Rows_count)
            print(words_list)
            try:
                with open(filename) as line:
                    contents = line.read()
            except FileNotFoundError:
                msg = "Sorry, the file " + line + "does not exist."
                print(msg)  # Sorry, the file John.txt does not exist.
                line.close()

def match_word_alphabets(words, word_alphabet):
    assert len(words) == len(word_alphabet)
    for letter, words in zip(word, word_alphabet):
        if letter not in words:
            return False
    return True

def solve():
    possible_words = WORDS.copy()
    word_alphabet = [set(string.ascii_lowercase) for _ in range(WORD_LENGTH)]
    for attempt in range(1, ALLOWED_ATTEMPTS + 1):
        print(f"Attempt {attempt} with {len(possible_words)} possible words")
        display_word_table(sort_by_word_commonality(possible_words)[:15])
        word = input_word()
        response = input_response()
        for idx, letter in enumerate(response):
            if letter == "G":
                word_alphabet[idx] = {word[idx]}
            elif letter == "Y":
                try:
                    word_alphabet[idx].remove(word[idx])
                except KeyError:
                    pass
            elif letter == "?":
                for vector in word_alphabet:
                    try:
                        alphabet.remove(word[idx])
                    except KeyError:
                        pass
        possible_words = match(word_alphabet, possible_words)

def check_if_word_in_dictionary(word):
    with open('words.txt', 'r+') as file_pointer:
        content = file_pointer.read().split('\n')
        is_word_present = word in content
        try:
            with open(filename) as file_pointer:
                contents = file_pointer.read()
        except FileNotFoundError:
            msg = "Sorry, the file " + file_pointer + "does not exist."
            print(msg)  # Sorry, the file John.txt does not exist.
        file_pointer.close()
        log_to_file('info', 'word is in the file')
        return is_word_present

def assess_word(self, test_word):

        target = list(self.target_word)
        matched_counts = defaultdict(int)
        rules = [None] * self.word_length
        # Test test_word for the "exact match" and "excluded letter" rules.
        for i, letter in enumerate(test_word):
            if letter == target[i]:
                rules[i] = RuleMatch(letter, i)
                target[i] = '*'
                matched_counts[letter] += 1
            elif letter not in target:
                rules[i] = RuleExcludedLetter(letter, i)

        for i, letter in enumerate(test_word):
            if rules[i]:
                continue
            if letter in target:
                # NB exact matches have already been filtered out.
                rules[i] = RuleContainsElsewhere(letter, i)
                target[target.index(letter)] = '*'
                matched_counts[letter] += 1
            else:
                rules[i] = RuleExcludedLetter(letter, i)

        rule_str = ''.join(rule.code for rule in rules)
        return rules, matched_counts, rule_str

def __str__(self):
    return 'a {self.words}wordle'


if __name__=='__main__':
    game=WordleGame()
    print(game.__str__())
