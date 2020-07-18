def fizzBuzz(n):
    for num in range(11,n+1):
        msg = ''
        if num%5 == 0:
            msg += "Fizz"
        if num%3 == 0:
            msg += "Buzz"
        if not msg:
            msg += str(num)
        print(msg)
fizzBuzz(100)