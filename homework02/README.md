Meteorite geolocation generator

The folder contains two python files:"calculate-trip.py", "sites-generator.py" and this "README.md" file.
This folders project is to have python scripts that generates 5 meteorite latitudes and longitudes, 
and another that takes the information from that first python script and uses that data to calculate the
distance and time from the latitudes, longitudes and composition.
This is important because it helps create a presepective of realworld latitude and longitude calculations 
in an enviornment like Mars. 


The first project generates 5 pairs of latitudes (between 16.0 and 18.0)
and longitudes (between 82.0 and 84.0). Additionally it assigns a compostion from a 
list of ["stony","iron", "stony-iron"] from this it creates a json file that provides a data structure.
The second project creates a dictionary from the input json file created from the first project and uses the 
latitude and longitude values to find the distance a rover would travel on mars from origin point (16.0, 82.0), 
also tracks the amount of time it would take to harvest a type of meteorite from the list of compositions.

