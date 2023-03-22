
class Result:

    def __init__( self, player, game, score ):
        self.player = player
        self.game = game
        self.score = score

    @property
    def score( self ):
        return self._score
    
    @score.setter
    def score( self, score ):
        if 1 <= score <= 5000:
            self._score = score
        else:
            print("Score needs to be between 1 and 5000!")