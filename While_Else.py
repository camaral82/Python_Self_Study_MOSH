#create a secret number
secret_number = 9
guess_count = 0
guess_limit = 3

#WHILE com ELSE -> nesse caso, se nao entra no IF - BREAK

while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count += 1
    if guess == secret_number:
        print("You won!")
        break
else:
    print('Sorry, you failed :( ')