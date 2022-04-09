def get_input(trial_number):
    return (f"enter the guess #{trial_number}: ").lower()
def congratulate():
    print("congratulations..!!")
def warn_repeat_word():
    print("Word already guessed, try again!")
def warn_word_length(expected_length):
    print(f"only {expected_length}letters allowed only!")
def warn_incorrect_letters():
    print("The word only contain alphabet letters!")
def warn_max_attempts(num_attempts):
    print("fail to guess in 6 tries, better luck next time")
def print_mismatch(appraisal):
    print(" " * 18 + "---" +appraisal+ "---")
