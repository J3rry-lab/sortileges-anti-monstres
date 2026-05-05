from flask import Flask, render_template_string, session
importer aléatoire

application = Flask(__nom__)
application = app # OBLIGATOIRE pour PythonAnywhere
app.secret_key = 'paco_le_gardien_du_clavier'

# Initialiser le compteur
@app.avant_requête
def init_counter():
    if 'compteur' not in session :
        session['compteur'] = 0

# Listes des sortilèges
noms_sortilèges = [
    "L'Exorcisme des Trolls",
    "Le Chuchotement des Algos Rebelles",
    "La Danse des Données Libres",
    "Le Sortilège du Code Éthique"
]

ingrédients = [
    "une larme de café froid",
    "un fil de laine emmelée (merci Paco)",
    "un morceau de code commenté",
    "une erreur 404"
]

effets = [
    "transformer les haters en statues de sel",
    "fait planter les algorithmes oppressifs",
    "Révèle la vérité cachée dans les données",
    "protège ton clavier des keyloggers"
]

def generer_sortilege():
    nom = random.choice(noms_sortileges)
    ingrédient = choix aléatoire(ingrédients)
    effet = choix aléatoire(effets)
    return {"nom": nom, "ingredient": ingrédient, "effet": effet}

@app.route("/")
def home():
    session['compteur'] += 1
    trier = generer_sortilege()
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>Générateur de Sortilèges Anti-Monstres Modernes</title>
            <style>
                body { police: 'Comic Sans MS', cursive; alignement du texte: centre; couleur de fond: #f0f8ff; marge intérieure: 20px; }
                .sortilege { border: 2px solid #8a2be2; border-radius: 10px; padding: 20px; margin: 20px auto; max-width: 500px; background: white; }
                button { couleur de fond : #8a2be2; couleur : blanc; bordure : aucune; marge intérieure : 10px 20px; taille de police : 16px; rayon de bordure : 5px; curseur : pointeur; }
                h1 { couleur : #8a2be2; }
            </style>
        </head>
        <body>
            <h1>🔮 Générateur de Sortilèges Anti-Monstres Modernes 🔮</h1>
            <p>Sortilèges lancés aujourd'hui : <strong>{{ session['compteur'] }}</strong></p>
            <div class="sortilege">
                <h2>{{ sort.nom }}</h2>
                <p><em>Ingrédient secret : {{ sort.ingredient }}</em></p>
                <p><strong>Effet :</strong> {{ sort.effet }></p>
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
    ''', trier=tri)

@app.route("/about")
def about():
    return render_template_string('''
        <!DOCTYPE html>
        <html>
        <head>
            <title>À propos - Sortilèges Anti-Monstres Modernes</title>
            <style>
                body { police: 'Comic Sans MS', cursive; alignement du texte: centre; couleur de fond: #f0f8ff; marge intérieure: 20px; }
                .container { max-width: 600px; margin: 0 auto; background: white; padding: 20px; border-radius: 10px; box-shadow: 0 0 10px rgba(0,0,0,0.1); border: 2px solid #8a2be2; }
                a { couleur : #8a2be2 ; décoration de texte : aucune ; }
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

si __name__ == "__main__":
    app.run(debug=True)