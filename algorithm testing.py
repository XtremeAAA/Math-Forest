import random

coefficient = random.randint(1, 10)
constant_1 = random.randint(5, 20)
constant_2 = random.randint(40, 80)
score = 0

x = (constant_2 - constant_1) / coefficient

x_2dp = round(x, 2)

question_text = f"{coefficient}x + {constant_1} = {constant_2}. What is x?"
print(question_text)
user_answer = int(input("Answer: "))


if user_answer == x_2dp:
    score + 1
    print(f"Correct! The answer is {x_2dp}.")
else:
    print(f"Incorrect. The correct answer is {x_2dp}.")
