from random import randint

print("CARTA-FORBICI-SASSO CONTRO TROLLMIND")
print("developed by Il Sultano")
print("\n Come ti chiami ominide?")
nome = input ()
print("\n Wow! Bel nome di me**a " + nome + " complimenti!")

print("\n Comunque fatti tuoi, proviamo a giocare un po'. Sei in grado di scegliere un'arma? Non è difficile dai...forse")

punteggio_giocatore = 0
punteggio_Piton = 0
comando = ""
while(comando != "si"):

  print("\n SCEGLI UN'ARMA")
  armi = [ "carta", "forbici", "sasso" ]
  for arma in armi:
        print ("")
        print(arma)
  
  print ("\n Premi 0 per Carta, 1 per Forbici, 2 per Sasso")
  
  numero_scelto = int(input())
  arma_scelta = armi[numero_scelto]
  print("Bravo, pessima scelta " + arma_scelta + "!")
  
  arma_Piton = ""
  numero_Piton = randint(0,2)
  arma_Piton = armi[numero_Piton]
  
  print("\n Ora tocca a me...lasciami pensare a come farti il c**o!")
  print("\n...ho fatto la mia scelta!")
  verdetto = ""
  
  if(arma_scelta == "carta" and arma_Piton == "sasso"):
     vedetto = nome + "Hai vinto! Hai più c**o che anima + nome!"
     punteggio_giocatore = punteggio_giocatore + 1 
  
  if(arma_scelta == "forbici" and arma_Piton == "carta"):
     vedetto = nome + "Hai vinto! Sicuramente sarai brutto forte + nome!"
     punteggio_giocatore = punteggio_giocatore + 1 
  
  if(arma_scelta == "sasso" and arma_Piton == "forbici"):
     vedetto = nome + "Hai vinto! Ti venisse il caghetto + nome"
     punteggio_giocatore = punteggio_giocatore + 1 
  
  if (arma_scelta == arma_Piton):
      verdetto = "Pareggio, volevi " + nome + " eh?! "
  
  if(verdetto == ""):
      verdetto = "Si dai bravo, hai perso, s**a!!"
      punteggio_Piton = punteggio_Piton + 1
  
  print("\n PREMI PER SCOPRIRE SE HAI VINTO")
  input()
  print("\n Ho scelto " + arma_Piton + "!")
  print(verdetto)
  print("\n PUNTEGGIO:")
  print(nome + " - Piton : " + str(punteggio_giocatore) + "-" + str(punteggio_Piton))
  print("\n Quindi ti sei stancato di perdere? si o no?")
  comando = input()

print("\n Ehy " +  nome + " Sei un cagasotto! Dove scappi?!")





   

   


