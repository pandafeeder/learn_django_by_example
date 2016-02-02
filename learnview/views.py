from django.http import  HttpResponse, HttpResponseNotFound, Http404
from learnmodel.models import Individual, Company, Species
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.core.urlresolvers import reverse
from itertools import izip
from django.views.generic import TemplateView, DetailView, ListView

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

#followings are class based views

class temp_view(TemplateView):
    "demonstrate use of TemplateView"
    template_name = "learnview/learnview_index.html"


class myGetQuerySetMixin(object):
    #use get_queryset decide which TABLE to be listed, 
    #this will overide the assingment to model attribut of this class
    #queryset attribut is another alternative
    #specifying model = MODELNAME is just short for queryset = MODELNAME.objects.all()
    def get_queryset(self):
	if self.kwargs['cate'] == 'individual':
	    self.kwargs['model_name'] = 'Individual'
	    return Individual.objects.all()
	elif self.kwargs['cate'] == 'company':
	    self.kwargs['model_name'] = 'Company'
	    return Company.objects.all()
	elif self.kwargs['cate'] == 'species':
	    self.kwargs['model_name'] = 'Species'
	    return Species.objects.all()
	else:
	    #raise a Http404 excepton at any point will make django repsone a 404 response,
	    #this is really handy
	    raise Http404("Page not found")


class list_view(myGetQuerySetMixin, ListView):
    "demonstrate use of ListView"
    template_name = "learnview/list_view.html"
	    
    #overide get_context_data to pass some extra content to context
    def get_context_data(self, **kwargs):
	context = super(list_view, self).get_context_data(**kwargs)
	context['model_name'] = self.kwargs['model_name']
	return context

class detail_view(myGetQuerySetMixin, DetailView):
    "demonstrate use of DetailView"
    template_name = "learnview/detail_view.html"

    def get_context_data(self, **kwargs):
	context = super(detail_view, self).get_context_data(**kwargs)
	fieldnames = [i.name for i in self.object._meta.get_fields()]
	print fieldnames
	context['object_dict'] = self.object.as_dict()
	return context
