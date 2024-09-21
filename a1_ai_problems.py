# Complete your individualized AI problems here
# from chatGPT

# def fizbuzz(input_num):
#     if(input_num%3==0):
#         if(input_num%5==0):
#             return 'FizzBuzz'
#         return 'Fizz'
#     elif(input_num%5==0):
#         return 'Buzz'
#     else:
#         return input_num

# assert fizbuzz(1) == 1, "fizzbuzz 1 test"
# assert fizbuzz(3) == "Fizz", "fizzbuzz 3 test"
# assert fizbuzz(4) == 4, "fizzbuzz 4 test"
# assert fizbuzz(5) == "Buzz", "fizzbuzz 5 test"
# assert fizbuzz(6) == "Fizz", "fizzbuzz 6 test"
# assert fizbuzz(15) == "FizzBuzz", "fizzbuzz 15 test"

### 1. **Fibonacci Sequence**
def fibonacci(n):
    fib_sequence = []
    a,b = 0,1 # starting values
     
    while a <=n:
        fib_sequence.append(a)
        a,b = b, a+b
    return fib_sequence

assert fibonacci(0) == [0], "Test case for n=0 failed"
assert fibonacci(1) == [0, 1, 1], "Test case for n=1 failed"
assert fibonacci(20) == [0, 1, 1, 2, 3, 5, 8, 13], "Test case for n=20 failed"
assert fibonacci(-1) == [], "Test case for n=-1 failed"  # No Fibonacci numbers below 0
print("All fibonacci tests passed!")

### 2. **Palindrome Checker**
def palindrome(s: str):
    s = s.lower()
    length = len(s)
    half = length // 2
    if length%2 == 0:
        str1 = s[0:half]
        str2 = s[half:]
    else:
        str1 = s[0:half+1]
        str2 = s[half:]
    #for i in range (len(str2)//2):
        #java way
        # holder = str2[i]
        # last = len(str2) - 1 - i
        # str2[i] = str2[last]
        # str2[last] = holder
        #pythonic way
    str2 = str2[::-1]
    return str1 == str2
assert palindrome("racecar") == True, "Test case for 'racecar' failed"
assert palindrome("12321") == True, "Test case for '12321' failed"
assert palindrome("12345") == False, "Test case for '12345' failed"
assert palindrome("Step on no pets") == True, "Test case for 'Step on no pets' failed"
print("All palindrome tests passed!")

### 6. **Anagram Checker**

### 7. **Caesar Cipher**

### Bonus Challenge: **Tic-Tac-Toe**