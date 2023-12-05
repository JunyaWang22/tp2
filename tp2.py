# Auteurs: Dipika Patel, Junya Wang
# Date: 9 décembre 2023

# def init():

    # changer le contenu HTML de l'élément racine
    racine = document.querySelector("#cb-body")
    racine.innerHTML = """
      <style>
        #jeu table { float:none; }
        #jeu table td { border:0; padding:1px 2px; height:auto; width:auto; }
        #jeu table td img { height:140px; }
      </style>
      <div id="jeu">
        <table>
        </table>
      </div>"""


# Vous devez remplacer le contenu de ce fichier par votre propre code
# tel qu'indiqué dans la description du TP2.  Le code ici correspond
# à l'exemple donné dans la description.

import math
import random
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

CARTES = ['10C.svg', '10D.svg', '10H.svg', '10S.svg', '2C.svg', '2D.svg', '2H.svg', 
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
def td(contenu): return '<td>' + contenu + '</td>'
def img(card): return '<img src="cards/'+ card + '">'

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
                column.append(td(img(val)))
            else:
                column.append(td('test'))
            c += 1
        line.append(tr(''.join(column)))
   
    tbl = table(''.join(line))
    return tbl

elem.innerHTML = init()
