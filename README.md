# learn_Django_by_example

Django has three fundamental parts plus one usefull util Form, Form is kinda familar to Model, but worth being taken as the fourth fundamental part, so:

1. Model Layer(django.db)
2. View Layer(django.views)
3. Template Layer(django.template)
4. Form(django.form)

## Model Layer(django.db)

### basic use sample:
```python
from django.db.models import Model

class Individual(models.Model): 
    GENDER = (                 
        ('M', 'male'),
        ('F', 'female'),
    )
    #id      = models.AutoField(primary_key=True)     #1
    name     = models.CharField(max_length=50)        #2
    age      = models.PositiveSmallIntegerField()
    species  = models.CharField(max_length=50) 
    gender   = models.CharField(max_length=1, choices=GENDER)
    company  = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)
    friends  = models.ManyToManyField('self')         

    #objects = models.Manager()                       #3

    def __str__(self):
        return self.name

    class Meta:                                       #4
        ordering = ('age',)
        
class Company(models.Model): 
    pass
```
1. This auto-incrementing key is auto added by Django,you can make your own field(primary_key=True), only one pk=True field for a whole Model. 
2. Filed coresponds to COLUMN of a TABLE in database. [There're plenty filed types in Django][field]. And there're many [options for each kind of Field][fieldop]. Among those, [vilidators][vilidator] is a good way to vilidate our input data.There's a special catagory field: relationship Field. [ForeignKey][mto], [ManyToManyField][mtm], [OneToOneField][oto]
3. This is auto added by Django, [Manager][manager] provides interfaces(by constructing QuerySet) for makeing queries, at least one Manager is provided for every unabstract model. You can change objects to other names your like with querying with the name your specified. MyModel.objects.all() => MyModel.yourname.all(). Also you can customize your own Manager(). You can define many custom Manager in one Model.
4. [Meta option.][meta]. abstract=True makes a model Abstract Model act as a parent class which can be herited. There're many Meta options in Django.


### query
When model code is done. You can use [Django provided command][migrate] to deploy your database.

Making query is now what we are facing.
Query involves three basic parts. When you have a database, how can you:

1. Creating data objects and saving them to database

    Creating objects is simple, just like any python object's instantiation, and calling save() method to save it to database. You can also use Manager's API ->create to create and save an object in one time.[[1]]

2. Saving changes to objects 

    Saving changes to objects is just like updating an attribute of any python object, then save() method will update it to database.[[2]] You should pay attension to creating or updateing relationship fields: [ForeignKey][mto], [ManyToManyField][mtm], [OneToOneField][oto]

3. Retrieving data objects from database.
     
    By constructing a [QuerySet][queryset] using a Manager() defined in a model. QuerySet provides all(), filter(), get(), exclude() methods to query data objects from database.[[3]]. QuerySet supports chaining filters, lazy evaluation, Python's array-slicing syntax. Keyword arguments of filter(), get(), exclude() are called "Filed Lookups". They have the form like: 

    ***field__lookuptype=value***. 

    ***field*** is an attribute of a model object, **__** has two underscores, ***lookuptype*** is provided by Django's built-in django.db.modles.Lookup class. 

    For a Lookup to span a relationship, just use the filed name of the related fields across models, then two underscore, then the field name you want to query of the ralated model, you can even use lookup after queried field, like:

    ***Individual.objects.filter(company__name__iexact='Planet Express')***

    There's a sepcial case for ForeignKey, you can use the ForeignKey Field name followed by ***_id=value*** to get the objects with Foreign Modle with ***pk=value***. Like:

    ***Individual.objects.filter(company_id=1)***

    And for the related model of ForeignKey field, the object of the model has a relating_name_set, attribute, like:

    ***express = Company.objects.get(pk=1); express.individual_set.all()*** will output all individual objects whose company is express. 

###create objects

1. ordinary objects with no relation field is easily created. Just like ordinary creatation of python objects.
    instance = Class(args=xxxx)

2. ForeignField

    You must save an object before it can be assigned to a foreign key relationship. Let's say that an employee and a company is ManyToOne relationship(a company could have lots of employees, but a employee should work for only one company). In this case:

    ***acompany = Company(name="PlanetExpress", description="deliver things")***
    ***fry = Employee(name="Fry", age=35, company=acompany)***

    Above will raise a error when assign acompany to fry's company, you have to save acompany first before use it.

3. ManyToManyField
    
    You have to save an objects before associating it with manytomany relationship. Let's say that fry and leela are friends,

    ```python
    class Individual(modles.Model): 
        ...
        name = models.CharField(max_length=50)
        friends = models.ManyToManyField('self')
        ...

    fry = Individual(name="Fry")
    leela = Individual(name="Leela")
    #you have to save it first
    fry.save()
    leela.save()
    fry.friends.add(leela)
    leela.friends.add(fry)
    ```













[field]:https://docs.djangoproject.com/en/1.9/ref/models/fields/#model-field-types
[vilidator]:https://docs.djangoproject.com/en/1.9/ref/validators/
[fieldop]:https://docs.djangoproject.com/en/1.9/ref/models/fields/#field-options
[mto]:https://docs.djangoproject.com/en/1.9/topics/db/examples/many_to_one/
[mtm]:https://docs.djangoproject.com/en/1.9/topics/db/examples/many_to_many/
[oto]:https://docs.djangoproject.com/en/1.9/topics/db/examples/one_to_one/
[manager]:https://docs.djangoproject.com/en/1.9/topics/db/managers/
[meta]:https://docs.djangoproject.com/en/1.9/ref/models/options/
[migrate]:https://docs.djangoproject.com/en/1.9/topics/migrations/
[retrieve]:https://docs.djangoproject.com/en/1.9/topics/db/queries/#retrieving-objects
[1]:https://docs.djangoproject.com/en/1.9/topics/db/queries/#creating-objects
[2]:https://docs.djangoproject.com/en/1.9/topics/db/queries/#saving-changes-to-objects
[3]:https://docs.djangoproject.com/en/1.9/topics/db/queries/#retrieving-objects
[queryset]:https://docs.djangoproject.com/en/1.9/ref/models/querysets/#django.db.models.query.QuerySet
