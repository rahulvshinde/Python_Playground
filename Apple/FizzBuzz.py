"""
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
"""


n = 15
def fizzbuzz(nums):
    for num in range(1,nums+1):
        msg = ''
        if num%3 == 0:
            msg += "Fizz"
        if num%5 == 0:
            msg += "Buzz"
        if not msg:
            msg += str(num)
        print(msg)

print(fizzbuzz(n))