
class Result:

    all = []

    def __init__( self, player, game, score ):
        self.player = player
        self.game = game
        self.score = score

        Result.all.append( self )

    @property
    def score( self ):
        return self._score
    
    @score.setter
    def score( self, score ):
        if 1 <= score <= 5000:
            self._score = score
        else:
            print("Score needs to be between 1 and 5000!")

    @property
    def player( self ):
        return self._player
    
    @player.setter
    def player( self, player ):
        self._player = player

    @property
    def game( self ):
        return self._game
    
    @game.setter
    def game( self, game ):
        self._game = game
    
