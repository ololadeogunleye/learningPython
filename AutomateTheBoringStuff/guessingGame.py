from random import randint
print("hi you have 10 chances to guess my secret number")
secretNumber = randint(0, 101)
for i in range(1,10):
    guess= int(input('Guess my secret Number:'))
    if guess < secretNumber:
        print("Your guess is less than my secret number")
    elif guess > secretNumber:
            print("Your guess is greater than my secret number")
    else:
        break
    print("you have "+ str(10-i)+ "Guesses left")
print('You guessed  correctly ')
    
    