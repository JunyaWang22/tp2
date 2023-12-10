# Variables globales :
#
# tour      entier indiquant à qui c’est le tour, 1 pour "x", 2 pour "o"
# grille    contenu de la grille de jeu, un 0 indique une case vide
# occupees  nombre de cases occupées
# coups     tableau de position des coups joués

def symboleJoueur(joueur):
    if joueur == 1:
        return '<img src="https://codeboot.org/4.1.2/images/x.png">'
    else:
        return '<img src="https://codeboot.org/4.1.2/images/o.png">'

def nomJoueur(joueur):
    return 'x' if joueur == 1 else 'o'

def autreJoueur(joueur):  # 1 -> 2, 2 -> 1
    return 3-joueur

def element(id):
    return document.querySelector('#' + id)

def case(index):
    return element('case'+str(index))

alignements = [struct(pas= +1, departs= [0,3,6]),
               struct(pas= +3, departs= [0,1,2]),
               struct(pas= +4, departs= [0]),
               struct(pas= -2, departs= [6])]

def victoire():

    for alignement in alignements:

        pas = alignement.pas

        for pos in alignement.departs:
            joueur = grille[pos]
            if joueur != 0:
                for i in range(1, 3):
                    if grille[pos+i*pas] != joueur:
                        break
                else:
                    return joueur  # il y a un gagnant

    return 0  # pas de gagnant

def activer(id, oui):
    if oui:
        element(id).removeAttribute('disabled')
    else:
        element(id).setAttribute('disabled', 'true')

html = """
   <style>

     #cb-body table {
         border-collapse: collapse;
         table-layout: fixed;
         line-height: 1;
     }

     #cb-body td {
         width: 100px;
         height: 100px;
         border: 1px solid black;
         vertical-align: center;
         text-align: center;
         font-family: Helvetica;
         font-size: 80px;
     }

     #cb-body img {
         width: 90px;
     }
   </style>

   <div id="main">

     <button onclick="init()">Nouvelle partie</button> 
     <button id="undo" onclick="undo()">Undo</button>  
     <button id="redo" onclick="redo()">Redo</button>  

     <br><br>

     <table>
       <tr>
         <td id="case0" onclick="clic(0)"></td>
         <td id="case1" onclick="clic(1)"></td>
         <td id="case2" onclick="clic(2)"></td>
       </tr>
       <tr>
         <td id="case3" onclick="clic(3)"></td>
         <td id="case4" onclick="clic(4)"></td>
         <td id="case5" onclick="clic(5)"></td>
       </tr>
       <tr>
         <td id="case6" onclick="clic(6)"></td>
         <td id="case7" onclick="clic(7)"></td>
         <td id="case8" onclick="clic(8)"></td>
       </tr>
     </table>

   </div>

 </body>
"""

def init():

    global tour, grille, occupees, coups

    document.querySelector('#cb-body').innerHTML = html

    tour = 1
    grille = [0] * 9
    occupees = 0
    coups = []
    for i in range(9):
        case(i).innerHTML = ''
    activer('redo', False)
    activer('undo', False)

def clic(index):
    global coups, occupees, tour
    if grille[index] == 0:

        grille[index] = tour
        case(index).innerHTML = symboleJoueur(tour)

        coups = coups[:occupees] # oublier coups futurs
        coups.append(index)

        activer('undo', True)
        activer('redo', False)

        gagnant = victoire()
        if gagnant != 0:
            alert(nomJoueur(gagnant) + ' est le gagnant!')
            init()
        else:
            tour = autreJoueur(tour)
            occupees += 1
            if occupees == 9:
                alert('match nul!')
                init()

def undo():
    global occupees, tour
    if occupees > 0:
        occupees -= 1
        grille[coups[occupees]] = 0
        case(coups[occupees]).innerHTML = ''
        tour = autreJoueur(tour)
        if occupees == 0:
            activer('undo', False)
        activer('redo', True)

def redo():
    global occupees, tour
    if occupees < len(coups):
        grille[coups[occupees]] = tour
        case(coups[occupees]).innerHTML = symboleJoueur(tour)
        occupees += 1
        tour = autreJoueur(tour)
        if occupees == len(coups):
            activer('redo', False)
        activer('undo', True)

init()
