import random

leeftijd = random.randint(0,80)


if leeftijd < 67:
	print("Je moet nog", 67 - leeftijd, "jaren werken!")
else:
	print("Je bent al", leeftijd-67, "jaren moet pensioen!")