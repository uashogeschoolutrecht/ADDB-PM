def jaaromzet(omzet):
	if omzet < 800000:
		print('harder werken!')
	elif omzet > 1000000:
		print('jippie, tijd voor feest!')
	else:
		print('prima jaartje')

jaaromzet(1200000)


def jaaromzet_met_return(omzet):
	if omzet < 800000:
		return 'harder werken!'
	elif omzet > 1000000:
		return 'jippie, tijd voor feest!'
	else:
		return 'prima jaartje'


uitkomts = jaaromzet_met_return(850000)
print(uitkomts)