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

# INSTALLING POSTGRESQL LOCALLY #
   ## Download Postgresql using this link: ##
   https://www.postgresql.org/download/windows/

   > version should be 16.1

- Open pgAdmin4
- Click server, and choose PostgreSQL version
Note: You don’t have to separately install pgAdmin. Fortunately, PostgreSQL includes this for us in its package (free)
- Right click Databases
- Create database name (guia_db)

## Now, go back to VSCode and navigate to settings.py ##
- Modify the DATABASES part
  
   ```
   import environ
   env = environ.Env()
   # reading .env file
   environ.Env.read_env()
   # Raises django's ImproperlyConfigured exception if SECRET_KEY not in os.environ
   '''SECRET_KEY = env("SECRET_KEY", default="unsafe-secret-key")

   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql_psycopg2',
           'NAME': env("DATABASE_NAME"),
           'USER': env("DATABASE_USER"),
           'PASSWORD': env("DATABASE_PASSWORD"),
           'HOST': env("DATABASE_HOST"),
           'PORT': env("DATABASE_PORT"),
       }
   }

Run this in the terminal

      `pip install django-environ`

      `pip freeze`

      `pip install psycopg2`


## Create .env file with this content ##
   ```
   SECRET_KEY=0x!b#(1*cd73w$&azzc6p+essg7v=g80ls#z&xcx*mpemx&@9$
   DATABASE_NAME=guia_db
   DATABASE_USER=postgres
   DATABASE_PASSWORD=kabitsass
   DATABASE_HOST=127.0.0.1
   DATABASE_PORT=5432
   ```

## Add this in the gitignore ##
   ```
   db.sqlite3
   *.env
   /env
   ```

## Now, migrate the table to the Postgresql database ##

- Go to settings.py and register guia_db in the INSTALLED_APPS
  
   Run command

   `python manage.py makemigrations`

   Expect "No changes detected" on the console

   `python manage.py migrate`

   Expecting "Applying ... OK" and no error

## Verify tables added ##
- Go back to pgAdmin
- Right click the db_name to refresh
- Double click the "Tables" 
- Right click the new table added and then View/Edit Data/All Rows


## Let's make a sample data for our table ##
Go back to VSCode and run command

   `python manage.py shell`

   `from guia_db.models import Model`

   `objectname=classname(attribute="attribute_value")`

   `objectname.save()`

## Check the changes in pgAdmin ##
- Right click to refresh the table 
- Right click the table and then View/Edit Data/All Rows
- Verify data added


### Reference on How to Start Django Project with a Database(PostgreSQL): ###

https://stackpython.medium.com/how-to-start-django-project-with-a-database-postgresql-aaa1d74659d8


# Django Admin
Django Admin is an interface automatically made by django so we can access our tables without using third-party database manager (like MySQL Workbench or PgAdmin).

Precondition:
You must be running in the virtual environmnent as instructed above and the app is already running on the localhost.

**1. Create a superuser**
- Make sure you are running in the virtual environment as instructed above.
- Run the app using python manage.py runserver
- On a separate terminal run `python manage.py createsuperuser`
- You will be prompted to enter username, email (can be skipped), and password. This will be your credential in accessing the admin.

**2. Accessing the django-admin**
- Go to http://127.0.0.1:8000/admin, or replace the base url with whatever url is used when you run your app locally.
- You will be prompted to input the username and password. Enter the credentials you used when you created the superuser.

**3. Navigating the django-admin**
- Upon logging in, you will be redirected to the page that includes all the tables present in the app.
- If your table is not in django-admin, it is not yet registered in `admin.py`
