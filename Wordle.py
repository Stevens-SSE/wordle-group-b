WORD = 'SONAR' #this word user have to guess
GUESS_WORD = list(WORD)

def word_check(user):
    return user.lower() == WORD.lower()

def get_instance(spot_word):
    if spot_word:
        if spot_word == 'invalid':
            return 'the Alphabet is not on spot'

        return 'the Alphabet is perfectly on spot'

    return 'the Alphabet is on Incorrect spot'


def alpha_check(user):
    arr = list(user)
    result = []
    for i in range(len(WORD)):
        value = arr[i].upper()
        if value not in GUESS_WORD:
            result.append('invalid')
            continue
        if value != GUESS_WORD[i]:
            result.append(False)
            continue
        result.append(True)

    for i in range(len(WORD)):
        final = result[i]
        user_value = user[i]

        print('%s -> %s'%(user_value, get_instance(final)))

def main():
    count_word = 0
    while count_word < 6:
        user = input('Please Enter a word: ')
        if len(user) != 5:
            print('only 5 Alphabetic words are allowed')
            continue
        if word_check(user):
            print('Congratulations..!words are matched.')
            break

        alpha_check(user)
        count_word += 1

if __name__ == "__main__":
    main()