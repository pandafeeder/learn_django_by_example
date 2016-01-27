# learn_Django_by_example

Django has three fundamental parts plus one usefull util Form, Form is kinda familar to Model, but worth being taken as the fourth fundamental part, so:

1. Model Layer(django.db)
2. View Layer(django.views class based view or view function)
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

    More about all/get/filter/exclude

    1. All. I think all is the leatest useful one among the four methods. It simply retrive all objects of a table. No other use. Althoug QuerySet supports chaining, but something like below is really unnecessary.

        ***Individual.objects.all().filter(friends__name__exact="Fry")***

        You should just omit all(), changing it to:

        ***Individula.objects.filter(friends__name__exact="Fry")***

    2. Get. Remember that get directly return a single object according to your query. If your query gets more than one objects satifying it, get will raise a ***MultipleObjectsReturned***exception. So use it when you're sure that only one object will meet your query condition. Like below, we know that this will return the only one objects due to ***unique=True*** is used when defining the ***Individual***'s name field.

        ***Individula.objects.get(name__exact="Fry")***

    3. Filter. Filter will always return a QuerySet, even if only a single object matches the query, it will be a QuerySet containing a single element. Each time you refine a QuerySet, you get a brand-new Query that is in no way bound to the previous QuerySet. Each refinement creates a separate and distinct QuerySet that can be stored, used and reused.

        ***q1 = Individual.objects.filter(species="human")***

        Above will return a QuerySet containing Individuals' with species equal to "human", q1 is reuseable, let's reuse it to find out whose name is "Fry" under species equal to "human"

        ***q1.get(name="Fry")***

        Above will return a single object who is fry.

    4. Exclude. Exclude is the oppsite of filter. It will return a QuerySet which doesn't match the query condition.




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


###shut up and show me the example
1. migrate

   From command line, use the following command to migrate:

   ***python learndjango.py makemigrations learnmodel***

   ***python learndjango.py migrate***

   This will generate the db.sqlite3 database file.

2. create TABLES

   From command line, input:
   
   ***python learndjango.py shell***

   in the python prompt, enter:

   **>>from learnmodel import create**

   **>>create.create()**

   This will save INSERTs into the TABLEs. And we got the following recoreds: 

   ***Company TABLE***

|id   | name         |  description  |
|-----|--------------|---------------|
|1    |PlanetExpress |deliver company|

   ***Species TABLE***

|id   | name         |  characteristic                                                 |
|-----|--------------|-----------------------------------------------------------------|
|1    |Human         |a human                                                          |
|2    |Mutant        |they live in the sewage                                          |
|3    |Robot         |there are many different kinds of robots with different function |
|4    |Reptile       |they are reptile live in the swamp                               |
|5    |Crab          |crab, this is for Zoidberg                                       |

   ***Individual TABLE***

|id   | name                |  age | species | gender |  company      | friends                    |
|-----|---------------------|------|---------|--------|---------------|----------------------------|
|1    |Fry                  | 35   | Human   | MALE   |PlanetExpress  | leela, bender, amy, hermes |
|2    |Leela                | 35   | Mutant  | FAMALE |PlanetExpress  | fry, bender, amy, hermes   |
|3    |Bender               | 17   | Robot   | MALE   |PlanetExpress  | fry, leela                 |
|4    |Zoidberg             | 86   | Crab    | MALE   |PlanetExpress  | NULL                       |
|5    |Amy Wong             | 37   | Human   | FAMALE |PlanetExpress  | leela                      |
|6    |Hubert J. Farnsworth | 210  | Human   | MALE   |PlanetExpress  | hermes                     |
|7    |Hermes               | 54   | Human   | MALE   |PlanetExpress  | hubert                     |


    Now From command line, input:

   ***python learndjango.py shell***

   in the python prompt, enter:

   **>>from learnmodel import query**

   **>>query.test()**

   This will print some query quiz on the screen, input your anwser then hit Enter to make a check. Answers are contained in the [query.py][queryfile] file



###Uncovered topics

   Django.db also has lots of other features, like F, Q objects, raw SQL excutions. Keep in mind that [offical document always has the treature][officalDOM]. 




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
[queryfile]:https://github.com/pandafeeder/learn_django_by_example/blob/master/learnmodel/query.py
[officalDOM]:https://docs.djangoproject.com/en/1.9/topics/db/queries/



## View Layer(class based views in django.views and function based views)

### URL dispatcher

When a request coming from client, how does django decide which view is used to generate response? Of course this is based on the comming url,
but to know about how does django do the mapping bewteen url and view, we have to understand django's url dispatcher mechanism.

#### basic use sample:

**ROOT_URLCONF file**

```python
from django.conf.urls import url, include

urlpatterns = [
    url(r'^myapp1/', include('myapp1.urls', namespace='myapp1')),
    url(r'^myapp2/', include('myapp2.urls', namespace='myapp2')),
]
```


**urls.py file under myapp1**

```python
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^slug1(\w+)', views.slug1view.as_view(), name='slug1'), #use class based view
    url(r'^slug2(?P<slug2_parameter>\d+)', views.slug2view, name='slug2'), #use function based view
    url(r'^slug3', view.slug3view, {extra_parameter: value}, name='slug3'), #pass extra parameter using python dict
]

```
