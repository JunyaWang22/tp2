# Ok il semble plus lisisble mais pas vraiment...

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
def case (id_pos): return 'case' + str(id_pos)
def td(contenu, id_pos): 
    return '<td' + ' id=' + case (id_pos) + '>' + contenu + '</td>'
def td_clic(nv_absent,carte,contenu):
    return '<td' + ' id=' + case (nv_absent) +'" onclick="clic(' + str(nv_absent)+','+str(carte) + ')"' + contenu + '</td>'
def img(card): return '<img src="cards/'+ card + '"/>'

trou = []
idx_cartes_lime=[]   
cartes = brasser(paquet)
ROW = 4
COL = 13

#def val(cartes,indice,position):
#    return CARTES[cartes[indice]+position]  

def lime(liste):
    for i in range (len(liste)):
        case0 = document.querySelector("#"+case(liste[i]))
        case0.setAttribute("style", "background-color: lime")

def clic(nv_absent,carte):
    img_cartes.pop(i)
    img_cartes.insert(img('absent.svg'),carte)
    img_cartes.pop(nv_absent)
    img_cartes.insert(nv_absent,td(img('absent.svg'),nv_absent))
    lime(index_lime)
    
def init():
    global img_cartes,index_lime
    line=[]
    index_lime=[]
    cartes = brasser(paquet)
    absent_liste=[]
    img_cartes=[0]*52
    for i in range(len(paquet)):
        id_carte = paquet[i]
        if id_carte != 0 and id_carte != 13 and id_carte != 26 and id_carte != 39:
            img_cartes[i]=td(img(CARTES[id_carte]),i)
        else:
            #img_cartes[i]=td(img('absent.svg'),i)
            absent_liste.append(i)
            if i == 0 or i == 13 or i == 26 or i == 39:
                index_lime.extend([1,14,27,40])
                img_cartes[i]=td_clic(paquet.index(1),img(CARTES[1]),img('absent.svg'))
                img_cartes[i]=td_clic(paquet.index(14),img(CARTES[14]),img('absent.svg'))
                img_cartes[i]=td_clic(paquet.index(27),img(CARTES[27]),img('absent.svg'))
                img_cartes[i]=td_clic(paquet.index(40),img(CARTES[40]),img('absent.svg'))
            else:
                index_lime.append(paquet[i-1]+1)
                img_cartes[i]=td_clic(paquet[i-1]+1,img(CARTES[paquet[i-1]+1]),img('absent.svg'))
                #print(img_cartes[i])
                #print(index_lime)
    for i in range(0,52,13):
        line.append(tr(''.join(img_cartes[i:i+13])))
   
    tableau = table(''.join(line))
    print(tableau)
    return tableau



racine.innerHTML = css + init() #+ brassage() + html_redemarre
lime(index_lime)










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
    for i in range(0,52,13):
        line.append(tr(''.join(img_cartes[i:i+13])))
   
    tableau = table(''.join(line))
    return tableau
