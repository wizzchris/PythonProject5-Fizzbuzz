
import FizzBuzzChecks as fb

print('Welcome to the game of fizz buzz. Play with the computer')
number = 1
while True:
    guess = input('What number is next? Type HELP for rules. EXIT to end. RESTART to restart. ----------').strip().upper()
    if guess == '0':
     print('The number starts at 1')

    elif guess.isnumeric() == True:
        if fb.check3(guess) == 0:
            print('Sorry, you lost, try again')

        elif fb.check5(guess) == 0:
            print('Sorry, you lost, try again')

        elif guess == str(number):
            number += 1

    elif guess.isnumeric() == False:
        if guess == 'HELP':
            print('Add 1 to the previous number, and if the number is a multiple of 3 say FIZZ\n and if it is a multible of 5 type BUZZ.\n The number starts at 0')

        elif guess == 'EXIT':
            break

        elif guess == 'RESTART':
            guess = 1

        elif guess == 'FIZZ':
            if fb.check3(number) > 0:
                print('Sorry thats wrong, guess again')

            else:
                number += 1

        elif guess == 'BUZZ':
            if fb.check5(number) > 0:
                print('Sorry thats wrong, guess again')

            else:
                number += 1

        else:
            print('Sorry that is not a valid guess')

print('This allows you to check a number to see if it is fizz or buzz')

while True:
    user_number = input('What number do you want to check? Type EXIT to exit -----')
    if user_number.isnumeric() == False:
        if user_number.strip().lower() == 'exit':
            break

        else:
            print('Not valid')

    elif user_number.isnumeric() == True:
        user_number = int(user_number)
        if fb.check3(user_number) == 0 and fb.check5(user_number) == 0:
            print('Fizzbuzz')

        elif fb.check3(user_number) == 0:
            print('Fizz')

        elif fb.check5(user_number) == 0:
            print('Buzz')

        else:
            print(user_number, 'is not fizz or buzz')