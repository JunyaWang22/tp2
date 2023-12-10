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

def brasser(paquet):
    for i in range(len(paquet) -1, -1, -1):
        j = math.floor(random() * (i+1))
        tmp = paquet[i]
        paquet[i] = paquet[j]
        paquet[j] = tmp
    return paquet

def table(contenu): return '<table>' + contenu + '</table>'
def tr(contenu): return '<tr>' + contenu + '</tr>'
def case (id_pos): return '#case' + str(id_pos)
def td(contenu, id_pos): 
    return '<td' + ' id="' + case(id_pos) + '" onclick="clic(' + str(id_pos) + ')"' + '>' + contenu + '</td>'
def img(card): return '<img src="cards/'+ card + '"/>'
    
trou = []
index_lime=[]   
cartes = brasser(paquet)
ROW = 4
COL = 13

#def val(cartes,indice,position):
#    return CARTES[cartes[indice]+position]  

    
def init():
    global cartes
    i = 0 

    line = []
    
    for _ in range(ROW):
        column = []
        for _ in range(COL):
            value = CARTES[cartes[i]]
            
            if paquet[i] % COL != 0:
                column.append(td(img(value),i))
            else:
                column.append(td(img('absent.svg'),i))
                trou.append(cartes.index(i))
                trouver_lime(i)
            i += 1
        line.append(tr(''.join(column)))
   
    tableau = table(''.join(line))
    return tableau

def lime():
    for i in range (len(index_lime)):
        case0 = document.querySelector(case(index_lime[i]))
        #case0.setAttribute("style", "background-color: lime")

def trouver_lime(case):
    A_ou_2 = [0,13,26,39,1,14,27,40]
    position = cartes[case-1]+1
    
    if case % COL == 0:
        i = 1
        while i < COL*ROW:
            index_lime.append(cartes.index(i))
            i += COL

    if case % COL != 0 and position not in A_ou_2:
        index_lime.append(cartes.index(position))

def clic(id_pos):   
    
    carte = document.querySelector(case).innerHTML
    a_change = carte[carte.find('/') + 1:carte.find('">')]
    # print(a_change)
    p = CARTES.index(a_change) - 1
    index = cartes.index(p)
    
    # Move the card to the trou cell and trou its prior position
    
    if id_pos in index_lime:
        document.querySelector('#case' + str(index+1)).innerHTML = '<img src="cards/' + name + '">'
        document.querySelector(case).innerHTML = '<img src="cards/absent.svg">'
        document.querySelector(case).removeAttribute("style")
        trouver_idx(id_pos)
        index_lime.remove(id_pos)
        lime()

def aligne():
    for i in range (COL):
        if column[:i]== cartesC[:i] or cartesD[:i] or cartesS[:i] or cartesH[:i]:
            return column[i+1:]
      
# def cartes_index(carte):
#    return cartes.index(CARTES.index(carte))
#def clic(case):
   # lime_card.replace('absent.svg')

def brassage():
    essai = 1
    while essai <= 3:
        aligne()
        for _ in range (ROW):
            cartei=brasser([i+1:])
            for j in cartei:
                column[:i].append(CARTES[j])
    essai += 1
    
    msg = "Vous pouvez encore "
    html_brassage = '''<button id="brasser" onclick="brassage()">Brasser les cartes </button>'''
    msg1 = str(essai) + "fois\n"
    return msg + html_brassage + msg1
    


html_redemarre = "<button id=""redemarre"" onclick=redemarre()> Nouvelle partie </button>"

def redemarre():
    brasser(paquet)
    racine.innerHTML = css + init() + brassage() + html_redemarre
    lime()
    
def result():
    if line == CARTES:
        print("Vous avez réussi!  Bravo!")
    if idx_cartes_lime == [] and brassage()==False and line != CARTES:
        print("Vous n'avez pas réussi à placer toutes les cartes... Essayez à nouveau!")
        
racine.innerHTML = css + init() + brassage() + html_redemarre
lime()
