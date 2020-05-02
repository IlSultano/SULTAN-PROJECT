print("INDOVINA IL NUMERO")
print("developed by Adel Salah")
print("\n Come ti chiami piccolo cerbiatto?")
nome_giocatore = input()
print("\n Ti volevano proprio male i tuoi genitori per averti dato un nome simile, comunque in bocca al lupo " + nome_giocatore + "!")

numero_segreto = 8 
print("\n PROVA AD INVODINARE IL NUMERO DA 1 A 10, SE CI BECCHI VINCI UN SALAME A DOMICILIO !")

while(True):
  numero_inserito = int(input())
  if(numero_inserito == numero_segreto):
    print("Bravo, dove vuoi che te lo porti il salame, " + nome_giocatore + "?")
    dove_salame = input()
    break
  if(numero_inserito > numero_segreto):
    print("\n ...fuochino, fuochino... prova un po' meno!")
  if(numero_inserito < numero_segreto):
    print("\n...fuocherello, prova un po' di più!")
print("\n Alla prossima " + nome_giocatore + ", anzi spero di no!")
