import random


class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

    def show(self):
        if self.value == '1' or self.value == '11':
            self.value = 'A'
        print(f'{self.value} of {self.suit}')


class Deck:
    def __init__(self):
        self.cards = []
        self.build()
        self.shuffle()

    def build(self):
        for s in ['♠', '♣', '♢', '♡']:
            for v in range(1, 14):
                if v == 1:
                    n = 'A'
                elif v == 11:
                    n = 'J'
                elif v == 12:
                    n = 'Q'
                elif v == 13:
                    n = 'K'
                else:
                    n = str(v)
                self.cards.append(Card(s, n))

    def show(self):
        for c in self.cards:
            c.show()

    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def drawCard(self):
        return self.cards.pop()


class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def draw(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def hit(self, deck):
        self.hand.append(deck.drawCard())
        return self

    def stand(self):
        if self.name == 'Player':
            dealer.showDealerHandTwo()

    def showPlayerHand(self):
        print('\nYour hand: ')
        for card in self.hand:
            card.show()

    def showDealerHandOne(self):
        print("\nDealer's hand: ")
        self.hand[0].show()
        j = self.hand[0]
        print('? of ?')

    def showDealerHandTwo(self):
        print('')
        print("Dealer's hand: ")
        for card in self.hand:
            card.show()


class Scores:
    def __init__(self):
        pass


    def calcScore(self, player):
        val = []
        score = 0
        for v in range(player.hand.__len__()):
            if player.hand[v].value == 'J' or player.hand[v].value == 'Q' or player.hand[v].value == 'K':
                player.hand[v].value = '10'
            if player.hand[v].value == 'A':
                player.hand[v].value = '11'
            score+=int(player.hand[v].value)
        if score > 21:
            score = 0
            for v in range(player.hand.__len__()):
                if player.hand[v].value == '11':
                    player.hand[v].value = '1'
                score += int(player.hand[v].value)
        return score


def deal():
    player.draw(deck)
    dealer.draw(deck)
    player.draw(deck)
    dealer.draw(deck)
    player.showPlayerHand()
    dealer.showDealerHandOne()


while True:
    user = input('\nMenu:\nPlay new game - P\nQuit - Q\n')
    check = True
    user = user.lower().strip()
    while check == True:
        if user == 'p':
            print('Dealing cards...')
            check = False
        elif user == 'q':
            print('Quitting...')
            exit()
        else:
            print('\nInvalid input. Please try again. (Note: only type P or Q).\n')
            user = input('\nMenu:\nPlay new game - P\nQuit - Q\n')
            user = user.lower().strip()

    deck = Deck()
    player = Player('Player')
    dealer = Player('Dealer')
    deal()
    score = Scores()
    player_score = score.calcScore(player)
    if player_score == 21:
        print('Blackjack! You win!')
    else:
        check = True
        while check == True:
            user = input('\nHit - H\nStand - S\n')
            user = user.lower().strip()
            if user == 'h':
                player.hit(deck)
                player.showPlayerHand()
                player_score = score.calcScore(player)
                print(f'Score {player_score}')
                if player_score > 21:
                    print(f'{player.name} Busted!')
                    check = False
            elif user == 's':
                dealer.showDealerHandTwo()
                dealer_score = score.calcScore(dealer)
                print(f'Score: {dealer_score}')
                while dealer_score < player_score:
                    dealer.hit(deck)
                    dealer.showDealerHandTwo()
                    dealer_score = score.calcScore(dealer)
                    print(f'Score: {dealer_score}')
                if dealer_score > 21:
                    print(f'{dealer.name} Busted!\nYou Win!')
                else:
                    print('Dealer won!')

                check = False
            else:
                print('\nInvalid input. Please try again. (Note: only type H or S).\n')
                user = input('\nHit - H\nStand - S\n')

