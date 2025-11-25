cards = ["SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", 
    "S10", "SJ", "SQ", "SK", "HA", "H2", "H3", "H4", "H5", "H6", 
    "H7", "H8", "H9", "H10", "HJ", "HQ", "HK", "DA", "D2", "D3", 
    "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK", 
    "CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", 
    "CJ", "CQ", "CK"]

hand = cards[0:25:2]

print(hand)
hand_value = 0
for card in hand:
    if hand_value > 21:
        print("Bust!", card)
        break
    if "2" in card:
        hand_value += 2
    elif "3" in card:
        hand_value += 3
    elif "4" in card:
        hand_value += 4
    elif "5" in card:
        hand_value += 5
    elif "6" in card:
        hand_value += 6
    elif "7" in card:
        hand_value += 7
    elif "8" in card:
        hand_value += 8
    elif "9" in card:
        hand_value += 9
    elif "10" in card:
        hand_value += 10
    elif "J" in card:
        hand_value += 10
    elif "Q" in card:
        hand_value += 10
    elif "K" in card:
        hand_value += 10

    if "A" in card:
        if hand_value <= 10:
            hand_value += 11
        else:
            hand_value += 1



print(hand_value)
