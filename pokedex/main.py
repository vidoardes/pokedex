import os
import json


class pokemon:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

        self.type_list = " / ".join(self.types)

    def __str__(self):
        return ("{} {}\n"
                "------------------\n"
                "Category: {}\n"
                "Types: {}\n\n"
                "{}\n"
                "Evolutions: "
                ).format(self.number, self.name, self.category, self.type_list, self.description)


def main_menu():
    select_pokemon = ""
    pokemon_stats = ""
    pokedex = json.loads(open('pokedex.dat', encoding='utf-8').read())["pokemon"]

    os.system('cls')
    print("Welcome to the Pokédex!")

    while pokemon_stats == "":
        select_pokemon = input("Which Pokémon would you like to see details for?: ")
        try:
            pokemon_stats = next(stats for stats in pokedex if stats['name'] == select_pokemon)
        except:
            print("\nNo Pokémon found with the name \"{}\"\n".format(select_pokemon))

        if pokemon_stats != "":
            active_pokemon = pokemon(pokemon_stats)
            os.system('cls')
            print(active_pokemon)
            input("\n<< Back to main menu")
            main_menu()


if __name__ == '__main__':
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    main_menu()
