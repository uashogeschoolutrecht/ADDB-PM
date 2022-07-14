naam = input("Wat is je naam? ")
print("Hello", naam)

lengte_naam = len(naam)

print("Je naam bestaat uit:", lengte_naam, "letters")

#We hadden ook met een + de stukken tekst aan elkaar kunnen plakken, maar dan moeten we wel 
#de variabele lengte_naam naar een String casten. Dan krijg je:
 
print("Je naam bestaat uit: " + str(lengte_naam) + " letters")
#merk op dat je met dit + je niet vanzelf spaties erbij krijgt, die zetten we er dus zelf tussen

leeftijd = input("Wat is je leeftijd? ")
leeftijd = int(leeftijd)
verschil = abs(leeftijd - 32)

print("Wij schelen", verschil, "jaar in leeftijd.")