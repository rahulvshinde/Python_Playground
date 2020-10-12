name = input("What is your name? ")
age = int(input("What is your age? "))
city = input("Where do you live? ")
hobby = input("What is your hobby? ")

print("My name is {n}, I'm {a} years old. I live in {c} "
      "and I like to play {h}.".format(n=name, a=age, c=city, h=hobby))
