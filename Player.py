import Worker

class Player:
    def __init__(self,playerName,worker=None):
        self.playerName = playerName
        self.wins = 0
        self.loss = 0
        if type(worker) != type(Worker.Worker):
            self.worker = Worker.Worker()  
        else:
            self.worker = worker

    def turn(self):
        myinput = self.worker.input()  #Loose coupled
        return myinput

    def setPlayerName(self,name):
        self.playerName = name

    def setWin(self):
        self.wins += 1

    def setLoss(self):
        self.loss += 1

    def getWins(self):
        return self.wins

    def getLoss(self):
        return self.loss