<detail> <summary> **Meteorite geolocation generator**
</summary>

<details>
<summary>Folder Contents</summary>
The folder contains two python files:"calculate-trip.py", "sites-generator.py" and this "README.md" file.
This folders project is to have python scripts that generates 5 meteorite latitudes and longitudes,
and another that takes the information from that first python script and uses that data to calculate the
distance and time from the latitudes, longitudes and composition.
This is important because it helps create a presepective of realworld latitude and longitude calculations
in an enviornment like Mars.
<br>
</details>

<details >
<summary>Python Scripts </summary>

The first project generates 5 pairs of latitudes (between 16.0 and 18.0)
and longitudes (between 82.0 and 84.0). Additionally it assigns a compostion from a
list of ["stony","iron", "stony-iron"] from this it creates a json file that provides a data structure.
The second project creates a dictionary from the input json file created from the first project and uses the
latitude and longitude values to find the distance a rover would travel on mars from origin point (16.0, 82.0),
also tracks the amount of time it would take to harvest a type of meteorite from the list of compositions.
<br>
</details>
<details open>
<summary>How To Run The Code</summary>
To start type 

```
python3 sites-generator.py
```
to begin running the first program required to execute the full project.



```
def main():
    data = {}
    data["sites"] = []
    for i in range(5):
        data["sites"].append({"site_id" : (i + 1),
            "latitude" : generate_latitude(),
            "longitude" : generate_longitude(),
            "composition" : generate_composition()})
    with open("data.json", "w") as outfile:
        json.dump(data, outfile,indent=4)
main()
```
This will generate 5 Sites that will be output into a Json file with the data "site_id", "latitude","longitude"
and "composition" and create a new json file named "data.json"
After running the "sites-generator.py"  you can run the next python script by typing 
``` 
python3 calculate-trip.py
```
this one will first read "data.json" and create a dictionary from it. Then use the values obtained from the data.json file to calculate the distance, and time that a rover spends traveling and collecting samples if the rovers speed is 10 km.

the data that is output from this should be interpreted as the leg being the trip made to the destination on mars surface, the time it took to travel, the time spent collecting samples, and a summary that gives the total of the amount of trips and total time spent on the trip.

<br>
</details>
</detail>
