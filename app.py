from flask import Flask, render_template_string, session
import random

app = Flask(__name__)
app.secret_key = 'paco_le_gardien_du_clavier'

# Initialise le compteur
@app.before_request
def init_counter():
    if 'compteur' not in session:
        session['compteur'] = 0

# Listes des sortilèges
noms_sortileges = [
    "L'Exorcisme des Trolls",
    "Le Chuchotement des Algos Rebelles",
    "La Danse des Données Libres",
    "Le Sortilège du Code Éthique"
]

ingredients = [
    "une larme de café froid",
    "un fil de laine emmêlée (merci Paco)",
    "un morceau de code commenté",
    "une erreur 404"
]

effets = [
   "transforme les haters en statues de sel",
   "fait planter les algorithmes oppressifs",
   "révèle la vérité cachée dans les données",
   "protège ton clavier des keyloggers"
]

def generer_sortilege():
    nom = random.choice(noms_sortileges)
    ingredient = random.choice(ingredients)
    effet = random.choice(effets)
    return {"nom": nom, "ingredient": ingredient, "effet": effet}

# Route principale
@app.route("/")
def home():
    session['compteur'] += 1
    sort = generer_sortilege()
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Générateur de Sortilèges Anti-Monstres Modernes</title>
            <style>
                body { font-family: 'Comic Sans MS', cursive; text-align: center; background-color: #f0f8ff; padding: 20px; }
                .sortilege { border: 2px solid #8a2be2; border-radius: 10px; padding: 20px; margin: 20px auto; max-width: 500px; background: white; }
                button { background-color: #8a2be2; color: white; border: none; padding: 10px 20px; font-size: 16px; border-radius: 5px; cursor: pointer; }
                h1 { color: #8a2be2; }
           </style>
       </head>
       <body>
           <h1>🔮 Générateur de Sortilèges Anti-Monstres Modernes 🔮</h1>
           <p>Sortilèges lancés aujourd'hui : <strong>{{ session['compteur'] }}</strong></p>
           <div class="sortilege">
               <h2>{{ sort.nom }}</h2>
               <p><em>Ingrédient secret : {{ sort.ingredient }}</em></p>
               <p><strong>Effet :</strong> {{ sort.effet }}</p>
           </div>
           <button onclick="window.location.reload()">Lancer un nouveau sortilège !</button>
           <p style="margin-top: 20px; font-size: 12px; color: #666;">
               <a href="/about" style="color: #8a2be2;">En savoir plus sur ce projet</a>
           </p>
           <p style="font-size: 12px; color: #666;">
                Avec la bénédiction de Paco, Gardien Suprême du Clavier.
           </p>
       </body>
       </html>
''', sort=sort)

# Route "À propos" (UNE SEULE FOIS !)
@app.route("/about")
def about():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>À propos - Sortilèges Anti-Monstres Modernes</title>
            <style>
                body { font-family: 'Comic Sans MS', cursive; text-align: center; background-color: #f0f8ff; padding: 20px; }
                .container { max-width: 600px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); border: 2px solid #8a2be2; }
                a { color: #8a2be2; text-decoration: none; }
            </style>
        </head>
        <body>
            <div class="container">
                <h1>🔮 À propos de ce projet</h1>
                <p>Ce générateur de sortilèges est une <strong>arme poétique</strong> contre les monstres modernes :
                trolls, algorithmes oppressifs, et bugs malveillants.</p>
                <p>Développé avec <strong>Flask</strong> et <strong>Python</strong>, avec l'aide spirituelle de <em>Paco, Gardien Suprême du Clavier</em>.</p>
                <p><a href="/">← Retour aux sortilèges</a></p>
           </div>
        </body>
        </html>
    ''')

if __name__ == "__main__":
    app.run(debug=True)
