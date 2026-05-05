import random

noms_sortileges = [
    "L'Exorcisme des Trolls",
    "Le Chuchotement des Algos Rebelles",
    "La Danse des Données Libres"
]

ingredients = [
    "une larme de café froid",
    "un fil de laine emmêlée (merci Paco)",
    "un commit sans message"
]

effets = [
    "transforme les haters en statues de sel",
    "fait planter les algorithmes oppressifs",
    "protège ton clavier des keyloggers"
]

def generer_sortilege():
    nom = random.choice(noms_sortileges)
    ingredient = random.choice(ingredients)
    effet = random.choice(effets)
    return f"🔮 {nom} 🔮\nIngrédient : {ingredient}\nEffet : {effet}\n"

for _ in range(3):
    print(generer_sortilege())
    print("---")
