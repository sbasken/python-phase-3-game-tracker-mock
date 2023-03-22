from classes.result import Result

class Game:
    def __init__(self, title:str):
        if 0 < len(title):
            self._title = title

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if not hasattr(self, "_title"):
            self._title = title
        else:
            print('Cannot change the title of the game')