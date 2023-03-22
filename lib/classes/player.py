from .result import Result
from .game import Game

class Player:
    def __init__(self, username:str):
        self._username = username

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
        return [ result for result in Result.results if result.player == self]
    
    def games_played( self ):
        return [ result.game for result in self.results() ]
