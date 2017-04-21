class Handlungsoption:
	def __init__(self, nummer, aktion, konsequenz):
		self.nummer = nummer
		self.aktion = aktion
		self.konsequenz = konsequenz

	def getAktion(self):
		return self.aktion

	def getNummer(self):
		return self.nummer

	def getKonsequenz(self):
		return self.konsequenz

class Knoten:
	def __init__(self, beschreibung, listeDerHandlungsoptionen = []):
		self.beschreibung = beschreibung
		self.listeDerHandlungsoptionen = listeDerHandlungsoptionen

	def addHandlungsoption(self, handlungsoption):
		self.listeDerHandlungsoptionen.append(handlungsoption)

	def zeigeBeschreibung(self):
		print(self.beschreibung)

	def zeigeHandlungsoptionen(self):
		for Handlungsoption in self.listeDerHandlungsoptionen:
			print(Handlungsoption.getNummer(), ".", Handlungsoption.getAktion())

	def getKonsequenz(self, eingabe):
		for Handlungsoption in self.listeDerHandlungsoptionen:
			if eingabe == Handlungsoption.getNummer():
				return Handlungsoption.getKonsequenz()
		return False



option1 = Handlungsoption(1, "Aktion 1_1", "weiter")
option2 = Handlungsoption(2, "Aktion 1_2", "game over")

option3 = Handlungsoption(1, "Aktion 2_1", "nix")
option4 = Handlungsoption(2, "Aktion 2_2", "weiter")

knoten1 = Knoten("Knotenbeschreibung", [option1, option2])
knoten2 = Knoten("Beschreibung 2", [option3, option4])

knotenliste = [knoten1, knoten2]
aktuelleKnotenNummer = 0

gameOver = False

while not gameOver:
	aktuellerKnoten = knotenliste[aktuelleKnotenNummer]
	aktuellerKnoten.zeigeBeschreibung()
	aktuellerKnoten.zeigeHandlungsoptionen()
	benutzerEingabe = int(input(">>"))
	konsequenz = aktuellerKnoten.getKonsequenz(benutzerEingabe)
	if konsequenz == "game over":
		gameOver = True
		print("Sie haben verloren")
		break

	if konsequenz == "weiter":
		aktuelleKnotenNummer += 1
		if aktuelleKnotenNummer > len(knotenliste)-1:
			print("Sie haben gewonnen")
			gameOver = True
			break

	if konsequenz == "nix" or not konsequenz:
		print("Versuchen Sie es noch einmal!")


