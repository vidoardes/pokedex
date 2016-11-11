import os


class pokemon:
    def __init__(self, name, dictionary):
        self.name = name

        for k, v in dictionary.items():
            setattr(self, k, v)

        self.type_list = " / ".join(self.types)

    def __str__(self):
        return ("{} {}\n"
                "------------------\n"
                "Category: {}\n"
                "Types: {}\n\n"
                "{}"
                ).format(self.number, self.name, self.category, self.type_list, self.description)


def main_menu():
    select_pokemon = None
    pokedex = {
                  "Bulbasaur": {
                      "number": "#001",
                      "types": ["Grass", "Poison"],
                      "category": "Seed",
                      "height": "0.7m",
                      "weight": "6.9kg",
                      "description": "Bulbasaur can be seen napping in bright sunlight. There is a seed on its back. By soaking up the sun's rays, the seed grows progressively larger."
                  },
                  "Charmander": {
                      "number": "#004",
                      "types": ["Fire"],
                      "category": "Lizard",
                      "height": "0.6m",
                      "weight": "8.5kg",
                      "description": "The flame that burns at the tip of its tail is an indication of its emotions. The flame wavers when Charmander is enjoying itself. If the Pokémon becomes enraged, the flame burns fiercely."
                  }
              }

    os.system('cls')
    print("Welcome to the Pokédex!")

    while select_pokemon not in pokedex:
        select_pokemon = input("Which Pokémon would you like to see details for?: ")

        if select_pokemon in pokedex:
            active_pokemon = pokemon(select_pokemon, pokedex[select_pokemon])
            os.system('cls')
            print(active_pokemon)
        else:
            print("No Pokémon found with the name {}\n".format(select_pokemon))

if __name__ == '__main__':
    abspath = os.path.abspath(__file__)
    dname = os.path.dirname(abspath)
    os.chdir(dname)

    main_menu()
