# How to install Django
## This is the reference used for installing the django from django documentation
https://docs.djangoproject.com/en/5.0/topics/install/#

# STEP BY STEP INSTALLATION OF DJANGO 
**1. Download and install latest python**
   
https://www.python.org/downloads/ 

**2. Install pip**
- usually pip is automatically installed if using python downloaded from python.org
- verify by running `pip --version` in cmd
  
> should be version 23.3.2
- or head to this link to install pip
  
   https://pip.pypa.io/en/latest/installation/

**3. Setup virtual environment**
   - open the cloned repository in VSCode and open the terminal 
  
   - create guia virtual machine using `py -m venv guia`

   - activate the vm `guia\Scripts\activate.bat`

   - install django `py -m pip install Django`

   - modify console appearance `py -m pip install "colorama >= 0.4.6"`

   - verify django version `django-admin --version`

      > should be version 5.0.1

**4. Run server**
   
- input `python manage.py runserver` to run the server
