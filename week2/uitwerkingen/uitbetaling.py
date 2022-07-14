def uitbetaling(uren, tarief):
	return uren*tarief


met_floats = uitbetaling(4.5, 12.50)
print("Het salaris is", met_floats)

met_ints = uitbetaling(7,20)
print("Het salaris is", met_ints)