# Auteurs: Dipika Patel, Junya Wang
# Date: 12 décembre 2023


# Programme qui consiste à créer un jeu d'Addiction Solitaire. Il comprend un 
# paquet de cartes brassé aleatoirement et des cartes limes à cliquer pour 
# déplacer chaque cartes au bon endroit. Ce jeu permet jusqu'a 3 brassage des 
# cartes qui ne sont toujours pas placés et permet de reinitialiser une partie.  

import math
 
# Création du paquet de cartes en ordre croissant des chiffres de 'A' à 'K'.
paquet = list(range(0,52))
chiffre = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
cartesC=[]
cartesD=[]
cartesH=[]
cartesS=[]
for i in range (len(chiffre)):
    cartesC.append(chiffre[i]+'C.svg')
    cartesD.append(chiffre[i]+'D.svg')
    cartesH.append(chiffre[i]+'H.svg')
    cartesS.append(chiffre[i]+'S.svg')
    
CARTES = cartesC + cartesD + cartesH + cartesS

# Fonction qui prend un paramètre, une liste des numero de cartes,dans le but
# de brasser un paquet de cartes aléatoirement en pigeant un carte en ordre 
# décroissant. 

def brasser(paquet):
    for i in range(len(paquet) -1, -1, -1):
        j = math.floor(random() * (i+1))
        tmp = paquet[i]
        paquet[i] = paquet[j]
        paquet[j] = tmp
    return paquet

# Fonction qui prend un paramètre,contenu, et retourne une balise HTML table. 
def table(contenu): return '<table>' + contenu + '</table>'

# Test unitaire pour fonction table 
def testtable():
    assert table('ffhf') == '<table>ffhf</table>'
testtable()

# Fonction qui prend un paramètre,contenu, et retourne une balise HTML tr. 
def tr(contenu): return '<tr>' + contenu + '</tr>'

# Test unitaire fonction tr 
def testtr():
    assert tr('fvueil') == '<tr>fvueil</tr>'
testtr()

# Fonction qui prend la position d'affichage d'un case et retourne un id sous 
# forme de string.
def case (id_pos): return 'case' + str(id_pos)

# Test unitaire pour fonction case 
def testcase():
    case(3) == 'case3'
testcase()

# Fonction qui prend le contenu et un chaine de caracteres de la position 
# d'affichage et retrourne une balise HTML td.
def td(contenu, id_pos): 
    return '<td' + ' id="' + case(id_pos) +'" onclick="clic('+str(id_pos) + ')"' + '>' + contenu + '</td>'

# Test unitaire pour fonction td 
def testtd():
    assert td('2D.svg',44) == '<td id="44" onclick="clic("44")">2D.svg</td>'
#testtd() # mis en commentaire pour ne pas affecter le jeu

# Fonction qui prend le nom de la carte sous forme de chaine de caractères
# comme paramètre pour l'inserer dans la balise HTML img src permettant de
# faire reference à la bonne image à afficher.
def img(carte): return '<img src="cards/'+ carte + '"/>'

# Test unitaire pour fonction img 
def testimg():
    assert img('AS.svg') == '<img src="cards/AS.svg"/>'
testimg() 

AS = ['AS.svg','AH.svg','AC.svg','AD.svg']
DEUX  = ['2S.svg','2H.svg','2C.svg','2D.svg']
RANGEE = 4
COL = 13   # colonne
cartes = brasser(paquet)
idx_cartes_lime=[] # liste d'index des cartes limes 

# Fonction qui initalise le jeu prenant aucun paramètre et qui retourne un 
# tableau affichant les cartes de jeu en 4 rangées de 13 colonnes placés 
# aléatoirement et qui remplaces les "AS" par des trous (cartes absentes). 
def init():
    idx_paquet=0  
    ligne = []
    
    for _ in range(RANGEE):
        colonne = []
        for _ in range(COL):
            valeur = CARTES[cartes[idx_paquet]]  #cherche la position où 
                         # le nom de la carte est situé dans le paquet brassé.
            
            if valeur in AS:
                colonne.append(td(img('absent.svg'),idx_paquet)) 
                trouver_idx(idx_paquet)
            else:
                colonne.append(td(img(valeur),idx_paquet))
            idx_paquet += 1
        ligne.append(tr(''.join(colonne)))
   
    tableau = table(''.join(ligne))
    return tableau

# Procédure qui prend la valeur case en paramètre et permet de trouver les 
# index des cartes qui deviendront vertes. 
def trouver_idx(case): 
# Cas spécial index se rend à 52.
    position = cartes[case-1]+1
    if position > 51: return
        
    carte_lime = CARTES[cartes[case-1]+1] # position de la carte à devenir 
                                              #lime.
    if case % COL == 0:
        i = 1
        while i < COL*RANGEE:
            idx_cartes_lime.append(cartes.index(i))
            i += COL

    if case % COL != 0 and carte_lime not in AS and carte_lime not in DEUX:
        idx_cartes_lime.append(cartes.index(CARTES.index(carte_lime)))

# Fonction pour le cas spécial des '2' qui prend nom, chaine de charactere, 
# en paramètre, pour determiner les index des cartes "2" qui seront vertes et 
# retourne l'index de la carte "2" à déplacer. 
def placer_deux(nom):
    global DEUX
    index_as=[] #liste des index dans cartes des 'AS'
    
    #Crée une liste avec les '2' qui n'ont pas été cliqués.
    if nom in DEUX:
        DEUX.remove(nom)
        for i in DEUX:
            index_as.append(cartes.index(CARTES.index(i)))
    
   # Retire le style et les index des '2' non-cliqués.
    for i in range(len(index_as)):
        if index_as[i] in idx_cartes_lime:
            document.querySelector('#case'+ 
                                   str(index_as[i])).removeAttribute("style")
            idx_cartes_lime.remove(index_as[i])
            
    # Retourne la position à placer du '2' dans la première colonne.
    for i in range(0, len(CARTES), 13):
        case = document.querySelector('#case' + str(i)).innerHTML
        if case == '<img src="cards/absent.svg">':
            return i       

# Procédure qui sera activé au moment d'un clic sur la page web. Elle prend un 
# parametre, l'identifiant de la position(id_pos),qui est un entier.Elle a pour 
# but de déterminer la carte qui a été choisi et d'appliquer les changements de 
# positions de cartes au bon endroit.
def clic(id_pos):
    global idx_cartes_lime
    case = '#case' + str(id_pos)
    
    # Chercher le nom de la carte dans tag <img> dans cellule <td> avec  
    # l'identificant #case.
    carte = document.querySelector(case).innerHTML
    nom = carte[carte.find('/') + 1:carte.find('">')]

    # Chercher l'index de la carte plus petite que celle choisie vers laquelle 
    # la carte lime se déplacera.
    if nom != 'absent.svg':
        pos = CARTES.index(nom) - 1  # position de la carte avant le nom dans liste CARTES
        index = cartes.index(pos)    # position de la carte dans liste cartes
    
    # Déplace la carte dans le trou au bon index et rend vert la prochaine 
    # carte à déplacer.
    if id_pos in idx_cartes_lime and (index%13 != 12):
        position = index + 1
        if nom in DEUX:
            position = placer_deux(nom)

    # changement des attributs de style pour les cartes à déplacer     
    document.querySelector('#case'+ str(position)).innerHTML ='<img src="cards/' + nom + '">'
    document.querySelector(case).innerHTML = '<img src="cards/absent.svg">'
    document.querySelector(case).removeAttribute("style")
    trouver_idx(id_pos)
    idx_cartes_lime.remove(id_pos)
    lime()

# Procédure qui prend pas de parametre. Elle permet d'appliquer le style CSS 
# "lime" aux cartes á deplacer.
def lime():
    global idx_cartes_lime
    for i in range (len(idx_cartes_lime)):
        case0 = document.querySelector("#"+case(idx_cartes_lime[i]))
        case0.setAttribute("style", "background-color: lime")

# # Fonction qui vérifie si les cartes placées sont bien rangés.
# def aligne():
#     ligne=[[],[],[],[]]
#     indice=0
#     for i in range(0,52,13):
       
#         for j in range(i,i+13):
#             card = document.querySelector("#"+case(j)).innerHTML
#             ligne[indice].append(card[card.find('/') + 1:card.find('">')])
#             ligne[indice].append(j)
#         indice+=1
 
#     for j in range (4):
#         for i in range (COL):
#             if ligne[j][:i]== cartesC[:i] or cartesD[:i] or cartesS[:i] or cartesH[:i]:
#                 return True
# Fonction pour brasser les cartes qui ne sont pas toujours placés en ordre. Il ne prend 
# pas de paramètre
# def brassage():
#     global indice
#     essai = 3
#     while essai > 0:
#         ligne=[[],[],[],[]]
#         nouvelle_ligne=[]
#         c=0
#         for i in range(0,52,13):        
#             for j in range(i,i+13):
#                 card = document.querySelector("#"+case(j)).innerHTML
#                 ligne[indice].append(card[card.find('/') + 1:card.find('">')])
#                 ligne[c].append(j)
#             c += 1

#         for j in range (4):
#             for i in range (COL):
#                 if ligne[j][:i]== cartesC[:i] or cartesD[:i] or cartesS[:i] or cartesH[:i]:
#                     nouvelle_ligne[j].extend(ligne[j][:i])
#                     nouvelle_ligne[j].extend(brasser(ligne[j][i+1:]))               
#         essai -= 1
    
msg = "Vous pouvez encore "
html_brassage = '''<button id="brasser" onclick="brassage()">Brasser les cartes </button>'''
msg1 = " fois"
    # msg2 = "vous devez"
    # msg3 = "Vous ne pouvez plus brasser les cartes"
bouton = msg + html_brassage +msg1 
html_redemarre = """<button id=""redemarre"" onclick=redemarre()> Nouvelle
partie </button>"""

    # if essai > 0:
    #     if idx_cartes_lime == []:
    #         bouton = (msg2 + html_brassage)
    #     else:
    #         bouton = (msg + html_brassage + msg1)
    # else:
    #     bouton = msg3
    # return bouton, nouvelle_ligne

# Procédure qui va reinintialiser le partie avec un nouveau brassage du paquet 
# de carte au complet.
def redemarre():
    brasser(paquet)
    racine.innerHTML = css + init() + bouton + html_redemarre
    lime()

# Fonction pour afficher le résultat. On extrait les chiffres des cartes et
# le compare avec la liste de chiffre en ordre.
# def result():
#     brassage()
#     ligne_chiffre=[]
#     for _ in range(COL):
#         for i in range(RANGEE):
#             ligne_chiffre.append(nouvelle_ligne[i][:3])
#     if ligne_chiffre == chiffre * 4:
#         resultat = print("Vous avez réussi!  Bravo!")
#     if idx_cartes_lime == [] and bouton==False and line != CARTES:
#         resultat = print("Vous n'avez pas réussi à placer toutes les cartes..."
#                         "Essayez à nouveau!")
#     return resultat

racine = document.querySelector('#cb-body')

# Style CSS pour l'affichage des cartes de la page web du jeu. 
css = """
<style>
#cb-body td {
    width: 14vh;
    height: 20vh;
}

#cb-body table td img {
    width: 100%;
    height: 100%;
}
</style>
"""
        
racine.innerHTML = css + init() + bouton + html_redemarre
lime()





   





   


   