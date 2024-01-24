# How to install Django
## This is the reference used for installing the django from django documentation
https://docs.djangoproject.com/en/5.0/topics/install/#

# STEP BY STEP INSTALLATION OF DJANGO 
1. Download and install latest python
   
https://www.python.org/downloads/ 

2. Install pip
- usually pip is automatically installed if using python downloaded from python.org
- verify by running `pip --version` in cmd
  
> should be version 23.3.2
- or head to this link to install pip
  
https://pip.pypa.io/en/latest/installation/

3. Setup django environment
- run in command prompt
  
`py -m venv guia`

`guia\Scripts\activate.bat`

`py -m pip install Django`

`django-admin --version`

> should be version 5.0.1

`py -m pip install "colorama >= 0.4.6"`

`python`

`import django`

`print(django.get_version())`

> should be version 5.0.1

`exit()`

4. run
   
`python manage.py runserver`
