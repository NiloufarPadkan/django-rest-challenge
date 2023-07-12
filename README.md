
# Django REST API challenge

Implementiing a simple Restful API on Django using the following tech stack:
- Python
- Django
- AWS DynamoDB



## Installation


#### 1- clone the repo

```bash
git clone https://github.com/NiloufarPadkan/django-rest-challenge.git

cd django-rest-challenge
```
  
#### 2-install and configure AWS cli

- [download and install AWS Cli](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) 
  
- open terminal and enter 
```
aws configure
```

- You will be prompted to enter the following information:

 AWS Access Key ID,
 AWS Secret Access Key, Default region name, Default output format(JSON)

- If you don't have table, create a table named 'devices' and set attribute named id as primarykey

#### 2- download python
- [download and install python](https://www.python.org/downloads/) 
#### 3- Create a new virtual environment 
This will create a new virtual environment in a folder named `venv`.

```bash
python -m venv venv
```

for activating this environment:

- on windows
```
venv\Scripts\activate
```
on linux

```
. venv/bin/activate
```

    
#### 4- install requirements
This will install all the required packages for the Django project:

```bash
pip install -r requirements.txt
```



    
## Run Locally

Start the server

```bash
  python manage.py runserver 
```



## Running Tests

To run tests, run the following command

```bash
python manage.py test 
```
result will be :
``` bash
Found 5 test(s).
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
.....
----------------------------------------------------------------------
Ran 5 tests in 3.376s

OK
Destroying test database for alias 'default'...
```
