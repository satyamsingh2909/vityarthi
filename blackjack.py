import random
from art import text2art

print(text2art("logo"))

def deal_Card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card=random.choice(cards)
    return card
def calculate_score(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)>21:
        cards.remove(11)
        cards.append(11)
    return sum(cards)
def compare(user_score,computer_score):
    if user_score==computer_score:
        return "Draw"
    elif computer_score==0:
        return "Computer win,Blackjack"
    elif user_score==0:
        return ("You win,Blackjack")
    elif user_score>21:
        return ("You Lose")
    elif computer_score>21:
        return ("You Win")
    elif user_score>computer_score:
        return ("You win")
    elif computer_score>user_score:
        return ("You lose")

def game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over=False
    for _ in range(2):
        user_cards.append(deal_Card())
        computer_cards.append(deal_Card())
    while not is_game_over:
        user_score=calculate_score(user_cards)
        computer_score=calculate_score(computer_cards)
        print(f"    Your Cards:{user_cards},current score:{user_score}\n    Computer's First Card:{computer_cards[0]}")

        if user_score==0 or computer_score==0 or user_score>21:
            is_game_over=True
        else:
            user_should_deal = input("Type 'y' to get another card,type 'n' to pass: ")
            if user_should_deal=="y":
                user_cards.append(deal_Card())
            else:
                is_game_over=True
    while computer_score!=0 and computer_score<17:
        computer_cards.append(deal_Card())
        computer_score=calculate_score(computer_cards)
    print(f"    Your Final hand:{user_cards},current score:{user_score}\n    Computer's Final Hand:{computer_cards},Computer's Score:{computer_score}")
    print(compare(user_score,computer_score))
end_game=False
logo = r"""
  __      __  
 /  \    /  \ 
 \   \/\/   / 
  \        /  
   \__/\__/   
"""

print(logo)

while not end_game:
    start_again=input("Do you want play again yes 'y' or no 'n'?")

    if start_again=="y":
        game()
    elif start_again=="n":
        end_game=True
    else:
        print("invalid key")
