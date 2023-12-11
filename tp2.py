# Auteurs: Dipika Patel, Junya Wang
# Date: 9 décembre 2023

import math

racine = document.querySelector('#cb-body')

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
racine.innerHTML = css
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

# Fonction qui prend un paramètre dans le but de brasser un paquet de cartes aléatoirement allant en ordre décroissant. 

def brasser(paquet):
    for i in range(len(paquet) -1, -1, -1):
        j = math.floor(random() * (i+1))
        tmp = paquet[i]
        paquet[i] = paquet[j]
        paquet[j] = tmp
    return paquet

def table(contenu): return '<table>' + contenu + '</table>'
def tr(contenu): return '<tr>' + contenu + '</tr>'
def case (id_pos): return 'case' + str(id_pos)
def td(contenu, id_pos): 
    return '<td' + ' id="' + case(id_pos) + '" onclick="clic(' + str(id_pos) + ')"' + '>' + contenu + '</td>'
def img(card): return '<img src="cards/'+ card + '"/>'


trou = []
idx_cartes_lime=[]   
cartes = brasser(paquet)
RANGEE = 4
COL = 13
c=0
 

   
def init():
    global cartes,RANGEE, COL,c

    line = []
    
    for _ in range(RANGEE):
        column = []
        for _ in range(COL):
            value = CARTES[cartes[c]]
            
            if(not value.startswith('A')):
                column.append(td(img(value),c))
            else:
                column.append(td(img('absent.svg'),c))
                trou.append(cartes.index(c))
                trouver_idx(c)
            c += 1
        line.append(tr(''.join(column)))
   
    tableau = table(''.join(line))
    return tableau


def trouver_idx(case):

# cas special index se rend a 52
        position = cartes[case-1]+1
        if position > 51: return
        
        carte_lime = CARTES[cartes[case-1]+1]
        if case % COL == 0:
            i = 1
            while i < COL*RANGEE:
                idx_cartes_lime.append(cartes.index(i))
                i += COL

        if case % COL != 0 and not(carte_lime).startswith('A') and not(carte_lime).startswith('2'):
            idx_cartes_lime.append(cartes.index(CARTES.index(carte_lime)))

# Fonction pour cas special des '2' 
def placer_deux(name):
    liste_deux = ['2S.svg','2H.svg','2C.svg','2D.svg']
    index_as=[]
    
    #créer une liste avec les '2' restants de celui cliqué
    if name in liste_deux:
        liste_deux.remove(name)
        for i in liste_deux:
            index_as.append(cartes.index(CARTES.index(i)))
    
   # Retirer le style et les index des '2' non-cliqués
    for i in range(len(index_as)):
        if index_as[i] in idx_cartes_lime:
            document.querySelector('#case'+ str(index_as[i])).removeAttribute("style")
            idx_cartes_lime.remove(index_as[i])
            
     # Retourne la position a placer du '2' 
    for i in range(0, len(CARTES), 13):
        case = document.querySelector('#case' + str(i)).innerHTML
        if case == '<img src="cards/absent.svg">':
            return i       
        
def clic(id_pos):
    case = '#case' + str(id_pos)
    
    # Chercher le nom de la carte dans tag <img> dans cellule <td> 
    card = document.querySelector(case).innerHTML
    name = card[card.find('/') + 1:card.find('">')]
    
    # Chercher l'index de la carte plus petite vers laquelle la carte lime se deplacera 
    pos = CARTES.index(name) - 1
    if pos != 'absent.svg':
        index = cartes.index(pos)
    
    # Déplace la carte dans le trou au bon index et rend vert la prochaine carte à deplacer.
    liste_deux=['2S.svg','2H.svg','2C.svg','2D.svg']
    if id_pos in idx_cartes_lime :
        position = index + 1
        if name in liste_deux:
            position = placer_deux(name)
              
        document.querySelector('#case' + str(position)).innerHTML = '<img src="cards/' + name + '">'
        document.querySelector(case).innerHTML = '<img src="cards/absent.svg">'
        document.querySelector(case).removeAttribute("style")
        trouver_idx(id_pos)
        idx_cartes_lime.remove(id_pos)
        lime()

def lime():
    for i in range (len(idx_cartes_lime)):
        case0 = document.querySelector("#"+case(idx_cartes_lime[i]))
        case0.setAttribute("style", "background-color: lime")
    # for i in range(1,len(CARTES),13):
    #     if name == CARTES[i] and trou[i-1] == True:
    #         document.querySelector("#case"+ str(i-1)).innerHTML = '<img src="cards/' + name + '">'
    #         document.querySelector(case).innerHTML = '<img src="cards/absent.svg">'
            

# def aligne():
#     for i in range (COL):
#         if column[:i]== cartesC[:i] or cartesD[:i] or cartesS[:i] or cartesH[:i]:
#             return True
# def aligner(RANGEE):
#     for i in range(RANGEE):
#         for i in range(len(RANGEE)-1):
#             carte_courante = RANGEE[i]
#             carte_voisine = RANGEE[i+1]
#             valeur_courante, couleur_courante= carte_courante//4, carte_courante%4            
#             valeur_voisine, couleur_voisine= carte_voisine//4, carte_voisine%4
            
#             if valeur_voisine-valeur_courante != 1:
#                 return False
#             if couleur_courante != couleur_voisine:
#                 return False 
#     return True 

                
      
# def cartes_index(carte):
#    return cartes.index(CARTES.index(carte))
#def clic(case):
   # lime_card.replace('absent.svg')

# def brassage(): 
    # aligner(RANGEE)
    # return "hello"
    #print("hello")
    # elem.innerHTML = css + init() + msg + html_brassage + html_redemarre

msg = "Vous pouvez encore "
html_brassage = '''<button id="brasser" onclick="brassage()">Brasser les cartes </button>'''
msg1 = "fois\n"
bouton = (msg + html_brassage + msg1)
html_redemarre = "<button id=""redemarre"" onclick=redemarre()> Nouvelle partie </button>"

def redemarre():
    brasser(paquet)
    racine.innerHTML = css + init() + bouton + html_redemarre
    lime()
    
# def result():
#     if line == CARTES:
#         print("Vous avez réussi!  Bravo!")
#     if idx_cartes_lime == [] and bouton==False and line != CARTES:
#         print("Vous n'avez pas réussi à placer toutes les cartes... Essayez à nouveau!")
        
racine.innerHTML = css + init() + bouton + html_redemarre
lime()
