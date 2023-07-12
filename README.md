
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

- If you don't have table, create a table named 'devices' and set attribute named id(string) as primarykey

#### 3- download python
- [download and install python](https://www.python.org/downloads/) 
#### 4- Create a new virtual environment 
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

    
#### 5- install requirements
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

## Postman

- import postman json file into your postman which is named as **DevicesApp.postman_collection.json** in root folder.

  now you have access to all existing APIs:
  <br>
  <img src="https://github.com/NiloufarPadkan/django-rest-challenge/assets/50741400/ec62d143-7010-489a-90d2-bf0172320b25" width="300" />


#### This is a list of APIs and their examples. for example store device has 3 example:
- store Device (valid Request)
- store Device (missed request parameters)
- store Device (invalid id format)

  and the response is saved in this examples.

### example of store Device( valid request)
<img src="https://github.com/NiloufarPadkan/django-rest-challenge/assets/50741400/35214cbb-9db0-4081-89ac-d2f4ca8e8d50" width="800" />

### example of store Device( invalid request with missed parameters)

<img src="https://github.com/NiloufarPadkan/django-rest-challenge/assets/50741400/a2d4e96a-e596-4b28-b5d5-5b0d07989e2d" width="800" />

### example of store Device( invalid id format)

<img src="https://github.com/NiloufarPadkan/django-rest-challenge/assets/50741400/8dc877e1-a290-4365-9ed3-8b69c87fb630" width="800" />

### example of get a Device( existing device)

<img src="https://github.com/NiloufarPadkan/django-rest-challenge/assets/50741400/bbe1c612-9c0d-44b0-9958-279c1cd73c09" width="800" />


### example of get a Device(non  existing device)

<img src="https://github.com/NiloufarPadkan/django-rest-challenge/assets/50741400/4de985b9-4913-4fb2-8fcf-13b34f8301df" width="800" />






