def fizzBuzz(n):
	for num in xrange(1,n+1):
		if num%5 == 0 and num%3 == 0:
			print "FizzBuzz"
		elif num%5 == 0:
			print "Fizz"
		elif num%3 == 0:
			print "Buzz"
		else:
			print num
fizzBuzz(100)


