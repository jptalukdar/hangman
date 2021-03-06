import Worker

class Game():
    def __init__(self,worker = None):
        self.host = None
        self.player = None
        self.lives = 3
        self.worker = Worker.Worker()


    def addHost(self,host):
        self.host = host

    def addPlayer(self,player):
        self.player = player

    def start(self):
        self.host.getNewCard()
        while(True):
            self.host.displayCurrentState()
            outcome = self.host.playerTurn(self.player.turn())
            if outcome == False:
                self.lives -= 1
                self.worker.output('{}: Incorrect, You lose a life. Remaining:{}'.format(self.host.hostName,self.lives))
                if self.lives <=0:
                    self.worker.output('{}: Your Lives have ended, you lose'.format(self.host.hostName))
                    self.player.setLoss() 
                    break
            else:
                self.worker.output('{}:  Correct Guess'.format(self.host.hostName))
                if self.host.finished() == True:
                    self.worker.output('{}:  YOU WON'.format(self.host.hostName))
                    break
                

        self.worker.output('{}: GAME END'.format(self.host.hostName))

