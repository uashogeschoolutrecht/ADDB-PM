maand = int(input("Wat is het nummer van de maand?"))

if maand >= 3 and maand <= 5:
	print("Lente")
elif maand >= 6 and maand <= 8:
	print("Zomer")
elif maand >=9 and maand <= 11:
	print("Herfst")
else:
	print("Winter")