# Auteurs: Dipika Patel, Junya Wang
# Date: 9 décembre 2023

import math

racine = document.querySelector('#cb-body')

css = """
<style>
#cb-body { font-size: 24px; }
#cb-body td { border: 1px solid black; }
#cb-body table {
    float: left;
    table-layout: fixed;
    border-collapse: collapse;
}
#cb-body td {
    padding: 0;
    font-family: Helvetica;
    text-align: center;
    vertical-align: center;
    border: 1px solid black;
}

#cb-body td {
    width: 100px;
    height: 100px;
    font-size: 60px;
}

#cb-body table td img {
    display: block;
    object-fit: contain;
    vertical-align: middle;
    width: 100%;
    height: 100%;
}
#cb-body { float: none; }
#cb-body table td { border: 0; padding: 1px 2px; height: auto; }
#cb-body table td img { height: auto; }
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
def case (id_pos): return 'case' + str(id_pos)
def td(contenu, id_pos): 
    return '<td' + ' id="' + case(id_pos) + '" onclick="clic(' + str(id_pos) + ')"' + '>' + contenu + '</td>'
def img(card): return '<img src="cards/'+ card + '"/>'


trou = []
idx_cartes_lime=[]   
cartes = brasser(paquet)
ROW = 4
COL = 13
c = 0

#def val(cartes,indice,position):
#    return CARTES[cartes[indice]+position]  

    
def init():
    global cartes,ROW, COL, c

    line = []
    
    for _ in range(ROW):
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

def lime():
    for i in range (len(idx_cartes_lime)):
        case0 = document.querySelector("#"+case(idx_cartes_lime[i]))
        case0.setAttribute("style", "background-color: lime")

def trouver_idx(case):
# card_val =val(cartes,c-1,1)
        p = cartes[case-1]+1
        if p > 51: return
        
        carte_lime = CARTES[p]
        if case % COL == 0:
            i = 1
            #breakpoint()
            while i < COL*ROW:
                idx_cartes_lime.append(cartes.index(i))
                i += COL

        if case % COL != 0 and not(carte_lime).startswith('A') and not(carte_lime).startswith('2'):
            idx_cartes_lime.append(cartes.index(CARTES.index(carte_lime)))

def clic(id_pos):
    case = '#case' + str(id_pos)
    
    # Get the <img> tag inside <td> cell and extract image name
    card = document.querySelector(case).innerHTML
    name = card[card.find('/') + 1:card.find('">')]
    
    # Get index of the next to which we can moved the highlighted card
    p = CARTES.index(name) - 1
    index = cartes.index(p)
    
    # Move the card to the trou cell and trou its prior position
    
    if id_pos in idx_cartes_lime :
        document.querySelector('#case' + str(index+1)).innerHTML = '<img src="cards/' + name + '">'
        document.querySelector(case).innerHTML = '<img src="cards/absent.svg">'
        document.querySelector(case).removeAttribute("style")
        trouver_idx(id_pos)
        idx_cartes_lime.remove(id_pos)
        lime()

def aligne():
    for i in range (COL):
        if column[:i]== cartesC[:i] or cartesD[:i] or cartesS[:i] or cartesH[:i]:
            return True
      
# def cartes_index(carte):
#    return cartes.index(CARTES.index(carte))
#def clic(case):
   # lime_card.replace('absent.svg')

def brassage():
    msg = "Vous pouvez encore "
    html_brassage = '''
    <button id="brasser" onclick="brassage()"> Brasser les cartes </button>
    <br>
    <br>'''
    msg1 = "fois"
    return msg + html_brassage + msg1
    #print("hello")
    # elem.innerHTML = css + init() + msg + html_brassage + html_redemarre


def redemarre():
    brasser(CARTES)
    
def result():
    if line == CARTES:
        print("Vous avez réussi!  Bravo!")
    if idx_cartes_lime == [] and brassage()==False and line != CARTES:
        print("Vous n'avez pas réussi à placer toutes les cartes... Essayez à nouveau!")


html_redemarre = '''
<button id="redemarre" onclick="redemarre()"> Nouvelle partie </button>
<br>
<br>'''

racine.innerHTML = css + init() + brassage() + html_redemarre
lime()
