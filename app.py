from flask import Flask, render_template

app = Flask(__name__)

# ============================================
# PAGE D'ACCUEIL - CHOIX DE LA MATIÈRE
# ============================================

@app.route('/')
def index():
    matieres = [
        {
            'id': 'histoire-ri',
            'titre': 'Histoire des Relations Internationales',
            'description': 'Cours sur l\'histoire des relations internationales au XXe siècle',
            'url': '/histoire-ri'
        },
        {
            'id': 'geopolitique',
            'titre': 'Géopolitique',
            'description': 'Analyse géopolitique des grands enjeux contemporains',
            'url': '/geopolitique'
        },
        {
            'id': 'risques',
            'titre': 'Analyse des Risques Internationaux',
            'description': 'Étude des risques géopolitiques, économiques et sécuritaires',
            'url': '/risques'
        }
    ]
    return render_template('index.html', matieres=matieres)


# ============================================
# SECTION 1 : HISTOIRE DES RELATIONS INTERNATIONALES
# ============================================

@app.route('/histoire-ri')
def histoire_ri_index():
    cours_list = [
        {
            'id': 'definitions-ri',
            'titre': 'Les relations internationales - Définitions',
            'description': 'Introduction historiographique et acteurs des relations internationales',
            'url': '/histoire-ri/cours/definitions-ri'
        },
        {
            'id': 'quest-ce-que-europe',
            'titre': "Qu'est-ce que l'Europe ?",
            'description': 'Définitions, mythes et représentations de l\'idée européenne',
            'url': '/histoire-ri/cours/quest-ce-que-europe'
        },
        {
            'id': 'organisations-internationales',
            'titre': "Histoire des organisations internationales",
            'description': 'De la SDN à l\'ONU : institutionnalisation des relations internationales',
            'url': '/histoire-ri/cours/organisations-internationales'
        },
        {
            'id': 'onu-integration',
            'titre': "L'ONU pendant la Guerre Froide et l'intégration régionale",
            'description': 'Organisations internationales, régionalisme et accords commerciaux',
            'url': '/histoire-ri/cours/onu-integration'
        },
        {
            'id': 'afrique-colonisation',
            'titre': "L'Europe, la Méditerranée et l'Afrique au XXe siècle",
            'description': 'Colonisation, décolonisation et héritages post-coloniaux',
            'url': '/histoire-ri/cours/afrique-colonisation'
        },
        {
            'id': 'migrations',
            'titre': 'Histoire des migrations internationales contemporaines',
            'description': 'Phénomènes migratoires, causes et évolutions du XIXe au XXIe siècle',
            'url': '/histoire-ri/cours/migrations'
        },
        {
            'id': 'diplomatie-culturelle',
            'titre': 'Relations internationales et diplomatie culturelle',
            'description': 'Échanges culturels, soft power et hégémonies culturelles au XXe siècle',
            'url': '/histoire-ri/cours/diplomatie-culturelle'
        },
        {
            'id': 'sport',
            'titre': "Le sport dans les relations internationales",
            'description': 'L\'internationalisation progressive du sport depuis la fin du XIXe siècle',
            'url': '/histoire-ri/cours/sport'
        },
        {
            'id': 'economie-20e',
            'titre': 'Relations économiques internationales au XXe siècle',
            'description': 'Mondialisation, crises et question environnementale',
            'url': '/histoire-ri/cours/economie-20e'
        }
    ]
    return render_template('histoire_ri_index.html', cours=cours_list)

@app.route('/histoire-ri/cours/definitions-ri')
def cours_definitions_ri():
    return render_template('histoire_ri/cours_definitions_ri.html')

@app.route('/histoire-ri/cours/quest-ce-que-europe')
def cours_europe():
    return render_template('histoire_ri/cours_europe.html')

@app.route('/histoire-ri/cours/organisations-internationales')
def cours_organisations_internationales():
    return render_template('histoire_ri/cours_organisations.html')

@app.route('/histoire-ri/cours/onu-integration')
def cours_onu_integration():
    return render_template('histoire_ri/cours_onu.html')

@app.route('/histoire-ri/cours/afrique-colonisation')
def cours_afrique_colonisation():
    return render_template('histoire_ri/cours_afrique.html')

@app.route('/histoire-ri/cours/migrations')
def cours_migrations():
    return render_template('histoire_ri/cours_migrations.html')

@app.route('/histoire-ri/cours/diplomatie-culturelle')
def cours_diplomatie_culturelle():
    return render_template('histoire_ri/cours_diplomatie_culturelle.html')

@app.route('/histoire-ri/cours/sport')
def cours_sport():
    return render_template('histoire_ri/cours_sport.html')

@app.route('/histoire-ri/cours/economie-20e')
def cours_economie():
    return render_template('histoire_ri/cours_economie.html')


# ============================================
# SECTION 2 : GÉOPOLITIQUE
# ============================================

@app.route('/geopolitique')
def geopolitique_index():
    cours_list = [
        {
            'titre': 'Démarches et enjeux de la géopolitique',
            'description': 'Introduction aux concepts fondamentaux de la géopolitique : relations entre pouvoir, espace et territoire, histoire de la discipline, méthodologies d\'analyse.',
            'url': '/geopolitique/cours/seance1'
        },
        {
            'titre': 'L\'État-nation, un cadre politique territorial indépassable ?',
            'description': 'Définitions et légitimation de l\'État, formes et caractéristiques étatiques, émergence de l\'État-nation, rapports au territoire.',
            'url': '/geopolitique/cours/seance2'
        },
        {
            'titre': 'Les conflits dans le monde contemporain',
            'description': 'Transformations des conflits, typologie des guerres, nouvelles échelles, crise de l\'État, émergence de nouveaux acteurs.',
            'url': '/geopolitique/cours/seance3'
        },
        {
            'titre': 'Quelles frontières pour l\'Europe ?',
            'description': 'Limites géographiques de l\'Europe, construction européenne, élargissements successifs, instruments IPA et PEV, défis contemporains.',
            'url': '/geopolitique/cours/seance4'
        },
        {
            'titre': 'Les aires culturelles aujourd\'hui',
            'description': 'Étude critique des aires culturelles : origines académiques, théorie du choc des civilisations, globalisation et pertinence contemporaine.',
            'url': '/geopolitique/cours/seance5'
        },
        {
            'titre': 'L\'Inde : géographie, démographie et puissance émergente',
            'description': 'Analyse complète de l\'Inde : territoire immense, diversité exceptionnelle, économie en croissance et positionnement géopolitique stratégique.',
            'url': '/geopolitique/cours/seance6'
        },
        {
            'titre': 'L\'Amérique latine : influences américaine et européenne',
            'description': 'Histoire complète de l\'influence nord-américaine (1776-présent) et européenne (1980-présent) sur l\'Amérique latine : expansionnisme, néolibéralisme, Mercosur, néopopulisme et géopolitique contemporaine.',
            'url': '/geopolitique/cours/seance7'
        },
        {
            'titre': 'Le Moyen-Orient : Géopolitique et Conflits',
            'description': 'Analyse approfondie des dynamiques géopolitiques du Moyen-Orient, incluant les conflits historiques et contemporains, les enjeux énergétiques, et les influences internationales dans la région.',
            'url': '/geopolitique/cours/seance8'
        }
    ]
    return render_template('geopolitique_index.html', cours=cours_list)

@app.route('/geopolitique/cours/seance1')
def geopolitique_cours_seance1():
    return render_template('geopolitique/cours_seance1.html')

@app.route('/geopolitique/cours/seance2')
def geopolitique_cours_seance2():
    return render_template('geopolitique/cours_seance2.html')

@app.route('/geopolitique/cours/seance3')
def geopolitique_cours_seance3():
    return render_template('geopolitique/cours_seance3.html')

@app.route('/geopolitique/cours/seance4')
def geopolitique_cours_seance4():
    return render_template('geopolitique/cours_seance4.html')

@app.route('/geopolitique/cours/seance5')
def geopolitique_cours_seance5():
    return render_template('geopolitique/cours_seance5.html')

@app.route('/geopolitique/cours/seance6')
def geopolitique_cours_seance6():
    return render_template('geopolitique/cours_seance6.html')

@app.route('/geopolitique/cours/seance7')
def geopolitique_cours_seance7():
    return render_template('geopolitique/cours_seance7.html')

@app.route('/geopolitique/cours/seance8')
def geopolitique_cours_seance8():
    return render_template('geopolitique/cours_seance8.html')


# ============================================
# SECTION 3 : ANALYSE DES RISQUES INTERNATIONAUX
# ============================================

@app.route('/risques')
def risques_index():
    return render_template('risques/cours_risques.html')


# ============================================
# LANCEMENT DE L'APPLICATION
# ============================================

if __name__ == '__main__':
    app.run(debug=True)