from art import logo, vs
from game_data import data
import random

score = 0
print(logo)


def play(a_opt, b_opt):
    global score
    print(a_opt)
    print(b_opt)
    print(f"Compare A: {a_opt['name']}, a {a_opt['description']}, from {a_opt['country']}")
    print(vs)
    print(f"Compare B: {b_opt['name']}, a {b_opt['description']}, from {b_opt['country']}")
    ans = input("Who has more followers? Type 'A' or 'B' :")
    correct = "A" if a_opt['follower_count'] > b_opt['follower_count'] else "B"
    if ans == correct:
        score = score + 1
        print(f"Correct! Your score is {score}")
        print("**********************************")
        play(b_opt, random.choice(data))
    else:
        print(f"You lost. Final score is {score}")


a = random.choice(data)
b = random.choice(data)
play(a, b)
