def chiffrage(liste):
    chaine_chiffre=""
    for caractere in liste:
        valeur_ascii=ord(caractere)
        valeur_ascii=valeur_ascii+8
        caractere_chiffre=chr(valeur_ascii)
        chaine_chiffre=''.join([chaine_chiffre,caractere_chiffre,])
    return chaine_chiffre

def dechiffrage(liste):
    chaine_dechiffre=""
    for caractere in liste:
        valeur_ascii=ord(caractere)
        valeur_ascii=valeur_ascii-8
        caractere_dechiffre=chr(valeur_ascii)
        chaine_dechiffre=''.join([chaine_dechiffre,caractere_dechiffre,])
    return chaine_dechiffre

def decoupage(chaine):
    liste = []
    chaine=str(chaine)
    for caractere in chaine:
        liste.append(caractere)
    return liste
