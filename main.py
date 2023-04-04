from game_data import data
from art import logo, vs
import random
# from replit import clear()

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account['name']
    description = account['description']
    country = account['country']
    return f"Compare A: {name}, a {description}, from {country}"


def check_answer(a_followers, b_followers, answer):
    """Checks followers against user's guess
      and returns True if they got it right.
      Or False if they got it wrong."""
    if a_followers > b_followers:
        return answer == 'A'
    else:
        return answer == 'B'

def game():
    score = 0
    account_b = get_random_account()
    game_over = False

    print(logo)
    while not game_over:
        account_a = account_b
        account_b = get_random_account()

        while account_a == account_b:
            account_b = get_random_account()

        # print(f"Account A = {account_a['follower_count']}, Account B = {account_b['follower_count']}")
        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        answer = input("Who has more followers? Type 'A' or 'B': ").upper()

        a_follower = account_a['follower_count']
        b_follower = account_b['follower_count']
        is_correct = check_answer(a_follower, b_follower, answer)

        # clear()
        print(logo)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")s
        else:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True

# Play game
game()

'''
FAQ: Why does choice B always become choice A in every round, even when A had more followers? 

Suppose you just started the game and you are comparing the followers of A - Instagram (364k) to B - Selena Gomez (174k). Instagram has more followers, so choice A is correct. However, the subsequent comparison should be between Selena Gomez (the new A) and someone else. The reason is that everything in our list has fewer followers than Instagram. If we were to keep Instagram as part of the comparison (as choice A) then Instagram would stay there for the rest of the game. This would be quite boring. By swapping choice B for A each round, we avoid a situation where the number of followers of choice A keeps going up over the course of the game. Hope that makes sense :-)
'''
