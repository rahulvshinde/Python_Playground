#import random
#import string
#chars = string.ascii_letters + string.ascii_digits
#pass = ''.join(string.choice(chars) for i in range(20))


import string
import random

def randompassword():
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  size = random.randint(8, 12)
  return ''.join(random.choice(chars) for x in range(size))

print(randompassword())
