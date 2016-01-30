from django.http import  HttpResponse
from learnmodel.models import Individual, Company, Species
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.urlresolvers import reverse
from itertools import izip

def index(request):
    "view function is responsible for returning a HttpResponse object"
    return HttpResponse("welcome to learn Django by example's learnview page")

def allrecord(request):
    "demonstrate use HttpResponse file liky"
    individuals = Individual.objects.all()
    company     = Company.objects.all()
    species     = Species.objects.all()
    
    individual_dict = { i.id : str(i.name) for i in individuals}
    company_dict    = { i.id : str(i.name) for i in company}
    species_dict    = { i.id : str(i.name) for i in species}
 
    #way to reverse url besides 'url' tag in template and get_absolute_url() method
    url = reverse('learnview:allrecord')
    response = HttpResponse()

    #izip, iteritems are for the sake of performance
    for i in izip(['Individual', 'Species', 'Company'], [individual_dict, species_dict, company_dict]):
	response.write('<p>'+i[0]+'</p>')
	for k,v in i[1].iteritems():
	    response.write('<p>'+', '.join([str(k),v])+'</p>')
    response.write(url)

    return response

def individual(request, pk):
    "demonstrate use of shortcut get_object_or_404"
    indi = get_object_or_404(Individual, pk=pk)
    dict = indi.as_dict()
    response = HttpResponse()
    for k,v in dict.iteritems():
	if v.__class__.__name__ == 'QuerySet':
	    vlist =[]
	    for i in v:
		vlist.append(str(i))
	    response.write('<p>'+k+': '+', '.join(vlist)+'</p>')
	    continue
	response.write('<p>'+k+': '+str(v)+'</p>')
    return response
