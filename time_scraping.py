import requests
from team_soccer import Team
from bs4 import BeautifulSoup

class SoccerScrapy(object):
    '''
        The class find on the web the classification in league of the Brazil
    '''
    def __init__(self):
        self.page = requests.get('http://globoesporte.globo.com/futebol/brasileirao-serie-a/')
        self.soup = BeautifulSoup(self.page.text, 'html.parser')

    def find_data(self):
        '''
            Search the data and return an arrays of team and its qualification
        '''
        table_team = self.soup.find('table', {'class': 'tabela-times'})
        table_pontos = self.soup.find('table', {'class': 'tabela-pontos'})
        pontuacao = []

        # Fill the position, name  of soccer group
        for row in table_team.findAll('tr'):
            cells = row.findAll('td')
            if len(cells) > 0:
                position = cells[0].text.strip()
                name = cells[1].text[:-3]
                pontuacao.append(Team(name, position))

        # Fill the pontuations
        for index, row in enumerate(table_pontos.findAll('tr')):
            cells = row.findAll('td')
            if len(cells) > 0:
                pontuacao[index - 1].score = cells[0].text.strip()
                pontuacao[index - 1].partidas = cells[1].text.strip()
                pontuacao[index - 1].vitorias = cells[2].text.strip()
                pontuacao[index - 1].empates = cells[3].text.strip()
                pontuacao[index - 1].derrotas = cells[4].text.strip()
                
        return pontuacao
