from models import Individual, Company, Species

#modify companey
planetExpress = Company(name="PlanetExpress", description="deliver company")
planetExpress.save()

#modify species
human = Species(name="Human", characteristic="a human")
mutant = Species(name="Mutant", characteristic="they live in the sewage")
robot = Species(name="Robot", characteristic="there are many different kinds of robots with different function")
reptile = Species(name="Reptile", characteristic="they are reptile live in the swamp")
crab = Species(name="Crab", characteristic="crab, this is for Zoidberg")

#modify characters of Furturama
fry = Individual(name="Fry", age=37, species=human, gender='M', company=planetExpress)
leela = Individual(name="Leela", age=37, species=mutant, gender='F', company=planetExpress)
bender = Individual(name="Bender", age=17, species=robot, gender='M', company=planetExpress)
zoidberg = Individual(name="Zoidberg", age=86, species=crab, gender='M', company=planetExpress)
amy = Individual(name="Amy Wong", age=35, species=human, gender='F', company=planetExpress)
hubert = Individual(name="Hubert J. Farnsworth", age=210, species=human, gender='M', company=planetExpress)
hermes = Individual(name="Hermes", age=54, species=human, gender='M', company=planetExpress)

def create():
    """create calls save on the objects to save them to database
    for ForeignKey and ManyToManyField field, their saving must antecede using"""
    for i in [human, mutant, robot, reptile, crab]:
	i.save()
    for i in [fry, leela, bender, zoidberg, amy, hubert, hermes]:
	i.save()
    fry.friends.add(leela, bender, amy, hermes)
    leela.friends.add(fry, bender, amy, hermes)
    #oh, poor Zoidberg
    #zoidberg.friends.add(None)
    bender.friends.add(fry, leela)
    amy.friends.add(leela)
    hermes.friends.add(hubert)
    hubert.friends.add(hermes)
