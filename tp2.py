# Auteurs: Dipika Patel, Junya Wang
# Date: 9 décembre 2023

import math

elem = document.querySelector('#cb-body')

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
elem.innerHTML = css
deck = list(range(0,52))

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

def shuffle(deck):
    for i in range(len(deck) -1, -1, -1):
        j = math.floor(random() * (i+1))
        tmp = deck[i]
        deck[i] = deck[j]
        deck[j] = tmp
    return deck

def table(contenu): return '<table>' + contenu + '</table>'
def tr(contenu): return '<tr>' + contenu + '</tr>'
def case (id_pos): return 'case' + str(id_pos)
def td(contenu, id_pos): 
    return '<td' + ' id=' + case (id_pos) + '>' + contenu + '</td>'
def img(card): return '<img src="cards/'+ card + '">'

empty = []
casel=[]

def init():
    ROW = 4
    COL = 13
    c = 0
    cartes = shuffle(deck)
    line = []
    
    for _ in range(ROW):
        column = []
        for _ in range(COL):
            val = CARTES[cartes[c]]
            
            if(not val.startswith('A')):
                column.append(td(img(val),c))
            else:
                column.append(td(img('absent.svg'),c))
                if c % 13 != 0 and ((CARTES[cartes[c-1]+1]).startswith('2') is False):
                	casel.append(cartes.index(CARTES.index(CARTES[cartes[c-1]+1])))

            c += 1
        line.append(tr(''.join(column)))
   
    tbl = table(''.join(line))
    return tbl

elem.innerHTML += init()

for i in range (len(casel)):
    case0 = document.querySelector("#"+case(casel[i]))
    case0.setAttribute("style", "background-color: lime")
