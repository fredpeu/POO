import random as rdm

couleurs = ('CARREAU', 'COEUR', 'TREFLE', 'PIQUE')
noms = ['7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
valeurs = {'7': 7, '8': 8, '9': 9,'10': 10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}

class Carte:
    def __init__(self, nom, couleur):
        self.nom=nom
        self.couleur=couleur
    def valeur(self):
        return valeurs[self.nom]
    def __gt__(self,other):
        return self.valeur()>other.valeur()
    def __eq__(self,other):
        return self.nom==other.nom
    def __repr__(self):
        return self.nom+' de '+self.couleur

class JeuDeCartes:
    def __init__(self):
        self.jeu=[]
        self.jeu1=[]
        self.jeu2=[]
        for i in noms:
            for j in couleurs:
                self.jeu.append(Carte(i,j))
        rdm.shuffle(self.jeu)
    def distribue(self):
        for i in range(len(self.jeu)//2):
            self.jeu1.append(self.jeu[i])
            self.jeu2.append(self.jeu.pop())
class Bataille:
    def __init__(self,joueur1,joueur2):
        self.joueur1=joueur1
        self.joueur2=joueur2
        self.bataille=JeuDeCartes()
    def lancer(self):
        while True:
            if self.bataille.jeu1==[] or self.bataille.jeu2==[]:
                break
            input(self.joueur1+' et '+self.joueur2+'...sortez vos cartes!')
            print(self.joueur1,self.bataille.jeu1[-1])
            print(self.joueur2,self.bataille.jeu2[-1])
            if self.bataille.jeu1[-1]>self.bataille.jeu2[-1]:
                self.bataille.jeu1.insert(0, self.bataille.jeu1.pop())
                self.bataille.jeu1.insert(0, self.bataille.jeu2.pop()) 
            else:
                self.bataille.jeu2.insert(0, self.bataille.jeu2.pop())
                self.bataille.jeu2.insert(0, self.bataille.jeu1.pop())
            print(self.bataille.jeu1,self.bataille.jeu2)
        if self.bataille.jeu1!=[]:
            print(self.joueur1+' a gagné!')
        else:
            print(self.joueur2+' a gagné!')

# a=JeuDeCartes()
# print(a.jeu)
        
carte1=Carte('7','CARREAU')
carte2=Carte('Valet','CARREAU')

cartex=Carte(rdm.choice(noms),rdm.choice(couleurs))
# print(cartex)

new_game=Bataille('kiki','bibi')
new_game.bataille.distribue()
new_game.lancer()