## Futebol_to_csv

![Futebol](https://gds.portal5g-media.com/contentFiles/system/pictures/2015/5/135669/original/futebol.jpg)

O **Futebol_to_csv** é um projeto que obtém a classficação atual da série A do 
campeonato brasileiro para _CSV_ e _JSON_.
A raspagem dos dados é originada no site do [Globo esporte](http://globoesporte.globo.com/futebol/brasileirao-serie-a/).

## Configuração
* Python3
* PIP

## Instalação das dependências do projeto

pip install -r requirements.txt

## Guia de uso
Exportando Recuperando JSON
```
	from io_export import JSONExporter

	>>> json_exporter = JSONExporter()
	>>> json_exporter.build_string()
'[{"name": "Corinthians", "position": "1", "_Team__score": "71", "_Team__partidas": "35", "_Team__vitorias": "21", "_Team__empates": "8", "_Team__derrotas": "6"}, {"name": "Gr\\u00eamio", "position": "2", "_Team__score": "61", "_Team__partidas": "35", "_Team__vitorias": "18", "_Team__empates": "7", "_Team__derrotas": "10"}, {"name": "Palmeiras", "position": "3", "_Team__score": "57", "_Team__partidas": "34", "_Team__vitorias": "17", "_Team__empates": "6", "_Team__derrotas": "11"}, {"name": "Santos", "position": "4", "_Team__score": "56", "_Team__partidas": "34", "_Team__vitorias": "15", "_Team__empates": "11", "_Team__derrotas": "8"}, {"name": "Cruzeiro", "position": "5", "_Team__score": "55", "_Team__partidas": "35", "_Team__vitorias": "15", "_Team__empates": "10", "_Team__derrotas": "10"}, {"name": "Botafogo", "position": "6", "_Team__score": "51", "_Team__partidas": "34", "_Team__vitorias": "14", "_Team__empates": "9", "_Team__derrotas": "11"}, {"name": "Flamengo", "position": "7", "_Team__score": "50", "_Team__partidas": "34", "_Team__vitorias": "13", "_Team__empates": "11", "_Team__derrotas": "10"}, {"name": "Vasco", "position": "8", "_Team__score": "50", "_Team__partidas": "35", "_Team__vitorias": "13", "_Team__empates": "11", "_Team__derrotas": "11"}, {"name": "Atl\\u00e9tico-MG", "position": "9", "_Team__score": "47", "_Team__partidas": "35", "_Team__vitorias": "12", "_Team__empates": "11", "_Team__derrotas": "12"}, {"name": "Bahia", "position": "10", "_Team__score": "46", "_Team__partidas": "34", "_Team__vitorias": "12", "_Team__empates": "10", "_Team__derrotas": "12"}, {"name": "S\\u00e3o Paulo", "position": "11", "_Team__score": "45", "_Team__partidas": "35", "_Team__vitorias": "12", "_Team__empates": "9", "_Team__derrotas": "14"}, {"name": "Atl\\u00e9tico-PR", "position": "12", "_Team__score": "45", "_Team__partidas": "35", "_Team__vitorias": "12", "_Team__empates": "9", "_Team__derrotas": "14"}, {"name": "Chapecoense", "position": "13", "_Team__score": "44", "_Team__partidas": "34", "_Team__vitorias": "12", "_Team__empates": "8", "_Team__derrotas": "14"}, {"name": "Fluminense", "position": "14", "_Team__score": "43", "_Team__partidas": "35", "_Team__vitorias": "10", "_Team__empates": "13", "_Team__derrotas": "12"}, {"name": "Coritiba", "position": "15", "_Team__score": "40", "_Team__partidas": "34", "_Team__vitorias": "10", "_Team__empates": "10", "_Team__derrotas": "14"}, {"name": "Vit\\u00f3ria", "position": "16", "_Team__score": "39", "_Team__partidas": "34", "_Team__vitorias": "10", "_Team__empates": "9", "_Team__derrotas": "15"}, {"name": "Ponte Preta", "position": "17", "_Team__score": "39", "_Team__partidas": "35", "_Team__vitorias": "10", "_Team__empates": "9", "_Team__derrotas": "16"}, {"name": "Sport", "position": "18", "_Team__score": "36", "_Team__partidas": "34", "_Team__vitorias": "9", "_Team__empates": "9", "_Team__derrotas": "16"}, {"name": "Ava\\u00ed", "position": "19", "_Team__score": "36", "_Team__partidas": "35", "_Team__vitorias": "8", "_Team__empates": "12", "_Team__derrotas": "15"}, {"name": "Atl\\u00e9tico-GO", "position": "20", "_Team__score": "30", "_Team__partidas": "34", "_Team__vitorias": "8", "_Team__empates": "6", "_Team__derrotas": "20"}]'
```