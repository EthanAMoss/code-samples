import json
import random

NUM_PLAYERS = 6


def get_murder(data):
    # Randomly select a suspect, weapon, and room to be the real murder
    return (random.choice(data.get("suspects")), random.choice(data.get("weapons")),
            random.choice(data.get("rooms")))


def shuffle_deck(data, murder):
    deck = []

    # Get all of the cards
    for suspect in data.get("suspects"):
        if suspect not in murder:
            deck.append(suspect)
    for weapon in data.get("weapons"):
        if weapon not in murder:
            deck.append(weapon)
    for room in data.get("rooms"):
        if room not in murder:
            deck.append(room)

    # Shuffle the deck -- Using the Fisher-Yates shuffle algorithm
    for i in range(len(deck) - 1):
        # Randomly select an index to swap
        j = random.randint(i, len(deck) - 1)

        # Swap the cards at i and j
        swap = deck[i]
        deck[i] = deck[j]
        deck[j] = swap

    return deck


def distribute_cards(deck):
    hands = []

    # Initialize each player's "hand"
    for i in range(NUM_PLAYERS):
        hands.append([])

    # Distribute the cards
    for i in range(len(deck)):
        hands[i % NUM_PLAYERS].append(deck[i])

    return hands


def print_game_state(murder, hands):
    suspect, weapon, room = murder
    print("------- MURDER -------")
    print("Suspect: {}".format(suspect))
    print("Weapon: {}".format(weapon))
    print("Room: {}".format(room))
    print()

    print("---- Player Hands ----")
    for i in range(len(hands)):
        print("Player {}: {}".format(i + 1, hands[i]))


if __name__ == '__main__':
    # Load the JSON data
    deck_data = json.load(open('clueDeck.json'))

    # Get the the murder
    murder = get_murder(deck_data)

    # "Shuffle" the remaining cards
    shuffled_deck = shuffle_deck(deck_data, murder)

    # Hand out all cards
    hands = distribute_cards(shuffled_deck)

    # Print the results
    print_game_state(murder, hands)