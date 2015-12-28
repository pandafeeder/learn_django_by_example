# learn_django_by_example

Django has three fundamental parts plus 1 usefull util Form, Form is kindof familar to Model, worth being taken as the fourth fundamental part, so:

1. Model Layer(django.db)
2. View Layer(django.views)
3. Template Layer(django.template)
4. Form(django.form)

## Model Layer(django.db)

### basic usecase:
```
from django.db.models import Model

class Individual(models.Model): 
    GENDER = (                 
        ('M', 'male'),
        ('F', 'female'),
    )
    #id      = models.AutoField(primary_key=True)                                  #1
    name     = models.CharField(max_length=50) 
    age      = models.PositiveSmallIntegerField()
    species  = models.CharField(max_length=50) 
    gender   = models.CharField(max_length=1, choices=GENDER)
    company  = models.ForeignKey('Company', on_delete=models.CASCADE, null=True)
    friends  = models.ManyToManyField('self')

    #objects = models.Manager()                                                    #2

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('age',)
        
class Company(models.Model): 
    pass
```
this auto-incrementing key is auto added by django #you can make your own field(primary_key=True), only one pk=True field for a whole Model. #Think ModelField as a of, is an instance of coresponding Field class. #You can define as much fields as you want for your Model. #There's a special catagory "relationship field" #this is auto added by django, Manager provides interfaces for makeing queries #at least one Manager is provided for every model. You can change objects to other names #your like with querying with the name your specified. MyModel.objects.all() => MyModel.yourname.all() #Also you can customize your own Manager(). You can define many custom Manager in one Model.
