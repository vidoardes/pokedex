import os
import json
import textwrap


class pokemon:
    def __init__(self, dictionary):
        for k, v in dictionary.items():
            setattr(self, k, v)

        self.type_list = ""

        for poke_type in self.types:
            if poke_type == "Grass":
                self.type_list += "\x1b[6;30;42m Grass \x1b[0m "
            elif poke_type == "Poison":
                self.type_list += "\x1b[0;37;45m Poison \x1b[0m "
            elif poke_type == "Fire":
                self.type_list += "\x1b[6;37;41m Fire \x1b[0m "
            elif poke_type == "Flying":
                self.type_list += "\x1b[6;34;37m Flying \x1b[0m "
            else:
                self.type_list += " " + poke_type + " "

        self.evo_list = ""

        if len(self.evolutions) > 0 or len(self.pre_evolutions) > 0:
            if len(self.pre_evolutions) > 0:
                self.evo_list += " -> ".join(self.pre_evolutions)

            if self.evo_list != "":
                self.evo_list += " -> "

            self.evo_list += '\033[1m' + self.name + '\x1b[0m'

            if len(self.evolutions) > 0:
                self.evo_list += " -> "
                self.evo_list += " -> ".join(self.evolutions)
        else:
            self.evo_list = "None"

    def __str__(self):
        return ("\033[1m{} {}\x1b[0m\n"
                "{} Pokémon\n"
                "{}\n\n"
                "{}\n\n"
                "Evolutions: {}"
                ).format(self.number,
                         self.name,
                         self.category,
                         self.type_list,
                         textwrap.fill(self.description, 70),
                         self.evo_list)


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
            input("\n\x1b[6;30;47m << Back to main menu \x1b[0m")
            main_menu()


if __name__ == '__main__':
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    main_menu()
