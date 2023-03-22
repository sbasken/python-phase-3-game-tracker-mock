from classes.result import Result

class Game:

    # games = []

    def __init__(self, title:str):
        if 0 < len(title):
            self._title = title

        # Game.games.append(self)

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not hasattr(self, "_title"):
            self._title = title
        else:
            print('Cannot change the title of the game')

    def results( self ):
        return [ result for result in Result.all if result.game == self]
    
    def players( self ):
        return [ result.player for result in self.results()]
    
    def average_score( self, player):
        list = [ result.score for result in self.results()]
        return sum(list) / len(list) 