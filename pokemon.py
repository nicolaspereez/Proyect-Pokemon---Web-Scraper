from urllib import response
import requests
from bs4 import BeautifulSoup

DOMAIN = 'https://pokemondb.net'
URL = '/pokedex/all'

if __name__ == '__main__':
    response = requests.get(DOMAIN + URL)

    if response.status_code == 200:
        content = response.text

        soup = BeautifulSoup(content, 'html.parser')

        table = soup.find('table', {'id': 'pokedex'})

        for row in table.tbody.find_all('tr', limit=5):
            
            columns = row.find_all('td', limit=3)

            name= columns[1].a.text
            type = [a.text for a in columns[2].find_all('a')]
            link = DOMAIN + columns[1].a['href']

            
            pokemon_response = requests.get(link)

            if pokemon_response.status_code == 200:
                pokemon_content = pokemon_response.text
                
                pokemoon_soup = BeautifulSoup(pokemon_content, 'html.parser')

                pokemon_table = pokemoon_soup.find('table', 
                                                    class_='vitals-table')
                
                species = pokemon_table.tbody.find_all('tr')[2].td.text

                print(name, '-', *type, '-', species)

        

