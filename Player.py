import Worker

class Player:
    def __init__(self,playerName,worker=None):
        self.playerName = playerName
        if type(worker) != type(Worker.Worker):
            self.worker = Worker.Worker()  
        else:
            self.worker = worker

    def turn(self):
        myinput = self.worker.input()  #Loose coupled
        return myinput