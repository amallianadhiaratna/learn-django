# Learn Django

## Setup virtual environment

```
virtualenv -p python3 .
source bin/activate
deactivate
```

## Django admin command

```
source bin/activate
django-admin startproject learndjango .
python3 manage.py migrate >> sync our settings.py with the django project
python3 manage.py startapp products >> create new apps
python3 manage.py makemigrations >> create migrations
python3 manage.py createsuperuser
```

create object from python shell

```
python shell
python3 manage.py shell
In [1]: from products.models import Product

In [2]: Product.objects.all()
Out[2]: <QuerySet [<Product: Product object (1)>]>

In [3]: Products.objects.create(title='shirt', description='common', price='1
   ...: 200', summary='casual')
```

## Useful documents

- https://docs.djangoproject.com/en/4.0/ref/models/fields/
- https://docs.djangoproject.com/en/4.0/ref/templates/builtins/
- https://docs.djangoproject.com/en/4.0/topics/forms/formsets/
- https://docs.djangoproject.com/en/4.0/ref/forms/widgets/

