sentence = input("Enter" ).lower()

words = sentence.split()
pig_latin = []
conv = ""
for word in words:
    if word[0] not in "aeiou":
        vowel_pos = 0
        cons = ""
        rest = ""
        for letter in word:
            if letter not in "aeiou":
                vowel_pos +=1
            else:
                break
        word = word.title()
        cons = word[:vowel_pos]
        rest = word[vowel_pos:]
        conv = rest + cons + "ay"
        # pig_latin.append(conv)
    else:
        conv = word + "yay"
    pig_latin.append(conv)
output = " ".join(pig_latin)
print(output)