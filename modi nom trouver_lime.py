
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
