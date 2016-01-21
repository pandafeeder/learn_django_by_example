from .models import Individual, Company, Species

def test():
    while True:
	user_input = raw_input("How old is Fry?\n")
	try:
	    exec("aws = "+user_input)
	except NameError:
	    print "Input Error, Retry:"
	else:
	    if aws == 37:
		print "bingo"
		break
	    else:
		print "Wrong answer, Retry:"



















"""
answers:
1. Individual.objects.get(name="Fry").age
"""
