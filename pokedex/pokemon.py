import math
import random
import textwrap


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
                         self.stat_hp,
                         self.stat_atk,
                         self.stat_def,
                         self.stat_spd,
                         self.stat_spc)

    def calculate_stats(self):
        """Calculate base stats as per formula in original gen 1 games"""
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

        def stat_formula(base, iv, ev):
            """Formula used to calculate all stats"""
            calc_iv_mod = (base + iv) * 2
            calc_ev_mod = math.floor(math.sqrt(ev)/4)
            calc_level_mod = (calc_iv_mod + calc_ev_mod) * self.level
            stat_base = math.floor(calc_level_mod / 100)
            return stat_base + 5

        calculate_iv(self)

        self.stat_hp = stat_formula(self.base_hp, self.iv_hp, self.ev_hp) + self.level + 5
        self.stat_atk = stat_formula(self.base_atk, self.iv_atk, self.ev_atk)
        self.stat_def = stat_formula(self.base_def, self.iv_def, self.ev_def)
        self.stat_spd = stat_formula(self.base_spd, self.iv_spd, self.ev_spd)
        self.stat_spc = stat_formula(self.base_spc, self.iv_spc, self.ev_spc)

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
