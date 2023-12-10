def init():
    global cartes,ROW, COL
    c = 0 

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
                p = cartes[c-1]+1
                if p > 51: return
                
                carte_lime = CARTES[p]
                if c % COL == 0:
                    i = 1
                    while i < COL*ROW:
                        idx_cartes_lime.append(cartes.index(i))
                        i += COL

                if c % COL != 0 and not(carte_lime).startswith('A') and not(carte_lime).startswith('2'):
                    idx_cartes_lime.append(cartes.index(CARTES.index(carte_lime)))
                    column.append(td_clic(clic(column,c%COL,cartes.index(carte_lime),td(img(carte_lime)))))

            c += 1
        line.append(tr(''.join(column)))
   
    tableau = table(''.join(line))
    return tableau
def clic(liste, absent,nv_absent,carte):
    liste.pop(absent)
    liste.insert(absent,td(img(carte),absent))
    liste.pop(nv_absent)
    liste.insert(nv_absent,td(img('absent.svg'),nv_absent))

# une façon bcp plus lisible correspond list(range(52)) à CARTES
def init():
    line=[]
    index_lime=[]
    cartes = brasser(paquet)
    img_cartes=[0]*52
    for i in range(len(paquet)):
        id_carte = paquet[i]
        if id_carte == 0 or id_carte == 13 or id_carte == 26 or id_carte == 39:
            img_cartes[i]=td(img('absent.svg'),i)
            if i == 0 or i == 13 or i == 26 or i == 39:
                index_lime.extend([1,14,27,40])
            else:
                index_lime.append(paquet[i-1]+1)
        else:
            img_cartes[i]=td(img(CARTES[id_carte]),i)
    for i in range(0,52-13,13):
        line.append(tr(''.join(str(img_cartes[i:i+13]))))
   
    tableau = table(''.join(line))
    return tableau
