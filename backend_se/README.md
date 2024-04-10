# :wave: Setting Up Project

## :octocat: Cloning the Repository

git clone https://github.com/SonicSaurav/SE-Project.git

## :octocat: Setting Up Backend

cd SE-Project

cd backend

python3 -m venv .env

. .env/bin/activate

pip3 install --upgrade pip

pip3 install -r requirements.txt

export ALGOLIA_API_KEY="your_api_key_here"

python3 main.py

sudo service redis-server start

celery -A main.celery worker -l info   #to get workers info

celery -A main.celery beat --log=info  #to get scheduled jobs

celery -A main.celery beat --loglevel=info


## :octocat: Setting Up Frontend

cd SE-Project

cd frontend

rm -rf node_modules

npm install

npm run serve


## 💻 Default Users

[
  {
    "email_id": "test1@gmail.com",
    "role_id": 1,
    "user_id": 1,
    "user_name": "test1"
    "password" : 12345678
  },

  {
    "email_id": "admin@gmail.com",
    "role_id": 3,
    "user_id": 2,
    "user_name": "admin"
    "password" : 12345678
  },
  
  {
    "email_id": "support@gmail.com",
    "role_id": 2,
    "user_id": 3,
    "user_name": "support"
    "password" : 12345678
  }
]