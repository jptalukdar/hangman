import Worker
import random
import math

class NoExistingCards(Exception):
    def __str__(self):
        return "No Cards available, Please get some"

class EndOfLife(Exception):
    def __str__(self):
        return "You don't have any life. Game Ended"


class Host():
    def __init__(self,host,worker=None):
        self.hostName = host
        if type(worker) != type(Worker.Worker):
            self.worker = Worker.Worker()  
        else:
            self.worker = worker
        self.cards = []
        self.currentCard = None 
        self.currentState = None
        self.removedCharacters = None

    def getCards(self,filename):
        self.cards = self.worker.getList(filename)

    def getNewRandomCardNumber(self):
        if self.currentCard == None:
            index = random.randint(0,len(self.cards)-1)
            return index
        else:
            index = random.randint(0,len(self.cards))
            currentIndex = self.cards.index(self.currentCard)
            while (currentIndex == index):
                index = random.randint(0,len(self.cards)-1)
            return index

    def prepareCard(self):
        if self.cards == None:
            raise NoExistingCards()
        card = self.currentCard
        characters = list(set(card))            #Get list of unique Characters
        self.worker.debug(characters)
        length = len(characters)
        length = math.ceil(0.5 * length)        
        removedCharacters = random.choices(characters,k=length)  #Remove approx 50% of unique Characters
        removedCharacters = list(set(removedCharacters))        #Remove duplicate characters if given by random
        if ' ' in removedCharacters:
            removedCharacters.remove(' ')
        for i in removedCharacters:
            card = card.replace(i,'_')
        self.removedCharacters =  removedCharacters
        self.currentState = card

    def updateCurrentState(self,letter):
        card = self.currentCard
        self.worker.debug('Removed Chars: {}'.format(self.removedCharacters))
        self.removedCharacters.remove(letter)
        for i in self.removedCharacters:
            card = card.replace(i,'_')
        self.currentState = card

    def getNewCard(self):
        if self.cards == None:
            raise NoExistingCards()
        
        index = self.getNewRandomCardNumber()
        self.currentCard = self.cards[index]
        self.prepareCard()

    def getCurrentState(self):
        if self.currentCard == None:
            raise NoExistingCards()
        return self.currentState

    def finished(self):
        if '_' in self.currentState:
            return False
        else:
            return True

    def displayCurrentState(self):
        if self.currentCard == None:
            raise NoExistingCards()
        
        state = self.getCurrentState()
        self.worker.output('{}: {}'.format(self.hostName,state))
    
    def playerTurn(self,turn):
        turn = turn.upper()
        if turn in self.removedCharacters:
            self.worker.debug(self.currentState)
            self.updateCurrentState(turn)
            self.worker.debug(self.currentState)
            return True
        else:
            self.worker.debug('False: {}'.format(turn))
            return False
