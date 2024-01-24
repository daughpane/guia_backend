# How to install Django
## This is the reference used for installing the django from django documentation
https://docs.djangoproject.com/en/5.0/topics/install/#

# STEP BY STEP INSTALLATION OF DJANGO 
**1. Download and install latest python**

      https://www.python.org/downloads/ 

**2. Install pip**
- open **command prompt** and run as administrator
- usually, pip is automatically installed if python is downloaded from python.org
- if pip is already installed, run `py -m pip install --upgrade pip` to update pip
- verify by running `pip --version`
  > should be version 23.3.2
- or head to this link to install pip

      https://pip.pypa.io/en/latest/installation/

**3. Setup django environment**
- run these commands in **command prompt**
   - cd to the folder where guia_backend is located
   
         cd Documents\Github
  
   `py -m venv guia`

   > should be **(guia)** C:\Users\efypu\Documents\GitHub>
   
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

**4. Run**
- open the cloned repository in VSCode and open the terminal
- input `python manage.py runserver` in the terminal to create a server to run.
