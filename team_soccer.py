class Team(object):

    def __init__(self, name, position):
        self.name = name
        self.position = position

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        self.__score = value

    @property
    def partidas(self):
        return self.__partidas

    @partidas.setter
    def partidas(self, value):
        self.__partidas = value

    @property
    def vitorias(self):
        return self.__vitorias

    @vitorias.setter
    def vitorias(self, value):
        self.__vitorias = value
        
    @property
    def empates(self):
        return self.__empates

    @empates.setter
    def empates(self, value):
        self.__empates = value

    @property
    def derrotas(self):
        return self.__derrotas

    @derrotas.setter
    def derrotas(self, value):
        self.__derrotas = value
        
    def __eq__(self, other):
         return self.position == other.position and self.name == other.name

    def to_csv(self, delimiter=';'):
        elements = [self.position, self.name, self.__score, self.__partidas, self.__vitorias, self.__empates, self.__derrotas]
        return delimiter.join(elements) + '\n'
    
