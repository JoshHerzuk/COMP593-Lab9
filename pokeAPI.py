import requests


def get_poke_info(name): 
    """
    queries the poke API for information related to the pokemon specified 
    
    :param name: Pokemon's name or Pokedex number
    :returns: Dictionary of pokemon info if successful, and None if not successful
    """
    print("Retrieving Pokemon information...", end='')
    

    if name is None:
        return

    name = name.lower().strip()

    if name == '':
        return
        
    URL = 'https://pokeapi.co/api/v2/pokemon/' + str(name)
   
    response = requests.get(URL)

    if response.status_code == 200:
        print("Success")
        return response.json()

    else:
        print('failed. Response code:', response.status_code)
        return



def get_pokemon_names(limit=151, offset=0):
    """
    retrieves a list of pokemon names from the PokeApi

    :param limit: how many pokemon you want 
    :param offset: the number of pokemon skipped at the begining of the list
    :returns: a list of pokemon names
    """
    print("Retrieving List of Pokemon...", end='')

    URL = 'https://pokeapi.co/api/v2/pokemon/' 

    params = {
        'offset': offset,
        'limit': limit
    }
   
    response = requests.get(URL, params=params)

    if response.status_code == 200:
        print("Success")
        poke_dict = response.json()
        return [p['name'] for p in poke_dict['results']]

    else:
        print('failed. Response code:', response.status_code)
        return


def get_pokemon_image_url(name):
    """
    retrieves the url of the image of the specified pokemon
    
    :param name: the name of the pokemon you want the image of
    :returns: The url of the image of the pokemon
    """
    poke_dict = get_poke_info(name)

    if poke_dict:
        poke_url = poke_dict['sprites']['other']['official-artwork']['front_default']
        return poke_url