from django.http import  HttpResponse
from learnmodel.models import Individual, Company, Species


def index(request):
    individuals = Individual.objects.all()
    company     = Company.objects.all()
    species     = Species.objects.all()
    
    individual_dict = { i.id : i.name for i in individuals}
    company_dict    = { i.id : i.name for i in company}
    species_dict    = { i.id : i.name for i in species}

    return HttpResponse([individual_dict, company_dict, species_dict])
