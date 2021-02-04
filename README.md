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

# Create Superuser Admin Site
> $ python manage.py createsuperuser