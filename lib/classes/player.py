from .result import Result

class Player:

    def __init__(self, username:str):
        if 2 <= len(username) <=16:
            self._username = username
        else:
            print("Username must be between 2 and 16 characters!")

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if 2 <= len(username) <=16:
            self._username = username
        else:
            print("Username must be between 2 and 16 characters!")
        

    def results( self ):
        return [ result for result in Result.all if result.player == self]
    
    def games_played( self ):
        return [ result.game for result in self.results() ]
    
    def played_game( self, game ):
        return game in self.games_played()
    
    def num_times_played( self, game ):
        return len([ item for item in self.games_played() if item == game ])
    
    def add_result(self, game, score):
        Result(self, game, score )
