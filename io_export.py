from abc import ABCMeta, abstractmethod
import os
from time_scraping import SoccerScrapy
import json

class Exporter(metaclass=ABCMeta):

    def __init__(self):
        self._scrapy = SoccerScrapy()
        self._columns = ['Posição', 'Time',
                  'Pontos', 'Partidas',
                  'Vitórias', 'Empates',
                  'Derrotas']

    @abstractmethod
    def build_string(self):
        pass

class CSVExporter(Exporter):
    '''
        The CSV exporter
    '''
    def __init__(self, delimiter=';'):
        self.__delimiter = delimiter
        super().__init__()

    def build_string(self):
        '''
            Write the csv representation 
        '''
        teams = self._scrapy.find_data()
        content = self.__delimiter.join(self._columns)  + '\n'
    
        for team in teams:
            content += team.to_csv(self.__delimiter)
        return content
            
class JSONExporter(Exporter):
    '''
        The JSON writer
    '''
    def __init__(self):
        super().__init__()

    def build_string(self, path, filename):
        '''
            Write Json File
        '''
        teams = self.scrapy.find_data()
        return json.dumps([team.__dict__ for team in teams])
        
        
