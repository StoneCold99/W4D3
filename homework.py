#code wars / time and space 

#  --------Count characters in your string--------
# The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.
#What if the string is empty? Then the result should be empty object literal, {}.
def count(string):
    return {c:string.count(c) for c in string}
    # Time = Quadratic
    # Space = Linear


#  --------Multiples of 3 or 5---------------
#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Finish the solution so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
#Additionally, if the number is negative, return 0.
def solution(number):
    result = []
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            result.append(i)

    return sum(result)
    # Time = Linear
    # Space = Constant


#  ----------Ones and Zeros--------------
#Given an array of ones and zeroes, convert the equivalent binary value to an integer.
#Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.
def binary_array_to_number(arr):
    return int("".join([str(i) for i in arr]), 2)
    # Time = Linear
    # Space = Constant


