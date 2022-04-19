<h1> Kubernetes Deployment </h1>
This project uses the open source system Kubernetes to deploy a testing enviornemt that is sutible to interact with a Flask application using a redis database that which will allow users to load and recieve datasets containing specific information about meteroite landings from the file 
<a href="https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json">ML_Data_Sample.json</a> This has the feature that include class, longitude, latitude, and mass(g).
<h2> What's in the Project </h2>
The files in the project are:

```Dockerfile```: Functions to download necassary dependencies and environment variables to set up needed operations for the application.
```app.py``` : python script that provides routes to download and returns information from the Meteorite Landings Dataset.

**Yaml files**
```jal7434-test-redis-pvc.yml```: Stores data written to it from the deployment file independetly from the kubernetes pods.

```jal7434-test-redis-deployment.yml```: Redis setup/deployment of the Redis Database.

```jal7434-test-redis-service.yml```: implements a persistent IP address to interact with the redis.

```jal7434-test-flask-deployment.yml```: Deployment for the FLASK API with replicas.

```jal7434-test-flask-service.yml```: implements a persistent IP address to use that allows interaction with the API.
