# TA Tuan An
# groupe 3.1
#######################
# importations
#######################
MOTS = ['aimable','barracuda','bavard','chercheur','cocorico','dernier','egalite','fanfaronner','garage','hasard','huluberlu','infini','moitie','nulle','present','rare','savant']
from mots import MOTS
from figures_pendu import FIGURES_PENDU
import random
#######################
# fonctions
#######################
MOTS = ['aimable','barracuda','bavard','chercheur','cocorico','dernier','egalite','fanfaronner','garage','hasard','huluberlu','infini','moitie','nulle','present','rare','savant']

def choisit_mot(l:list)->str:
    index = random.randint(0,len(l)-1)
    return l[index]
     
def est_dans(ch:str, c:str)-> bool:
    for i in range(len(c)):
        if ch[i]==c:
            return True
    return False

def input_lettre(props:str):
    while True:
        choix= input('Proposez une lettre:')
        if len(choix)> 1:
            print("Proposez une seul lettre, s'il vous plait")
        elif choix in props:
            print("Vous avez déja proposé cette lettr")
        elif est_dans("0123456789",choix):
            print("n'est pas une lettre")
        else:
            return choix
def dessine_pendu(n:int)-> None:
    FIGURES_PENDU = ['''
   +---+
   |   |
       |
       |
       |
       |
==========''','''
   +---+
   |   |
   O   |
       |
       |
       |
==========''','''
   +---+
   |   |
   O   |
   |   |
       |
       |
==========''','''
   +---+
   |   |
   O   |
  /|   |
       |
       |
==========''','''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
==========''','''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
==========''','''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
==========''']
    
def affiche_erreurs(erreurs:str)-> None:
    for i in range (len(erreurs)):
        print(erreurs[i], end= ' ')
def affiche_correctes(correctes:str, mot_secret:str):
    res=''
    for m in range(len(mot_secret)):
        for c in range (len(correctes)):
            if mot_secret[m]==correctes[c]:
                res = res + mot_secret[m]
            else:
                res= res + '_'
    print(res)
     
                
            
          
               
                
            
        
    
    
    

   
        
            