import Host
import Player
import Game
import Worker

worker = Worker.Worker() 

player = Player.Player('Neo',worker)
host = Host.Host('Amitabh Bachchan',worker)

host.getCards('movies.txt')

game = Game.Game(worker)
game.addHost(host)
game.addPlayer(player)

game.start()
