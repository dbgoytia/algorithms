from prettytable import PrettyTable

pokedex = PrettyTable()
pokedex.field_names = ["Pokemon Name", "Type"]

pokedex.add_rows([
    ["Pikachu", "electro"],
    ["Squirtle", "water"],
    ["Charmander", "fire"]
])

pokedex.align = "l"

print(pokedex)