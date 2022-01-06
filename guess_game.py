#Simple guess game for predicting the right number in four tries.

secret_number = 7
guess_count = 0
guess_limit = 4
while guess_count < guess_limit:
    guess = int(input('Can you guess the correct number? '))
    guess_count += 1
    if guess == secret_number:
        print('Thats correct! You won.')
        break
else:
    print("Sorry you lost!")