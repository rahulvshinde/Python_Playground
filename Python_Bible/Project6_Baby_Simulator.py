from random import choice

questions = ["Why is the sky blue? ","Why is the earth round? ","Why cars don't fly? "]
question = choice(questions)
answer = input(question).strip().lower()
while answer != "just because":
    answer = input("why? ").strip().lower()
