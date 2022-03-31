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
