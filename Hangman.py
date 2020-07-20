import Host
import Player
import Game
import Worker

worker = Worker.Worker()
player = Player.Player('Jp',worker)
host = Host.Host('Amitabh Bachan',worker)
host.getCards('movies.txt')
game = Game.Game(worker)

game.addHost(host)
game.addPlayer(player)

game.start()
