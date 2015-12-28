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
#Think MyModel as a <TABLE> in a database
class MyModel(models.Model):
    id = models.AutoField(primary_key=True)                        #1
    
    MyModelField = models.allKindsOfFieldClass(*args, **kwargs)    #2

    objects = models.Manager()                                     #3
    class Meta:
        option = "option"
```
this auto-incrementing key is auto added by django #you can make your own field(primary_key=True), only one pk=True field for a whole Model. #Think ModelField as a of, is an instance of coresponding Field class. #You can define as much fields as you want for your Model. #There's a special catagory "relationship field" #this is auto added by django, Manager provides interfaces for makeing queries #at least one Manager is provided for every model. You can change objects to other names #your like with querying with the name your specified. MyModel.objects.all() => MyModel.yourname.all() #Also you can customize your own Manager(). You can define many custom Manager in one Model.
