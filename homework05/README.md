<h1> Meteorite Data using Redis and Flask </h1>
This project uses one data set containing a multitude of meteorite landing site data to observe.
The goal of this project is to create a container which launches a Redis database server that can be used to load data and get data by using another application Flask. Flask is contained in a Dockerfile that makes setup of the containters much easier.

<h2> Files Included in the Project folder </h2>

  - ```app.py``` - Application that contains the routes and provides the ability to download and reinstates information from the Meteorite Landing data set.
  -  ```Dockerfile``` - Contains necessary information for running Flask application and other setup. 

<h2> Initial Setup </h2>
To begin the following file is necessary 
[Meteorite Landing Data](https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json).

  - This can be downloaded directly to a directory using 

```
[jal7434@isp02 homework05]$ wget https://raw.githubusercontent.com/wjallen/coe332-sample-  data/main/ML_Data_Sample.json
```

<h2> Launching Redis Database </h2>
This project uses a default Redis port inside a container from the host.
  - To begin pull the existing Redis:6 version by running the command
  
 ``` 
 [jal7434@isp02 homework05]$ docker pull redis:6 
 ```
 Once the Redis:6 is pulled the following command can be run to launch the containerized Redis server. In this instance the Redis port will be assigned the default redis port and it will save a backup every second to the /data folder. 
  - ```<redis-port#>```: This is the assigned port or your own port
  - ```<your-name>```: This is replaced by well your name.
 ```
[jal7434@isp02 homework05] docker run -d -p <redis-port#>:6379 -v $(pwd)/data:/data:rw --name=<your-name>-redis redis:6 --save 1 1
 ```
 
 To ensure that the container is setup you can run 
 ```
 docker ps -a
 ```
 and check the list to see that the container was created and is running
To use your own redis-port, find the ip address contained in the redis client to be used in the Flask app 
  - Run ``` docker inspect <container id> | grep IPAddress```
  - Create the redis client in your Flask app as: ```redis.Redis(host='172.xx.x.x', port=6379, db=0)```
  - Replace ```172.xx.x.x``` with the actual IP you find by running the docker inspect

<h2> The Flask Application </h2>
To use the Flask application, first we use the ```Dockerfile``` that is found in this repository.
  - Touch the file ```Dockerfile```
The docker file has the following inside:
 
 ```
 FROM python:3.9

 RUN mkdir /app
 WORKDIR /app

 RUN pip3 install --user Flask==2.0.3

 RUN pip3 install --user redis

 RUN wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json 

 COPY app.py /app/app.py

 RUN chmod +rx /app/app.py

 ENTRYPOINT ["python"]

 CMD ["app.py"]
 
 ```

When the Dockerfile is set begin building by using the command ``` docker build```

```
docker build -t <username>/<code>:<version> .
```
Ensure to replace ```<username>``` with Docker Hub Username, ```<code>``` with what you wish to name your code, and ```<version>``` with whatever label of version you choose.
Once the container is build to run it you can use the following command: 
```
docker run --name "container name" -d -p <port#>:5000 <username>/<code>:<version>
```
Ensure to change ```<port#>``` to whatever port that you are using/were assigned and to use the name you chose when using the ```"container name"```
To check if the container is up you can use ```docker ps -a ``` to check if the container is running amongst other docker containers.

<h2> Using the Flask Application </h2>
Now that the Flask application is running you can use the one route and two available methods
  - ```/data``` : is the route 
  - ```POST``` : A method that serves to load and store the data into the Redis server. This should be run first by using the following command 
```
curl -X POST localhost:<port#>/data
```
This should promt the following output if run successfully. 
```
Data has Been Loaded to Redis
```
  - ```GET```: The second method that serves as the main method to get information from the data set and output it.
The following command will display all of the data that is stored in the Redis data that was collected from the Meteorite Landings Data json file.
```
curl localhost:<post#>/data
```
There is 300 outputs as there is a list of 300 dictionaries that were stored in the json file.

Another feature of this application is the incorportation of a start query 
which allows to start at a certain data set and display the rest of the data.

curl localhost:<post#>/data?start=(number-from-10001-to-10300)
If a number that is less than the 10001 or greater than 10300 will be promted with an error.
<h2> Description of Data </h2>
This is an example of the output data that is contained in the sample data.
This data set contains the name, id,classification, mass in grams, and the geolocation of the meteorites.

Additionally as described previously using the start query allows the user to get data starting from anywhere in within the 300 Id's and display the rest of the data set from that id to the final 10300 id.


~~~
 [jal7434@isp02 homework05]$ curl localhost:5017/data?start=10299
[
  {
    "name": "Jennifer",
    "id": "10299",
    "recclass": "L5",
    "mass (g)": "539",
    "reclat": "-84.0579",
    "reclong": "69.9994",
    "GeoLocation": "(-84.0579, 69.9994)"
  },
  {
    "name": "Christina",
    "id": "10300",
    "recclass": "H5",
    "mass (g)": "4291",
    "reclat": "-38.1533",
    "reclong": "-46.7127",
    "GeoLocation": "(-38.1533, -46.7127)"
  }
]
~~~
