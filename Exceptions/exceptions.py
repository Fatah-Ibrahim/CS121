# expections explained

'''try:
    block of code
    ...
    ...
    # if something "goes wrong" in here, and error will be raised
    # ans sent to the except statement

except (similar to a if statement):
    block of code
    ...
    ...
except NameError:
    # handle this type of error
    print('this is a name error')
except ValueError:
    print('this is a value error')
except TypeError:
    print('this is a type error')'''

# eg.1
'''print("Starting program")

try:
    age = int(input('What is your age?: '))

    print(f'Your age is {age}')
    print(f'Next your your age is {age+ 1}')
except ValueError:
    print('you must pick an integer age.')

print("Your program ended normally")'''

# eg.2

print('enter a number. I will divide that number by 10, and output the result')
user_input = input("your number: ")

done = False



while not done:
    try:
        user_number = int(user_input)
        result = 10 / user_number
        print(f'the result is {result}')
        done = True
    except ValueError:
        print('Your must pick a integer')
        user_input = input("your number: ")
    except ZeroDivisionError:
        print("Undefined. \nDon't pick 0")
        user_input = input("your number: ")
    except Exception:
        print('Something went wrong')
