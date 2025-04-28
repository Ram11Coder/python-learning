# Fetch API response
import requests

base_url = "https://pokeapi.co/api/v2/"

def pokemon_info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon_data = response.json()
        return pokemon_data
    else:
        print(f"Failed to retrieve data {response.status_code}")


pokeman = "pikachu"

pokeman_info = pokemon_info(pokeman)
if pokeman_info:
    print(pokeman_info["name"].capitalize())
    print(pokeman_info["id"])