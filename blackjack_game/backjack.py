import random
import art
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
start_game = 'y'

def draw_card():
    return random.choice(cards)

def calculate_total(card_list):
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    if sum(card_list) == 21 and len(card_list) == 2:
        return  0
    return sum(card_list)

def result(cm_score, us_score):
    if us_score == 0:
        return "Win with a Blackjack 😎"
    elif cm_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif us_score > 21:
        return "You went over. You lose :("
    elif cm_score > 21:
        return "Opponent went over. You win! :)"
    elif cm_score == us_score:
        return "Draw! :-"
    elif cm_score < us_score:
        return "You won! :)"
    else:
        return "You lose! :("

while start_game == 'y':
    user_cards = []
    computer_cards = []
    user_score = 0
    computer_score = 0
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
    if start_game == 'y':
        print("\n" * 20)
        print(art.logo)
        for c in range(2):
            user_cards.append(draw_card())
            computer_cards.append(draw_card())
        round_number = 0
        another_card = 'y'
        while another_card == 'y':
            if round_number > 0:
                user_cards.append(draw_card())
            user_score = calculate_total(user_cards)
            if user_score == 0 or user_score > 21:
                another_card = 'n'
            else:
                print(f"Your cards: {user_cards}, current score: {user_score}")
                print(f"Computer's first card: {computer_cards[0]}")
                round_number += 1
                another_card = input("Type 'y' to get another card, type 'n' to pass:").lower()
        computer_score = calculate_total(computer_cards)
        while computer_score > 0 and computer_score < 17:
            computer_cards.append(draw_card())
            computer_score = calculate_total(computer_cards)

        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(result(computer_score, user_score))

