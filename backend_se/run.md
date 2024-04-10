export ALGOLIA_API_KEY="your_api_key_here"

cd /mnt/c/Users/ajeet/OneDrive/Documents/iitm/projects/project-TND-MAD2
python3 -m venv .env
. .env/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
sudo service redis-server start
celery -A main.celery worker -l info   #to get workers info
celery -A main.celery beat --log=info  #to get scheduled jobs
celery -A main.celery beat --loglevel=info

C:\Users\PC\Desktop\test-mad2
sudo apt-get install redis-server
close server
redis-cli shutdown
sudo systemctl start redis-server
sudo systemctl stop redis-server
sudo systemctl restart redis-server

npm install
npm run serve


git clone https://<PAT>@github.com/username/repo.git


codes for discourse
d/boot_dev
d/rails s
d/ember-cli
d/mailhog

close docker
docker stop discourse_dev
start docker
docker start discourse_dev

docker ps
docker ps -a
docker rm discourse_dev
docker rename discourse_dev discourse_dev_old


Check Containers: You can check the status of all Docker containers (running and stopped) on your system with docker ps -a. This will help you identify which containers are currently on your system and their statuses.

Reusing the Container: If your goal is to simply start the Discourse development environment, starting the existing container (docker start discourse_dev) is often the simplest solution.

Accessing Discourse: Once the Discourse container is running, you can access the Discourse app by navigating to http://localhost:3000 in your web browser (assuming port 3000 is mapped to your host machine in the Docker configuration).

API_KEY=discourse
805203cb88be4b6020394bb489667f1052bc2fb93ad1d66cc836f2dbfd0c69af