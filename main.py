import random
from art import logo


def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


end_game = False
while not end_game:
    will_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")
    if will_play == "y":
        print(logo)
        user_hand = []
        computer_hand = []
        for i in range(2):
            user_hand.append(deal_cards())
            computer_hand.append(deal_cards())

        sum_user_hand = user_hand[0] + user_hand[1]
        com_first_card = computer_hand[0]
        print(f"Your cards: {user_hand}, current score: {sum_user_hand}")
        print(f"Computer's first card: {com_first_card}")

        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "y":
            user_hand.append(deal_cards())
            new_sum_user_hand = sum_user_hand + user_hand[2]
            computer_hand.append(deal_cards())
            sum_computer_hand = computer_hand[0] + computer_hand[1] + computer_hand[2]
            print(f"Your cards: {user_hand}, current score: {new_sum_user_hand}")
            print(f"Computer's first card: {com_first_card}")
            print(f"Your final hand: {user_hand}, final score: {new_sum_user_hand}")
            print(f"Computer's final hand: {computer_hand}, final score: {sum_computer_hand}")
            if new_sum_user_hand == sum_computer_hand:
                print("You draw!")
            elif new_sum_user_hand > sum_computer_hand and new_sum_user_hand < 22:
                print("You Win!")
            elif 21 < new_sum_user_hand:
                print("You went over. You lose")
            else:
                print("You lose")

        elif another_card == "n":
            sum_com_hand = computer_hand[0] + computer_hand[1]
            if sum_com_hand < 15:
                computer_hand.append(deal_cards())
                new_sum_com_hand = computer_hand[0] + computer_hand[1] + computer_hand[2]
                print(f"Your final hand: {user_hand}, final score: {sum_user_hand}")
                print(f"Computer's final hand: {computer_hand}, final score: {new_sum_com_hand}")

                if sum_user_hand == new_sum_com_hand:
                    print("You draw!")
                elif sum_user_hand > new_sum_com_hand and sum_user_hand < 22:
                    print("You Win!")
                elif 21 < sum_user_hand:
                    print("You went over. You lose")
                else:
                    print("You lose")

            else:
                print(f"Your final hand: {user_hand}, final score: {sum_user_hand}")
                print(f"Computer's final hand: {computer_hand}, final score: {sum_com_hand}")

                if sum_user_hand == sum_com_hand:
                    print("You draw!")
                elif sum_user_hand > sum_com_hand and sum_user_hand < 22:
                    print("You Win!")
                elif 21 < sum_user_hand:
                    print("You went over. You lose")
                else:
                    print("You lose")
        should_continue = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")
        if should_continue == "n":
            end_game = True

    else:
        end_game = True
