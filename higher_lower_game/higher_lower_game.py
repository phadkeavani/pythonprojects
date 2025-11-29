import art
import game_data
import random

def clear_screen():
    print("\n" * 20)

def print_ascii_art(art_name):
    print(art_name)

def fetch_entry():
    return random.choice(game_data.data)
def verify_answer(ans, entry_a, entry_b):
    if ans == 'a':
        return entry_a["follower_count"] > entry_b["follower_count"]
    else:
        return entry_b["follower_count"] > entry_a["follower_count"]

def form_a_compare_statement(a_or_b, entry):
    if a_or_b == 'a':
        suffix = 'Compare A: '
    else:
        suffix = 'Against B: '

    return suffix + entry["name"] + ", " + entry["description"] + ", from " + entry["country"]

def play_game(next_round):
    entry_1 = {}
    winner = False
    score = 0
    while next_round:
        print_ascii_art(art.logo)
        if entry_1 == {}:
            entry_1 = fetch_entry()
        if winner:
            print(f"You're right! Current score: {score}")
        print(form_a_compare_statement('a', entry_1))
        print_ascii_art(art.vs)
        entry_2 = fetch_entry()
        while entry_1 == entry_2:
            entry_2 = fetch_entry()
        print(form_a_compare_statement('b', entry_2))
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        winner = verify_answer(answer, entry_1, entry_2)
        if winner:
            score += 1
            if answer == 'b':
                entry_1 = entry_2
            clear_screen()
        else:
            clear_screen()
            print_ascii_art(art.logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            next_round = False

play_game(True)



