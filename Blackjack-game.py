import random
class blackjack:
  def __init__(self, name, buyin=0, card=[]):
    self.name = name
    self.bet = 0
    self.result = ''
    
    self.casinopt = 0
    self.playerpt = 0
    self.playerhit = []
    self.casinohit =[]
    self.buyin = buyin
    self.cards = card
    
  def __repr__(self):
    return ('Dear {name}, You buyin ${buyin} on BlackJack, good luck!').format(buyin= self.buyin, name= self.name)
  
  
    
  def playgame(self):
    self.bet = int(input('please place your bet: '))
    if (len(self.cards) > (decks/8*52*1.5) and self.buyin >= self.bet):
        self.playerhit = []
        self.casinohit =[]
        self.casinohit.append(random.choice(self.cards))
        self.casinohit.append(random.choice(self.cards))
        
        self.playerhit.append(random.choice(self.cards))
        self.playerhit.append(random.choice(self.cards))
        if((self.casinohit[0] == 'Ace' and (self.casinohit[1] == 10 or self.casinohit[1] == 'J' or self.casinohit[1] == 'Q' or self.casinohit[1] == 'K')) or (self.casinohit[1] == 'Ace' and (self.casinohit[0] == 10 or self.casinohit[0] == 'J' or self.casinohit[0] == 'Q' or self.casinohit[0] == 'K')) and (self.playerhit[0] == 'Ace' and (self.playerhit[1] == 10 or self.playerhit[1] == 'J' or self.playerhit[1] == 'Q' or self.playerhit[1] == 'K')) or (self.playerhit[1] == 'Ace' and (self.playerhit[0] == 10 or self.playerhit[0] == 'J' or self.playerhit[0] == 'Q' or self.playerhit[0] == 'K'))):
            print('Push! No one wins.')
        elif (self.casinohit[0] == 'Ace' and (self.casinohit[1] == 10 or self.casinohit[1] == 'J' or self.casinohit[1] == 'Q' or self.casinohit[1] == 'K')) or (self.casinohit[1] == 'Ace' and (self.casinohit[0] == 10 or self.casinohit[0] == 'J' or self.casinohit[0] == 'Q' or self.casinohit[0] == 'K')):
            print('You lose, Dealer BlackJack')
            self.buyin -= self.bet
        elif(self.playerhit[0] == 'Ace' and (self.playerhit[1] == 10 or self.playerhit[1] == 'J' or self.playerhit[1] == 'Q' or self.playerhit[1] == 'K')) or (self.playerhit[1] == 'Ace' and (self.playerhit[0] == 10 or self.playerhit[0] == 'J' or self.playerhit[0] == 'Q' or self.playerhit[0] == 'K')):
            print('You won, winer winer, chicken dinner! You got BlackJack, payout 1:1.5, you won {money}'.format(money= self.bet*1.5 ))
            self.buyin += self.bet * 1.5
        else:
            print(('Dealer has a card {card} faceup, and you have {card1} and {card2}.').format(card= self.casinohit[0], card1=self.playerhit[0],card2=self.playerhit[1]))
            self.cards.remove(self.casinohit[0])
            self.cards.remove(self.casinohit[1])
            self.cards.remove(self.playerhit[0])
            self.cards.remove(self.playerhit[1])
            self.result = input('Do you want to hit, surrender, double, or stay? ')
        while (self.result == 'hit' ):
            self.playerhit.append(random.choice(self.cards))
            print('The card you hit is {card}'.format(card = self.playerhit[len(self.playerhit)-1]))
            print('You have '+str(self.playerhit)+' on hand')
            self.cards.remove(self.playerhit[len(self.playerhit)-1])
            self.playerpt = 0
            for i in self.playerhit:
                if i == 'J' or i == 'Q' or i == 'K' :
                    self.playerpt += 10
                elif i == 'Ace':
                    self.playerpt += 1
                else:
                    self.playerpt += i
            
            if self.playerpt <= 21:
                self.result = input('Do you want to hit, or stay? ')
                while (self.result != 'hit' and self.result != 'stay'):
                   self.result = input('Do you want to hit, or stay? ')
                
            else:
                print('Boom! Greater than 21. You lose.')
                self.buyin -= self.bet
                break
            
            
        if (self.result == 'surrender'):
            print('You choose to surrender, lose half of bet')
            self.buyin -= self.bet/2
        elif (self.result == 'double'):
            if self.buyin >= self.bet*2:
                self.playerhit.append(random.choice(self.cards))
                print('The card you double is {card}'.format(card = self.playerhit[len(self.playerhit)-1]))
                self.bet *= 2
                self.cards.remove(self.playerhit[len(self.playerhit)-1])
                if self.checkplayerpt() == self.checkcasinopt():
                    print('Push!\nYour hand: ' +str(self.playerhit)+ '\nCasino hand:'+str(self.casinohit))
                elif self.checkcasinopt()>21 or self.checkplayerpt() > self.checkcasinopt():
                    print('You win! \nYour hand: ' +str(self.playerhit)+ '\nCasino hand:'+str(self.casinohit))
                    self.buyin += self.bet
                
                else:
                    print('You lose!\nYour hand: ' +str(self.playerhit)+ '\nCasino hand:'+str(self.casinohit))
                    self.buyin -= self.bet
            else:
                print('You don\'t have enough money to double. This game will count as hit.')
                self.playerhit.append(random.choice(self.cards))
                print('The card you hit is {card}'.format(card = self.playerhit[len(self.playerhit)-1]))
                self.bet *= 1
                self.cards.remove(self.playerhit[len(self.playerhit)-1])
                if self.checkplayerpt() == self.checkcasinopt():
                    print('Push!\nYour hand: ' +str(self.playerhit)+ '\nCasino hand:'+str(self.casinohit))
                elif self.checkcasinopt()>21 or self.checkplayerpt() > self.checkcasinopt():
                    print('You win! \nYour hand: ' +str(self.playerhit)+ '\nCasino hand:'+str(self.casinohit))
                    self.buyin += self.bet
                
                else:
                    print('You lose!\nYour hand: ' +str(self.playerhit)+ '\nCasino hand:'+str(self.casinohit))
                    self.buyin -= self.bet
        elif (self.result == 'stay'):
            if self.checkplayerpt() == self.checkcasinopt():
                print('Push!\nYour hand: ' +str(self.playerhit)+ '\nCasino hand:'+str(self.casinohit))
            elif self.checkcasinopt()>21 or self.checkplayerpt() > self.checkcasinopt():
            
                print('You win! \nYour hand: ' +str(self.playerhit)+ '\nCasino hand:'+str(self.casinohit))
                self.buyin += self.bet
            else:
                print('You lose!\nYour hand: ' +str(self.playerhit)+ '\nCasino hand:'+str(self.casinohit))
                self.buyin -= self.bet
        self.continueplay()
    elif (self.bet > self.buyin):
        print('You don\'t have enough credit to play.')
        outcome= input('Do you want to buy in more credits or leave? (Buyin = b , Leave = l , Chceck balance = c)')
        if outcome == 'b':
            self.buyin += int(input('How much you want to buy in? Please give me a number'))
            print('You total balance now is ${buyin}, good luck!'.format(buyin = self.buyin))
            self.playgame()
        elif outcome == 'l':
            
            print('You total balance now is ${buyin}, good luck!'.format(buyin = self.buyin))
        elif outcome == 'c':
            
            print('You total balance now is ${buyin}, good luck!'.format(buyin = self.buyin))
            self.continueplay()
            
    else:
        print('Please wait a second, run out of cards, will shuffle in a minute')
        self.cards = cards
        self.continueplay()

    # elif (self.result != 'stay' or self.result != 'surrender' or self.result != 'double' or self.result != 'hit'):
    #     print('please type in correct action')
    #     self.result = input('Do you want to hit, surrender, double, or stay? ')   
  def checkplayerpt(self):
    self.playerpt = 0
    for i in self.playerhit:
      if i == 'J' or i == 'Q' or i == 'K' :
        self.playerpt += 10
      elif i == 'Ace':
        self.playerpt += 1
      else:
        self.playerpt += i
    for i in range(self.playerhit.count('Ace')):
      if (self.playerpt +10 )<= 21:
        self.playerpt +=10
    return self.playerpt
  def checkcasinopt(self):
    self.casinopt = 0
    for i in self.casinohit:
        if i == 'J' or i == 'Q' or i == 'K' :
          self.casinopt += 10
        elif i == 'Ace':
          self.casinopt += 11
          if (self.casinopt ) > 21:
            self.casinopt -=10
        else:
          self.casinopt += i
    while(self.casinopt <=16 ):
        self.casinohit.append(random.choice(self.cards))
        self.cards.remove(self.casinohit[len(self.casinohit)-1])
        print('casino just draw a {card}'.format(card= self.casinohit[len(self.casinohit)-1]))
        index = self.casinohit[len(self.casinohit)-1]
        
        if index == 'J' or index == 'Q' or index == 'K' :
            self.casinopt += 10
        elif index == 'Ace':
            self.casinopt += 11
            if (self.casinopt ) > 21:
                self.casinopt -=10
        else:
            self.casinopt += index
        
        return self.casinopt
    return self.casinopt
  def continueplay(self):
    self.casinopt = 0
    choice = input('Do you want to continue playing?  (y/n) ')
    if choice =='y':
      self.playgame()
      
    elif choice == 'n':
      print('You have ${buyin} left, you can cashout'.format(buyin = self.buyin))
    else:
      print('please type in the answer')
      self.continueplay()


name = input('Dear Sir/Ma\'am, welcome to the blackjack table, how should I call you?  ')
cash = ''
while( type(cash) != type(5)):
    try:
        cash = int(input('How much you want to buy in the game? '))
    except (ValueError):
        print('please enter a number')
cards = ['Ace',2,3,4,5,6,7,8,9,10,'J','Q','K']
decks = ''
while(type(decks) != type(5)):
    try:
        decks = int(input('choose deck of cards you want to play with.(1 to 8 decks) '))
    except (ValueError):
        print('please enter a number')
    
cards *= 4 * int(decks)


player1 = blackjack(name, cash, cards) 
print(player1)
print(player1.playgame())

