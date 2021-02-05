# Django 3.1 Learning Journey
# Prequisite
- Install conda package manager (optional)
- Create Conda Environment
Using Conda
> $ conda create -N django3 python=3.9 django=3.1
- Activate Environment
> $ conda activate django3

# Create Django Project
> $ django-admin startproject learn_django3

# Run Django Server
> $ python manage.py runserver

# Create Django App
> $ python manage.py startapp polls

# Working With Database
- Create Table
> $ python manage.py migrate

- Activate Models
> Register app into INSTALLED_APP at `<appname>/settings.py`, add `<appname>.apps.<Appname>Config` to the list.

- Make Models to be stored as migration
> $ python manage.py makemigration polls

- Run Migration to create db schema automatically
> $ python manage.py sqlmigrate polls 0001

- Playing with the Database API
> $ python manage.py shell
> >>> from polls.models import Choice, Question  # Import the model classes we just wrote.
> >>> from django.utils import timezone

> >>> q = Question(question_text="What's new?", pub_date=timezone.now())

### Save the object into the database. You have to call save() explicitly.
> >>> q.save()

### Now it has an ID.
> >>> q.id
1

### Access model field values via Python attributes.
> >>> q.question_text
"What's new?"
> >>> q.pub_date
datetime.datetime(2012, 2, 26, 13, 0, 0, 775217, tzinfo=<UTC>)

### Change values by changing the attributes, then calling save().
> >>> q.question_text = "What's up?"
> >>> q.save()

### objects.all() displays all the questions in the database.
> >>> Question.objects.all()

### Create Superuser Admin Site
> $ python manage.py createsuperuser

### Display any choices from the related object set -- none so far.
>>> q.choice_set.all()
<QuerySet []>

### Create three choices.
>>> q.choice_set.create(choice_text='Not much', votes=0)
<Choice: Not much>
>>> q.choice_set.create(choice_text='The sky', votes=0)
<Choice: The sky>
>>> c = q.choice_set.create(choice_text='Just hacking again', votes=0)

### Choice objects have API access to their related Question objects.
>>> c.question
<Question: What's up?>

### And vice versa: Question objects get access to Choice objects.
>>> q.choice_set.all()
<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice: Just hacking again>]>
>>> q.choice_set.count()
3

# Html snipets, emmets is missing?
- > I found this problem while writing the first html for the views using django templates. But there is no html snipets and emmets showed up. Then this setting on vscode helped me to get back the snipets and emmet.
>  
> `CTRL + ,` -> `search:emmet` -> on include languages, input key:value pair as `"django-html"` - `"html"`


