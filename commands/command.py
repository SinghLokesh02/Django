# pip install django
# python.exe -m pip install --upgrade pip

# for creating Django Project
# django-admin startproject mysite

# setup with server
# python manage.py runserver

# Create App using Django
# python manage.py startapp {{app_name}}

# Create super user
# python manage.py createsuperuser

# After creating Database
# 1) Python manage.py makemigrations
# 2) python manage.py migrate


# python manage.py -> give below command help

# Available subcommands:

# [auth]
#     changepassword
#     createsuperuser

# [contenttypes]
#     remove_stale_contenttypes

# [django]
#     check
#     compilemessages
#     createcachetable
#     dbshell
#     diffsettings
#     dumpdata
#     flush
#     inspectdb
#     loaddata
#     makemessages
#     makemigrations
#     migrate
#     optimizemigration
#     sendtestemail
#     shell
#     showmigrations
#     sqlflush
#     sqlmigrate
#     sqlsequencereset
#     squashmigrations
#     startapp
#     startproject
#     test
#     testserver

# [sessions]
#     clearsessions

# [staticfiles]
#     collectstatic
#     findstatic
#     runserver