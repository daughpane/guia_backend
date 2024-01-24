# How to install Django
## This is the reference used for installing the django from django documentation
https://docs.djangoproject.com/en/5.0/topics/install/#

# STEP BY STEP INSTALLATION OF DJANGO 
1. Download and install latest python
   
https://www.python.org/downloads/ 

2. Install pip
- usually pip is automatically installed if using python downloaded from python.org
- verify by running `pip --version` in cmd
> version 23.3.2
- or head to this link to install pip
  
https://pip.pypa.io/en/latest/installation/

3. Setup django environment
- run in command prompt
  
`py -m venv guia`

`guia\Scripts\activate.bat`

`py -m pip install Django`

`django-admin --version`

`py -m pip install "colorama >= 0.4.6"`

`python`

`import django`

`print(django.get_version())`

> version 5.0.1

`ctrl + z`

`cd guia_backend`

4. run
   
`python manage.py runserver`
