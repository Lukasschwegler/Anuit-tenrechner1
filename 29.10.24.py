# Werte eingeben

kreditbetrag = int(input("Kreditbetrag "))
jahre = int(input("Laufzeit "))
zinssatz = float(input("Zinssatz in % "))
monatliche_rate = int(input("Monatlicherate "))
sonder_tilgung = int(input("Sondertilgung "))

def kreditrate_berechnen(kreditbetrag, zinssatz, jahre):
    # Zinssatz von Prozent in Dezimal umwandeln und monatlichen Zinssatz berechnen
    r = (zinssatz / 100) / 12
    # Anzahl der Monate berechnen
    n = jahre * 12
    # Annuitätenformel zur Berechnung der monatlichen Rate
    monatliche = (kreditbetrag * r * (1 + r) ** n) / ((1 + r) ** n - 1)
    return monatliche

#Anuitätenformel 
# Funktion aufrufen und Ergebnis ausgeben
monatliche = kreditrate_berechnen(kreditbetrag, zinssatz, jahre)
#print(f"Die monatliche Rate beträgt: {monatliche:.2f} Euro")

#Zinsen
# Berechnen der gesamten Zinsen im Jahr
jahr_zins = kreditbetrag * zinssatz / 100
#print(f"f string: Die Zinsen im Jahr : {jahr_zins:.2f} Euro")
# Berechnen der gesamten Zinsen
zinsen = kreditbetrag * zinssatz / 100 * jahre
#print(f"f string: Die gesamten Zinsen : {zinsen:.2f} Euro")

#Anuität
# Berechnen der Annuität
anu = monatliche_rate  * 12
#print(f"f string: Die Annuität beträgt : {anu:.2f} Euro")

#Sondertilgung
# Sondertilgung im Jahr
#print(f"f string: Die Sondertilgung im Jahr beträgt : {sonder_tilgung:.2f} Euro")
# Sondertilgung gesamt
gesamt = sonder_tilgung * jahre
#print(f"f string: Die Sondertilgung beträgt : {gesamt:.2f} Euro")

#Tilgung
# Tilgung ohne Sondertilgung im Jahr
rest = anu - jahr_zins 
#print(f"f string: Die Tilgung beträgt im Jahr {rest:.2f} Euro")
# Tilgung ohne Sondertilgung gesamt
rest1 = rest * jahre
#print(f"f string: Die Tilgung beträgt gesamt {rest1:.2f} Euro")

#Mit Restschuld
#Die Restschuld beträgt nach dem Ende der Laufzeit
rest2 = kreditbetrag - rest1
#print(f"f string: Die Restschuld beträgt nach dem Ende der Laufzeit: {rest2:.2f} Euro ")
# Restschuld mit Sondertilgung
tilgen = rest2 - gesamt
#print(f"f string: Die Restschuld mit Sondertilgung beträgt: {tilgen:.2f} Euro")

# Die Gesamtkosten
gesamtkosten = kreditbetrag + zinsen


# Beispiel-Dictionary
# Färben des Dictionary
farbe = "\033[90m"  # Grau
reset = "\033[0m"  # Zurücksetzen der Farbe
mein_dict = {

    "Kreditbetrag": f"{farbe}Meine Kreditbetrag beträgt: {kreditbetrag:.2f}€{reset}",
    "Laufzeit": f"{farbe}Meine Laufzeit beträgt: {jahre:.2f} Jahre{reset}",
    "Monatsrate": f"{farbe}Meine Monatsrate beträgt: {monatliche_rate:.2f}€{reset}",
    "Rate bei Volltilgung": f"{farbe}Die Volltilgung beträgt: {monatliche:.2f}€{reset}",
    "Zinssatz": f"{farbe}Meine Zinssatz beträgt: {zinssatz:.2f} %{reset}",
    "Die gesamten Zinsen": f"{farbe}Die gesamten Zinsen betragen: {zinsen:.2f}€{reset}",
    "Annuität": f"{farbe}Die Annuität beträgt: {anu:.2f}€{reset}",
    "Sondertilgung im Jahr": f"{farbe}Die Sondertilgung beträgt: {sonder_tilgung:.2f}€{reset}",
    "Sondertilgung gesamt": f"{farbe}Die gesamte Sondertilgung beträgt: {gesamt:.2f}€{reset}",
    "Restschuld ohne Sondertilgung": f"{farbe}Die Restschuld beträgt nach dem Ende der Laufzeit: {rest2:.2f}€{reset}",
    "Restschuld mit Sondertilgung": f"{farbe}Die gesamte Restschuld mit Sondertilgung beträgt: {tilgen:.2f}€{reset}",
    "Gesamtkosten": f"{farbe}Die Gesantkosten betragen: {gesamtkosten:.2f}€{reset}",
}

# Manuelle Formatierung
for key, value in mein_dict.items():
    print(f"{key}: {value}")








