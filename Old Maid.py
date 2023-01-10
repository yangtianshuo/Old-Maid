#Tianshuo Yang
#Old Maid card game

import random

#Deal cards to a number of players
def deal_card(num_players):
    deck = [*range(2, 11), *range(2, 11), *range(2, 11), *range(2, 11),'A','J','Q','K','A','J','Q','K','A','J','Q','K','A','J','Q','K','Joker']
    random.shuffle(deck)
    all_hands = [[] for i in range(num_players)]
    while len(deck) > 0:
        for i in range(len(all_hands)):
            if len(deck) > 0:
                all_hands[i].append(deck.pop())
    return all_hands

#Take a list and rotate it to the left once
def rotate_left(lst):
    first = lst[0]
    for i in range(len(lst)-1):
        lst[i] = lst[i + 1]
    lst[len(lst)-1] = first
    return lst

#Discard pairs in a list
#Return the discarded pairs as a tuple
def discard_pair(lst):
    pairs = []
    i = 0
    while i < len(lst):
        n = lst[i]
        if lst.count(n) > 1:
            lst.remove(n)
            lst.remove(n)
            pairs.append((n,n))
        else:
            i += 1
    return pairs

#Input: a list
#Return a user selected index
def player_pick(lst):
    print("Select a card (1-" + str(len(lst)) + ")")
    while True:
        try:
            n = int(input())
            if 1 <= n <= len(lst):
                return n-1
        except ValueError:
            print("Invalid input")

#Input: a list consisting of other lists as elements, a card
#Add card to the first list
#Return the main list
def move_card(lst,card):
    lst[0].insert(random.randint(0,len(lst[0])), card)
    return lst

#Return true if user enter yes, false for no
def play_again():
    while True:
        n = input("Do you want to play again? ")
        if n.lower() == "yes":
            return True
        elif n.lower() == "no":
            return False

#Gameplay
def old_maid():
    #Ask user for number of AI players
    while True:
        try:
            n = int(input("Enter the number of computer players: "))
            if n not in range(1, 12):
                raise ValueError
        except ValueError:
            print("Invalid input")
        else:
            players = ['Human']
            for i in range(n):
                players.append("Computer " + str(i+1))
            break
    #Select a random player to go first
    first_player = players[random.randint(0,len(players)-1)]
    print(first_player,"goes first")
    #Deal cards to each player
    print("Shuffling...")
    all_hands = deal_card(len(players))
    #Discard all starting pairs
    discarded_pairs = {}
    for i in range(len(all_hands)):
        discarded_pairs[players[i]] = discard_pair(all_hands[i])
    #Rotate the list so the first player is at the beginning
    for i in range(players.index(first_player)):
        rotate_left(players)
        rotate_left(all_hands)
    #Pick and discard cards until one person remain in the game
    while True:
        print()
        print("Discarded pairs:")
        print(discarded_pairs)
        print()
        #Player and computer pick card
        if players[0] == "Human":
            print("Your deck",all_hands[0])
            for i in range(1,len(players)):
                print(players[i],"has",len(all_hands[i]),"cards")
            pos = player_pick(all_hands[-1])
        else:
            pos = random.randint(0,len(all_hands[-1])-1)
        #If the selected card is in the deck, discard the pair
        #Otherwise move it in the deck at a random location
        selected_card = all_hands[-1].pop(pos)
        if selected_card in all_hands[0]:
            all_hands[0].remove(selected_card)
            discarded_pairs[players[0]].append((selected_card,selected_card))
        else:
             move_card(all_hands,selected_card)   
        #Rotate the list so the person on the right goes next
        rotate_left(players)
        rotate_left(all_hands)
        #Remove the players without cards from the game, they are winners!
        for i in range(-2,0):
            if len(all_hands[i]) == 0:
                players.pop(i)
                all_hands.pop(i)
        #End condition and output result
        if len(players) == 1:
            print(players[0],"lose")
            break

while True:
    n = input("Do you want to play again? ")
    if n.lower() == "yes":
        old_maid()
    elif n.lower() == "no":
        break


    


