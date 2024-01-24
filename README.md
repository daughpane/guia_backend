# How to install Django
## This is the reference used for installing the django from django documentation
https://docs.djangoproject.com/en/5.0/topics/install/#

# STEP BY STEP INSTALLATION OF DJANGO 
**1. Download and install latest python**

      https://www.python.org/downloads/ 

**2. Install pip**
- open **command prompt** 
- usually, pip is automatically installed if python is downloaded from python.org
- if pip is already installed, run `py -m pip install --upgrade pip` to update pip
- verify by running `pip --version`
  > should be version 23.3.2
- or head to this link to install pip

      https://pip.pypa.io/en/latest/installation/

**3. Activate virtual machine**
    - open the cloned repository in VSCode and open the terminal
   
   - input `guia\Scripts\activate.bat` to activate vm
      
   `django-admin --version`
   
   > should be version 5.0.1
   
   `exit()`

**4. Run**
- input `python manage.py runserver` in the terminal to run the server
