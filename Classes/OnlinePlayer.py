from Classes.Player import Player


class OnlinePlayer(Player):
    def __init__(self,color):
        super().__init__(self)
        self.username = None
        self.totalPlayer = 0
        self.totalWinned = 0
        self.totalLost   = 0