# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.

import math
# from xml.dom.minidom import Document

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

CARTES = [
 '10C.svg', '10D.svg', '10H.svg', '10S.svg', '2C.svg', '2D.svg', '2H.svg', 
 '2S.svg', '3C.svg', '3D.svg', '3H.svg', '3S.svg', '4C.svg', '4D.svg', 
 '4H.svg', '4S.svg', '5C.svg', '5D.svg', '5H.svg', '5S.svg', '6C.svg', 
 '6D.svg', '6H.svg', '6S.svg', '7C.svg', '7D.svg', '7H.svg', '7S.svg', 
 '8C.svg', '8D.svg', '8H.svg', '8S.svg', '9C.svg', '9D.svg', '9H.svg', 
 '9S.svg', 'AC.svg', 'AD.svg', 'AH.svg', 'AS.svg', 'JC.svg', 'JD.svg', 
 'JH.svg', 'JS.svg', 'KC.svg', 'KD.svg', 'KH.svg', 'KS.svg', 'QC.svg', 
 'QD.svg', 'QH.svg', 'QS.svg']

def shuffle(deck):
    for i in range(len(deck) -1, -1, -1):
        j = math.floor(random() * (i+1))
        tmp = deck[i]
        deck[i] = deck[j]
        deck[j] = tmp
    return deck

def table(contenu): return '<table>' + contenu + '</table>'
def tr(contenu): return '<tr>' + contenu + '</tr>'
# def tr(contenu): return '<td>' + contenu + '</td>'
def td(contenu, id_pos): 
    return '<td' + ' id=' + 'case' + str(id_pos) + '>' + contenu + '</td>'
def img(card): return '<img src="cards/'+ card + '">'

empty = []

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
                column.append(td('',c))
               # breakpoint()
                empty.append(c-1)
            c += 1
        line.append(tr(''.join(column)))
   
    tbl = table(''.join(line))
    return tbl

elem.innerHTML += init()

def card_value(card):
    card = card.split('.')[0]
    ranks = '2345678910JQKA'
    suits = 'CDHS'

    rank = card[:-1]
    suit = card[-1]

    return ranks.index(rank), suits.index(suit)

def find_higher_card(card, card_list):
    current_rank, current_suit = card_value(card)

    # Find a card with a higher rank and the same suit
    for other_card in card_list:
        other_rank, other_suit = card_value(other_card)

        inc = 2 if current_rank == 8 else 1

        # if other_suit == current_suit and other_rank == current_rank + inc:
        #     return other_card

        if other_suit == current_suit and other_rank+inc == current_rank + inc:
            value = card_value(other_card)
            print(value)

    # If no higher card with the same suit is found
    return None
voisin = []
for x in empty:
    voisin.append(CARTES[deck[x]])   #finds the card left to empty
for v in voisin :
    find_higher_card(v,voisins)
    # for x in deck: 
    #     print(CARTES[deck[x]])
              #case = document.querySelector('#'+ str(id_pos))
    #case.setAttribute("style", "background-color: lime")

#for i in voisin:
    
    