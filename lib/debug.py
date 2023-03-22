#!/usr/bin/env python3
import ipdb

from classes.player import Player
from classes.game import Game
from classes.result import Result


baseball = Game( 'Baseball' )
football = Game( 'Football' )
volleyball = Game( 'Volleyball' )

adam = Player( 'Adam' )
emily = Player( 'Emily' )
joe = Player( 'Joe' )

result1 = Result( adam, baseball, 30 )
result2 = Result( emily, volleyball, 10 )
result3 = Result( adam, football, 20 )

ipdb.set_trace()
