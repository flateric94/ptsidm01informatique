# -*- coding: utf-8 -*-
"""
Éditeur de Spyder

Ceci est un script temporaire.
"""

def encodage_naif(L):
    return L+L+L

#print(encodage_naif([1,1,0]))


def decodage_naif(L):
    if len(L) % 3 != 0:
        return (False,[])
    else:
        ListeMessages=[]
        TailleMessage=int(len(L) / 3)
        Increment=0
        Message=[]

        for k in range(0,int(len(L))):
                Message.append(L[k])
                Increment=Increment+1
                if Increment==TailleMessage:
                    ListeMessages.append(Message)
                    Increment=0
                    Message=[]

        for k in range(0,int(len(ListeMessages))):
            if ListeMessages.count(ListeMessages[k]) > 1:
                return (True, ListeMessages[k])
        
        return (False, [])

def bit_de_parite(L):
    somme_des_uns=L.count(1)
    #print(somme_des_uns)
    if somme_des_uns % 2 == 0 :
        return(0)
    else:
        return(1)
    

def encodage_b2p(L):
    listeResultat=[]
    for k in range(0,int(len(L))):
        listeResultat.append(L[k])
    
    listeResultat.append(bit_de_parite(L))
    return(listeResultat)
        

def decodage_b2p(L):
    if int(len(L))<=1:
        return(False,[])
    else:
        bit_de_parite_recu=L[-1]
        message_a_decoder=L
        del message_a_decoder[-1]
        bit_de_parite_calcule=bit_de_parite(message_a_decoder)
        if bit_de_parite_calcule==bit_de_parite_recu:
            return(True,message_a_decoder) 
        else:
            return(False,[])
 

def encodage_Hamming_segment(L):
    if int(len(L))==4:
        message=[]
        message.append(bit_de_parite([L[0],L[1],L[3]]))
        message.append(bit_de_parite([L[0],L[2],L[3]]))
        message.append(L[0])
        message.append(bit_de_parite([L[1],L[2],L[3]]))
        message.append(L[1])
        message.append(L[2])
        message.append(L[3])
        return(message)

def decodage_Hamming_segment(L):
    if int(len(L))!=7:
        return(False,[])
    if bit_de_parite([L[3],L[4],L[5],L[6]])!=0:
        return(False,L)
    if bit_de_parite([L[1],L[2],L[5],L[6]])!=0:
        return(False,L)
    if bit_de_parite([L[0],L[2],L[4],L[6]])!=0:
        return(False,L)
    return(True,L)

def decodage_Hamming_segment_explique(L):
    if int(len(L))!=7:
        return(False,[])
    message_explique=[]
    message_explique.append(bit_de_parite([L[3],L[4],L[5],L[6]]))
    message_explique.append(bit_de_parite([L[1],L[2],L[5],L[6]]))
    message_explique.append(bit_de_parite([L[0],L[2],L[4],L[6]]))
    return(message_explique)







#8) 
#print(encodage_Hamming_segment([1,0,1,1]))
#resultat encodage 1011 : [0, 1, 1, 0, 0, 1, 1]
print(decodage_Hamming_segment([0, 1, 1, 0, 0, 1, 1]))
print(decodage_Hamming_segment_explique([0, 1, 1, 0, 0, 1, 1]))
print(decodage_Hamming_segment([1, 0, 1, 0, 0, 1, 1]))
print(decodage_Hamming_segment_explique([1, 0, 1, 0, 0, 1, 1]))



#print(encodage_Hamming_segment([1,0,1,1]))
#print(encodage_Hamming_segment([0,1,0,1]))    
#print(decodage_Hamming_segment(encodage_Hamming_segment([0,1,0,1])))    
#print(decodage_Hamming_segment([0,1,1,0,0,1,1]))    
#print(decodage_Hamming_segment([0,1,1,0,0,1,1]))    
#print(decodage_Hamming_segment([1,1,1,0,1,1,0]))        
#print(decodage_b2p([0,1,0,1,0]))

#print(encodage_b2p([1,0,1,1]))
    
#print(bit_de_parite([1,0,1,1]))
#print(bit_de_parite([0])) 
#print(bit_de_parite([1])) 
#print(bit_de_parite([1,1,1,1])) 
#print(bit_de_parite([0,0,0])) 
#print(bit_de_parite([1,0,0])) 
#print(bit_de_parite([54851])) 


#print(decodage_naif([0,0,0,1]))
#print(decodage_naif([0,1,1,0,1,0]))
#print(decodage_naif([1,0,1,0,0,1]))

#[0,1] [1,0] [1,0]

#[0,1,1,0,1,0]
#[[0,1],[1,0],[1,0]]


#print(decodage_naif([0,1,0,0,0,1,0,0,0,1,1,0]))
#print(decodage_naif([0,1,0,0,1,0,0,1,0]))
#print(decodage_naif([1,1,0,0,1,0]))

#print(decodage_naif([1,1,0]))
#print(decodage_naif([1,0,1]))
#print(decodage_naif([0,1,1]))

#print(decodage_naif([1,1,1]))


#[0,1,0,0] [0,1,0,0] [0,1,1,0]


#print(decodage_naif([0,1,0,0,0,1,0,0,0,1,1]))