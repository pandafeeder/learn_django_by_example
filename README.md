# learn_Django_by_example

Django has three fundamental parts plus 1 usefull util Form, Form is kindof familar to Model, worth being taken as the fourth fundamental part, so:

1. Model Layer(django.db)
2. View Layer(django.views)
3. Template Layer(django.template)
4. Form(django.form)

## Model Layer(django.db)

### basic use sample:
```
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
3. This is auto added by Django, [Manager][manager] provides interfaces for makeing queries, at least one Manager is provided for every unabstract model. You can change objects to other names your like with querying with the name your specified. MyModel.objects.all() => MyModel.yourname.all().Also you can customize your own Manager(). You can define many custom Manager in one Model.
4. [Meta option.][meta]. abstract=True makes a model Abstract Model act as a parent class which can be herited. There're many Meta options in Django.


### query
When model code is done. You can use [Django provided command][migrate] to deploy your database.

Making query is now what we are facing.
Query involves three basic parts. When you have a database, how can you:

1. Creating data objects and saving them to database

    Creating objects is simple, just like any python object's instantiation, and calling save() method to save it to database. You can also use Manager's API ->create to create and save an object in one time.

2. Saving changes to objects 

    Saving changes to objects is just like updating an attribute of any python object, then save() method will update it to database. You should pay attension to creating or updateing relationship fields: [ForeignKey][mto], [ManyToManyField][mtm], [OneToOneField][oto]

3. Retrieving data objects from database.











[field]:https://docs.djangoproject.com/en/1.9/ref/models/fields/#model-field-types
[vilidator]:https://docs.djangoproject.com/en/1.9/ref/validators/
[fieldop]:https://docs.djangoproject.com/en/1.9/ref/models/fields/#field-options
[mto]:https://docs.djangoproject.com/en/1.9/topics/db/examples/many_to_one/
[mtm]:https://docs.djangoproject.com/en/1.9/topics/db/examples/many_to_many/
[oto]:https://docs.djangoproject.com/en/1.9/topics/db/examples/one_to_one/
[manager]:https://docs.djangoproject.com/en/1.9/topics/db/managers/
[meta]:https://docs.djangoproject.com/en/1.9/ref/models/options/
[migrate]:https://docs.djangoproject.com/en/1.9/topics/migrations/