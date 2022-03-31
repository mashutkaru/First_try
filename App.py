# This is a guessing_word game. I would like to add an ability to give a player indication regarding number of letters, and in case they've guessed some letters right, and their location. **

secret_word = "home"
guess_word = ""
count_try = 0
count_limit = 3
out_of_tries = False

while guess_word != secret_word and not(out_of_tries):
    if count_try < count_limit:
        guess_word = input("Guess a word: ")
        count_try +=1
    else:
        out_of_tries = True
if out_of_tries:
    print("You lo se")
else:
    print("You win")
