import functools
from dataclasses import dataclass

CARD_STRENGTH = {
    '2': 1,
    '3': 2,
    '4': 3,
    '5': 4,
    '6': 5,
    '7': 6,
    '8': 7,
    '9': 8,
    'T': 9,
    # 'J': 10,
    'J': 0,
    'Q': 11,
    'K': 12,
    'A': 13,
}

@dataclass
class Hand:
    """Class for storing hand and bid and other details."""
    old_hand: str
    bid: int
    hand: str = ""
    level: int = 0

    def __post_init__(self):
        self.hand = self.old_hand
        self.change_hand()
        self.level = self.get_level(self.hand)

    def get_level(self, hand):
        match len(set(hand)):
            case 1:
                return 7
            case 2:
                number_of_cards = [hand.count(card) for card in set(hand)]
                match max(number_of_cards):
                    case 4:
                        return 6
                    case 3:
                        return 5
                    case _:
                        return 1
            case 3:
                number_of_cards = [hand.count(card) for card in set(hand)]
                match max(number_of_cards):
                    case 3:
                        return 4
                    case 2:
                        return 3
                    case _:
                        return 1
            case 4:
                return 2
            case 5:
                return 1
            case _:
                return 1
    
    def change_hand(self):
        if len(self.hand.replace('J', '')) == 0:
            pass
        elif len(self.hand.replace('J', '')) != 5:
            cards = ""
            for card in self.hand.replace('J', ''):
                if card not in cards:
                    cards += card
            
            level = []
            for card in cards:
                replaced = self.hand.replace('J', card)
                level.append(self.get_level(replaced))
            # Get cards with the most counts in hand
            cards_level = dict(zip(cards, level))
            max_level = max(cards_level.values())
            cards_max = {key: value for key, value in cards_level.items() if value == max_level}
            # Sort cards according to strength
            sorted_cards = sorted(cards_max, key=functools.cmp_to_key(compare_cards), reverse=True)

            # Change hand
            self.hand = self.hand.replace('J', sorted_cards[0])


all_hands = []

"""
Compare function for 2 given hands.
Compare the level first, and then compare compare card strengths, i.e. compare per card.
"""
def compare_hands(hand1, hand2):
    if hand1.level == hand2.level:
        # Compare original cards with Js for tiebreakers
        hand1 = hand1.old_hand
        hand2 = hand2.old_hand
        for i in range(0, min(len(hand1), len(hand2))):
            if CARD_STRENGTH[hand1[i]] > CARD_STRENGTH[hand2[i]]:
                return 1
            elif CARD_STRENGTH[hand1[i]] < CARD_STRENGTH[hand2[i]]:
                return -1
        return 0
    elif hand1.level > hand2.level:
        return 1
    elif hand1.level < hand2.level:
        return -1
    return 0

"""
Compare function for 2 cards.
Check which card is "stronger" depending first on how many there is of that card in a hand, and then on how "high" that card is.
"""
def compare_cards(card1, card2):
    if CARD_STRENGTH[card1] > CARD_STRENGTH[card2]:
            return 1
    elif CARD_STRENGTH[card1] < CARD_STRENGTH[card2]:
        return -1
    return 0

if __name__ == "__main__":
    input_file = open("input.txt", "r")
    # input_file = open("sample.txt", "r")
    lines = input_file.readlines()

    for line in lines:
        split_line = line.split(" ")
        hand = split_line[0]
        bid = int(split_line[1])
        all_hands.append(Hand(hand, bid))
    sorted_hands = sorted(all_hands, key=functools.cmp_to_key(compare_hands))
    winnings = 0
    for i in range(1, len(sorted_hands) + 1):
        winnings += i * sorted_hands[i - 1].bid
    print(f"Total winnings: {winnings}")