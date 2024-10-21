"""Blackjack project."""
import random

from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def result(player_cards, computer_cards) -> str:
    """Generic Result on Blackjack"""
    if sum(computer_cards) < 21 and sum(player_cards) < 21:
        return ""
    if sum(computer_cards) == 21 and sum(player_cards) < 21:
        return "Lose, opponent has Blackjack 😱 "
    if sum(player_cards) == 21:
        return "You win 😊"
    if sum(player_cards) > 21:
        return "You went over. You lose 😭"
    if sum(computer_cards) == 21:
        return "You lose 😭"
    if sum(computer_cards) > 21:
        return "Opponent went over. You win 😁"
    if sum(computer_cards) > 17 and sum(player_cards) > 17:
        if sum(computer_cards) > sum(player_cards):
            return "You lose 😭"
        elif sum(computer_cards) < sum(player_cards):
            return "You win 😊"
        elif sum(computer_cards) == sum(player_cards):
            return "Draw 🙃"
    return ""


def blackjack() -> None:
    """Blackjack game algorithm."""
    result_string = ""
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if choice == "y":
        print(logo)
        player_cards = list(random.choices(cards, k=2))
        computer_cards = list(random.choices(cards, k=2))
        while not sum(player_cards) < 21 or not sum(computer_cards) < 21:
            player_cards = list(random.choices(cards, k=2))
            computer_cards = list(random.choices(cards, k=2))
        print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
        print(f"Computer's first card: {computer_cards[0]}")
        result_string = result(player_cards, computer_cards)
        while sum(player_cards) < 21 and result_string != "Draw" and sum(computer_cards) < 21:
            if result_string == "":
                another_card = input("Type 'y' to get another card, type 'n' to pass: ")
                if another_card == "y":
                    next_player_card = random.choice(cards)
                    play_card = 1 if sum(player_cards,
                                         next_player_card) >= 21 and next_player_card == 11 else next_player_card
                    player_cards.append(play_card)
                    print(f"Your cards: {player_cards}, current score: {sum(player_cards)}")
                    print(f"Computer's first card: {computer_cards[0]}")
                else:
                    while sum(computer_cards) < 21:
                        next_comp_card = random.choice(cards)
                        comp_card = 1 if sum(computer_cards,
                                             next_comp_card) >= 21 and next_comp_card == 11 else next_comp_card
                        computer_cards.append(comp_card)
                result_string = result(player_cards, computer_cards)
        print(result_string)
        print(f"Your final cards: {player_cards}, final score: {sum(player_cards)}")
        print(f"Computer's final card: {computer_cards}, final score: {sum(computer_cards)}")
        blackjack()


blackjack()
