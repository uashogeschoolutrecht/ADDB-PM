t = int(input('Geef een getal'))
som = 0

for n in range(t):
	som = som + n

print(som)


#Om hier een activiteiten-diagram bij de maken kun je het omzetten naar een while-loop. 
#Voor de volledigheid is de hele code weer gegeven.


t = int(input('Geef een getal'))
som = 0

n = 0
while n<t:
	som = som + n 
	n = n + 1

print(som)

