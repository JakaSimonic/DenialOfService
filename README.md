# DenialOfService
Requirements:
python3
docker
docker-compose

The repository consists of django web server and web client.
After cloning the repo:
docker-compose up //brings uš the web service
python3 client/DosClient.py 1 1  // initiates one client one worker DoS attack on the web service
