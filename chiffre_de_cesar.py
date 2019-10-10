import string

def chiffrage(liste,cle):
    chaine_chiffre=""
    for caractere in liste:
        valeur_ascii=ord(caractere)
        valeur_ascii=valeur_ascii+cle
        caractere_chiffre=chr(valeur_ascii)
        chaine_chiffre=''.join([chaine_chiffre,caractere_chiffre,])
    return chaine_chiffre

def dechiffrage(liste,cle):
    chaine_dechiffre=""
    for caractere in liste:
        valeur_ascii=ord(caractere)
        valeur_ascii=valeur_ascii-cle
        caractere_dechiffre=chr(valeur_ascii)
        chaine_dechiffre=''.join([chaine_dechiffre,caractere_dechiffre,])
    return chaine_dechiffre

def decoupage(chaine):
    liste = []
    chaine=str(chaine)
    for caractere in chaine:
        liste.append(caractere)
    return liste

def chiffrage_circulaire(liste,cle):
    chaine_chiffre=""
    abc_lower_origine = string.ascii_lowercase
    abc_lower_decale = abc_lower_origine[cle:] + abc_lower_origine[:cle]
    abc_upper_origine = string.ascii_uppercase
    abc_upper_decale = abc_upper_origine[cle:] + abc_upper_origine[:cle]
    for caractere in liste:
        if caractere in string.ascii_letters:
            if(caractere.islower()):
                valeur_ascii=abc_lower_origine.index(caractere)
                caractere_chiffre=abc_lower_decale[valeur_ascii]
            else:
                valeur_ascii=abc_upper_origine.index(caractere)
                caractere_chiffre=abc_upper_decale[valeur_ascii]
        else:
            caractere_chiffre=caractere
        chaine_chiffre=''.join([chaine_chiffre,caractere_chiffre,])
    return chaine_chiffre

def dechiffrage_circulaire(liste,cle):
    chaine_dechiffre=""
    abc_lower_origine = string.ascii_lowercase
    abc_lower_decale = abc_lower_origine[cle:] + abc_lower_origine[:cle]
    abc_upper_origine = string.ascii_uppercase
    abc_upper_decale = abc_upper_origine[cle:] + abc_upper_origine[:cle]
    for caractere in liste:
        if caractere in string.ascii_letters:
            if(caractere.islower()):
                valeur_ascii=abc_lower_decale.index(caractere)
                caractere_dechiffre=abc_lower_origine[valeur_ascii]
            else:
                valeur_ascii=abc_upper_decale.index(caractere)
                caractere_dechiffre=abc_upper_origine[valeur_ascii]
        else:
            caractere_dechiffre=caractere
        chaine_dechiffre=''.join([chaine_dechiffre,caractere_dechiffre,])
    return chaine_dechiffre