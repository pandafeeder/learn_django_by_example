from .models import Individual, Company, Species

questions_asw = {
    "How old is Fry?" : 37,
    "Who works for PlanetExpress and is mutant" : u"Leela",
    "Who are not human?" : [u"Bender", u"Leela", u"Zoidberg"],
    "Who has no friends?" : u"Zoidberg",
    "List individuals whose age is between 15 and 40 in acend order" : [u"Bender", u"Amy Wong", u"Fry", u"Leela"]
}


def test():
    for question, answer in questions_asw.items():
	while True:
	    user_input = raw_input(question+"\n")
	    try:
		exec("asw = "+user_input)
	    except :
		print "Input Error, Retry:"
	    else:
		if asw == answer:
		    print asw
		    print "Bingo!"
		    break
		else:
		    print "Your answer is:" 
		    print asw
		    print "Wrong answer, Retry:"




"""
answers:
1. Individual.objects.get(name="Fry").age
2. Individual.objects.get(company=Company.objects.get(name="PlanetExpress"), species=Species.objects.get(name="Mutant")).name
3. [i.name for i in Individual.objects.exclude(species=Species.objects.get(name="Human"))]
4. Individual.objects.get(friends=None).name
5. [i.name for i in Individual.objects.filter(age__gt=15, age__lt=40).order_by('age')]
"""
