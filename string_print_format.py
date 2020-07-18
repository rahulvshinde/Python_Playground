# Formatting with .format() method
# A good way to format objects into your strings for print statements in with the string .format() method.

print("This is a String {}".format("INSERTED"))

print("The {} {} {}".format("fox", "brown", "quick"))

print("The {2} {1} {0}".format("fox", "brown", "quick"))

print("The {q} {f} {b}".format(f="fox", b="brown", q="quick"))
########################################################################################

# Float formatting follows "{value:width.precision f}"

result = 100 / 777

print("The result was {}".format(result))

print("The result was {r:1.3f}".format(r=result))
########################################################################################

# fstring method

name = "Rahul"

print("Hello, My name is {n}".format(n=name))

print(f"Hello, My name is {name}")
########################################################################################

# Additional Examples

# Within the curly braces you can assign field lengths, left/right alignments, rounding parameters and more

print('{0:8} | {1:9}'.format('Fruit', 'Quantity'))
print('{0:8} | {1:9}'.format('Apples', 3.))
print('{0:8} | {1:9}'.format('Oranges', 10))

# By default, .format() aligns text to the left, numbers to the right. You can pass an optional <,^, or > to set a
# left, center or right alignment:

print('{0:<8} | {1:^8} | {2:>8}'.format('Left','Center','Right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11,22,33))

# You can precede the alignment operator with a padding character

print('{0:=<8} | {1:-^8} | {2:.>8}'.format('Left','Center','Right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11,22,33))

