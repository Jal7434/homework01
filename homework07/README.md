<h1> ISS Diagram </h1> 
ISS Positional and Sighting Data querier applicaiton that provides a functioning web server application container that any user with interest about the ISS can use.
You can find a more visual representation about how the data is used and what it outputs in the diagram below.
<Details> <summary> ISS Positional and Sighting Data Diagram </summary> <img src="ISS Positional and Sighting Data.png"     alt="Diagram"     style="float: left; margin-right: 10px;" /> </Details>

<h2> An Explanation of the Diagram </h2>
The diagram begins with the user's input and creation of the web server application using the makefile found in the project's repository to create and set up the enviornemnt that will allow the application to run. This includes the setup of the Docker image. 
After this the user can retrieve information from the Flask application using curl localhost:<code>FlaskIP</code>/
in this case for the project the flask ip is 5017 and you can use either <code>epoch</code> or <code>countries</code> as they are the routes available to retrieve data from. They can get specific usiing <code> /COUNTRY/regions/"specified region from list"/cities/"specified city from list" </code> these will return data representative of the sightings 

The arrows are representtive of the actions the users may take to retrieve information while utilizing the application using either the information from the positional data or the sighting data. The outer ring represents that they are being run in the Docker image and the two smaller rings represent the data being used seperately from the user downloaded data for the flask api.

<h3> Access to the Full Project </h3>
Access to further information regarding this project can be found in this <a href="https://github.com/Jal7434/ISS-Positional-Data-Analysis">GitHub Repository</a>

Provides a more in depht dive into how the information datasets are used and how the container and applications work.
