# Auteurs: Dipika Patel, Junya Wang
# Date: 9 décembre 2023

import math

elem = document.querySelector('#cb-body')

css = """
<style>
#cb-body { font-size: 24px; }
#cb-body td { border: 1px solid black; }
#cb-body table {
    float: center;
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
def tdid(id_pos, contenu):
    return '<td' + ' id=' + case (id_pos) + "onclick=" + contenu + '>' + '</td>'

empty = []
COL=13
ROW=4

def val(cartes,indice,position):
    return CARTES[cartes[indice]+position]  
    
def init():
    global casel, line
    casel=[]
    c = 0
    line = []
    cartes = shuffle(deck)
    for _ in range(ROW):
        global column
        column = []
        for _ in range(COL):
            val = CARTES[cartes[c]]
            
            if(not val.startswith('A')):
                column.append(td(img(val),c))
            else:
                column.append(td(img('absent.svg'),c))
                lime_card = CARTES[cartes[c-1]+1]
                if c % COL == 0:
                    i = 1
                    while i < COL*ROW:
                        casel.append(cartes.index(i))
                        i += COL

                if c % COL != 0 and (not (lime_card).startswith('A')) and  (not (lime_card).startswith('2')):    
                    casel.append(cartes.index(CARTES.index(lime_card)))
                    print(casel)
                    sleep(0.3)
                    print(column)
                    print(c)
                    column.pop(c%COL)
                    column.insert(c%COL,td(img(lime_card),c%COL))
                    #line.append(tdid((cartes.index(CARTES.index(lime_card))),"lime_card.replace('absent.svg')"))
                    # onclick = clic(cartes.index(CARTES.index(lime_card)))
            c += 1
        line.append(tr(''.join(column)))
    

    tbl = table(''.join(line))
    return tbl    
        # onclick = clic(cartes.index(CARTES.index(lime_card)))

#def clic():
    

def aligne():
    for i in range (COL):
        if column[:i]== cartesC[:i] or cartesD[:i] or cartesS[:i] or cartesH[:i]:
            return True
      
# def cartes_index(carte):
#    return cartes.index(CARTES.index(carte))
#def clic(case):
   # lime_card.replace('absent.svg')

def brassage():
    print("hello")
    elem.innerHTML = css + init() + msg + html_brassage + html_redemarre


def redemarre():
    elem.innerHTML = css + init() + msg + html_brassage + html_redemarre

def result():
    if line == CARTES:
        print("Vous avez réussi!  Bravo!")
    if casel == [] and brassage()==False and line != CARTES:
        print("Vous n'avez pas réussi à placer toutes les cartes... Essayez à nouveau!")

    
msg = "Vous pouvez encore "
html_brassage = '''
<button id="but" onclick="brassage()"> Brasser les cartes </button>
<br><span id="msg"></span>
<br>'''
html_redemarre = '''
<button id="but" onclick="redemarre()"+"removeAttribute"> Nouvelle partie </button>
<br><span id="msg"></span>
<br>'''
elem.innerHTML = css + init() + msg + html_brassage + html_redemarre #+ result()

for i in range(len(casel)):
        case0 = document.querySelector("#"+case(casel[i]))
        case0.setAttribute("style", "background-color: lime")
    #<td>id="case0" onclick="removeAttribute"
