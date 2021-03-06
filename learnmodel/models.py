from django.db import models
from django.utils.encoding import python_2_unicode_compatible

#Let's make some models for the beloved Carton eposide Futurama


class TimeStampModel(models.Model):
	"""abstract=True makes this model be a parent model of models which inherited 
	this model. Thus every sub-models would has fields created and modified"""
	created  = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def as_dict(self):

	    dict = {}
	    #exclude ManyToOneRel, which backwards to ForeignKey
	    field_names = [field.name for field in self._meta.get_fields() if 'ManyToOneRel' not in str(field)]
	    for name in field_names:
		field_instance = getattr(self, name)
		if field_instance.__class__.__name__ == 'ManyRelatedManager':
		    dict[name] = field_instance.all()
		    continue
		dict[name] = field_instance
	    return dict

	class Meta:
		abstract = True 


@python_2_unicode_compatible
class Individual(TimeStampModel):
	"""model for every individual character in Futurama, let's just take Robot as species"""
	GENDER  = (
		('M', 'male'),
		('F', 'female'),
	)
	name    = models.CharField(max_length=50, unique=True)
	age     = models.PositiveSmallIntegerField()
	species = models.ForeignKey('Species', on_delete=models.CASCADE)
	gender  = models.CharField(max_length=1, choices=GENDER)
	company = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)
	friends = models.ManyToManyField('self')

	def __str__(self):
		return self.name

	class Meta:
		ordering = ('age',)


@python_2_unicode_compatible
class Company(TimeStampModel):
	"""model for companies in Futurama"""
	name        = models.CharField(max_length=50)
	description = models.CharField(max_length=200)	

	def __str__(self):
		return self.name


@python_2_unicode_compatible
class Species(TimeStampModel):
	"""model for species in Futurama"""
	name = models.CharField(max_length=50)
	characteristic = models.CharField(max_length=100)

	def __str__(self):
		return self.name
