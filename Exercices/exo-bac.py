class Joueur:
    def __init__(self,pseudo,identifiant,equipe):
        self.pseudo=pseudo
        self.equipe=equipe
        self.id=identifiant
        self.nb_de_tirs_emis=0
        self.liste_id_tirs_recus=[]
        self.est_actif=True
    
    def tire (self):
        if self.est_actif==True:
            self.nb_de_tirs_emis+=1
    
    def est_determine(self):
        return self.nb_de_tirs_emis>500
    
    def subit_un_tir(self,id_recu):
        if self.est_actif==True:
            self.est_actif==False
            self.liste_id_tirs_recus.append(id_recu)
    
    def redevenir_actif(self,id_recu):
        if self.est_actif==False:
            self.est_actif==True
            # self.liste_id_tirs_recus.remove(id_recu)
    def nb_de_tirs_recus(self):
        return len(self.liste_id_tirs_recus)
    
################# 


class Carte:
    def __init__(self, val, coul):
        self.valeur = val
        self.coul= coul

c7 = Carte(7, "coeur")
c8 = Carte(8, "pique")

def initialiser() :
    jeu = []
    for c in ["coeur", "carreau", "trefle", "pique"] : # couleur carte
        for v in range(2,15) : # valeur carte
            carte_cree = Carte(v,c)
            jeu.append(carte_cree)
    return jeu



def comparer(carte1, carte2):
    if carte1.valeur > carte2.valeur :
        return 1
    elif carte1.valeur < carte2.valeur :
        return -1
    else :
        return 0