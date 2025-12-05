


def is_odd(num):
    if num % 2 == 0:
        return False
    else:
        return True
    
def is_pos(num):
    if num > 0:
         return False
    else:
        return True
    
def is_odd_and_positive(num):
    if is_odd(num) and is_pos(num):
       return True
    else:
        return False
    

def wacky_fctn(num):
    print(num)
    if num > 25:
        return num
    return wacky_fctn(num + 1)

print(wacky_fctn(10))

def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
    
# print(factorial(5))

def fib(num):
    if num == 0 or num == 1:
        return 1
    else:
        return fib(num - 1) + fib(num -2)
    

print(fib(5))