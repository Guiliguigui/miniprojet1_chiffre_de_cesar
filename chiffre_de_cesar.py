def chiffrage(caractere):
    valeur_ascii=ord(caractere)
    valeur_ascii=valeur_ascii+8
    caractere_chiffre=chr(valeur_ascii)
    return caractere_chiffre

def dechiffrage(caractere):
    valeur_ascii=ord(caractere)
    valeur_ascii=valeur_ascii-8
    caractere_dechiffre=chr(valeur_ascii)
    return caractere_dechiffre