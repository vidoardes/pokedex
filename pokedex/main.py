"""Pokedex - A Pokemon stat viewer in Python 3"""
import os
import json
import textwrap


class Pokemon:
    """Create a pokemon instance from a dictionary of attrubutes"""
    def __init__(self, dictionary):
        """Create a pokemon and load stats from dictionary"""
        self.type_list = ""
        self.evo_list = ""
        self.level = 5

        # Create attributes for every key in provided dictionary
        for k, v in dictionary.items():
            setattr(self, k, v)

        # Build a list of types for display purposes
        for poke_type in self.type:
            if poke_type == "Grass":
                self.type_list += "\x1b[6;30;42m Grass \x1b[0m "
            elif poke_type == "Poison":
                self.type_list += "\x1b[0;37;45m Poison \x1b[0m "
            elif poke_type == "Fire":
                self.type_list += "\x1b[6;37;41m Fire \x1b[0m "
            elif poke_type == "Flying":
                self.type_list += "\x1b[6;34;47m Flying \x1b[0m "
            elif poke_type == "Water":
                self.type_list += "\x1b[1;37;44m Water \x1b[0m "
            else:
                self.type_list += " " + poke_type + " "

        # Build a list of evolutions for display purposes
        if len(self.evolutions) > 0 or len(self.pre_evolutions) > 0:
            if len(self.pre_evolutions) > 0:
                self.evo_list += " -> ".join(self.pre_evolutions)

            if self.evo_list != "":
                self.evo_list += " -> "

            self.evo_list += "\033[1m" + self.name + "\x1b[0m"

            if len(self.evolutions) > 0:
                self.evo_list += " -> "
                self.evo_list += " -> ".join(self.evolutions)
        else:
            self.evo_list = "None"

    def __str__(self):
        """Print pokemon stats page"""
        return ("\033[1m{} {}\x1b[0m "
                "({} {})\n"
                "{} Pokémon\n"
                "{}\n\n"
                "{}\n\n"
                "Evolutions: {}"
                ).format(self.number,
                         self.name,
                         self.name_jp,
                         self.name_jp_phonetic,
                         self.category,
                         self.type_list,
                         textwrap.fill(self.description, 70),
                         self.evo_list)


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
