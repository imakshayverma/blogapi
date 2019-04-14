# Blog API
> A simple Blog app that provides the facility to add blog posts and comments. 


## Installation
```
git clone https://github.com/imakshayverma/blogapi.git
cd blogapi/

# Optional if you dont have pip and venv
sudo apt-get install python3-pip
sudo apt-get install python3-venv

# Create a Virtual Environment
python3 -m venv env
source env/bin/activate

# Install Dependencies
pip3 install -r requirements.txt

# Setup Database
cd blogsite
python manage.py migrate

# Create Superuser/Admin
python manage.py createsuperuser 

# Run Server
python manage.py runserver
```

### License 
[MIT](https://github.com/imakshayverma/blogapi/blob/master/LICENSE)


