"""Pokedex - A Pokemon stat viewer in Python 3"""
import os
import json
import textwrap
import random
import math


class Pokemon:
    """Create a pokemon instance from a dictionary of attrubutes"""

    def __init__(self, dictionary):
        """Create a pokemon and load stats from dictionary"""
        self.type_list = ""
        self.evo_list = ""
        self.level = 5
        self.ev_hp = 0
        self.ev_atk = 0
        self.ev_def = 0
        self.ev_spd = 0
        self.ev_spc = 0

        # Create attributes for every key in provided dictionary
        for k, v in dictionary.items():
            setattr(self, k, v)

        self.calculate_iv()
        self.calculate_stats()

    def __str__(self):
        """Print pokemon stats page"""
        self.generate_type_list()
        self.generate_evo_list()

        return ("\033[1m#{} {}\x1b[0m "
                "({} {})\n"
                "{} Pokémon\n"
                "{}\n\n"
                "{}\n\n"
                "Evolutions: {}\n"
                "Locations: {}\n"
                "Stats: HP {} / ATK {} / DEF {} / SPD {} / SPC {}"
                ).format(self.number,
                         self.name,
                         self.name_jp,
                         self.name_jp_phonetic,
                         self.category,
                         self.type_list,
                         textwrap.fill(self.description, 70),
                         self.evo_list,
                         ", ".join(self.location),
                         self.stat_max_hp,
                         self.stat_atk,
                         self.stat_def,
                         self.stat_spd,
                         self.stat_spc)

    def calculate_iv(self):
        """Generate IV values"""
        # 4 base values are a random value from 0 to 15
        self.iv_atk = random.randint(0, 15)
        self.iv_def = random.randint(0, 15)
        self.iv_spd = random.randint(0, 15)
        self.iv_spc = random.randint(0, 15)

        # HP IV is calculated by converting the previous IV
        # values to decimal, and taking the least significant
        # bit and creating a binary string from those 4 values
        self.iv_hp_bin = ""
        self.iv_hp_bin += "{0:b}".format(self.iv_atk)[-1:]
        self.iv_hp_bin += "{0:b}".format(self.iv_def)[-1:]
        self.iv_hp_bin += "{0:b}".format(self.iv_spd)[-1:]
        self.iv_hp_bin += "{0:b}".format(self.iv_spc)[-1:]

        self.iv_hp = int(self.iv_hp_bin, 2)

    def calculate_stats(self):
        def stat_formula(base, iv, ev):
            calc_iv = (base + iv) * 2
            calc_ev = math.floor(math.sqrt(ev)/4)
            stat_base = (calc_iv + calc_ev) * self.level
            return math.floor(stat_base / 100)

        self.stat_max_hp = stat_formula(self.base_hp, self.iv_hp, self.ev_hp) + self.level + 10
        self.stat_atk = stat_formula(self.base_atk, self.iv_atk, self.ev_atk) + 5
        self.stat_def = stat_formula(self.base_def, self.iv_def, self.ev_def) + 5
        self.stat_spd = stat_formula(self.base_spd, self.iv_spd, self.ev_spd) + 5
        self.stat_spc = stat_formula(self.base_spc, self.iv_spc, self.ev_spc) + 5

    def generate_type_list(self):
        """Build a list of types for display purposes"""
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

    def generate_evo_list(self):
        """Build a list of evolutions for display purposes"""
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
