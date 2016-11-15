"""Pokedex - A Pokemon stat viewer in Python 3"""
import os
import json

from pokemon import Pokemon


def main_menu():
    """Provide interface for finding and viewing pokemon details"""
    select_pokemon = ""
    pokemon_stats = ""

    # Read pokedex from JSON file and parse as list of dictioaries
    pokedex_json = open("pokedex.dat", encoding="utf-8").read()
    pokedex = json.loads(pokedex_json)["pokemon"]

    os.system("cls")
    print("\n                       \033[1mWelcome to the Pokédex!\x1b[0m")
    print("\n                     Generation I (Kanto Reigon)")
    print("                             #001 - #151")

    # Loop until user provides pokemon name that exists in pokedex
    while pokemon_stats == "":
        select_pokemon = input("\n\nWhich Pokémon would you like to see details for?: ").title()
        try:
            pokemon_stats = next(stats for stats in pokedex if stats["name"] == select_pokemon)
        except:
            print("\nNo Pokémon found with the name \"{}\"\n".format(select_pokemon))

        # If a valid pokemon matched, display details
        if pokemon_stats != "":
            active_pokemon = Pokemon(pokemon_stats)
            os.system("cls")
            print(active_pokemon)
            input("\n\x1b[6;30;47m << Back to main menu \x1b[0m")
            main_menu()


if __name__ == "__main__":
    os.system("chcp 65001")
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    main_menu()
