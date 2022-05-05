<details open>
<summary>  Meteorite Landing Calculations and General Understanding </summary>
   <details >
<summary>Folder Contents</summary>
This folder contains 5 files including this README.md file. 1 of the files included in this is a json file labeled
Meteorite_Landings.json that has information about certain meteorites. Another file included in this file is a Docker file to run
and build an image in a container known as Docker. the next file is the python script that is named ml_data_analysis.py which
gives quite a bit of information about 30 of the meteorites found in the Meteorite_Landings.json file.
The last flie is another python script that is meant to test to ensure that the ml_data_analysis.py script is running 
properly
</details>
<details>
<summary> How to Run </summary>
To begin ensure that all of the file found in this directory are copied to a single directory elsewhere 
with the inteded purpose of running the ml_data_analysis.py file. one should be able to pull the existing image 
created on the Docker Hub by  using the command docker pull jal7434/ml_data_analysis:hw04 once that is done
running the code in the contatiner is fairly simple and available with two options.
First option is to open up the container by using the command 

```
docker run --rm -it -v $PWD:/data jal7434/ml_data_analysis:hw04 /bin/bash 

```

and upon opening this the user will be see as the root user showing that they are in the container.
while in the container simply type ml_data_analysis.py followed by Meteorite_Landings.json to get the output from the script.
the Second option is to run the command through the container without opening it completely and simply getting
an output from the container. Use the code 

```

docker run --rm -v $PWD:/data jal7434/ml_data_analysis:hw04 ml_data_analysis.py /data/Meteorite_Landings.json

```

Additionally aside from running the main file a test file is installed and can be tested with pytest 
test_ml_data_analysis.json to ensure that
all the calculations found inside are done correctly.

To run the analysis script against a unique data set besides 
the example data set provided in the container, you can mount your own data set into 
the container, by first exiting the container with exit and then running the following
 command in the repository with your Dockerfile:

```

docker run --rm -it -v $PWD:/data jal7434/ml_data_analysis:hw04 /bin/bash

```

</details>
<details>
   <summary> Expected Results</summary>
The ml_data_analysis.py script should have the following ouput 

   ```
   Average mass of 30 meteor(s):
83857.3 grams

Hemisphere summary data:
There were 21 meteors found in the Northern & Eastern quadrant
There were 6 meteors found in the Northern & Western quadrant
There were 0 meteors found in the Southern & Eastern quadrant
There were 3 meteors found in the Southern & Western quadrant

Class summary data:
  The {'L5': 1, 'H6': 1, 'EH4': 2, 'Acapulcoite': 1, 'L6': 6, 'LL3-6': 1, 'H5': 3, 'L': 2, 'Diogenite-pm': 1, 'Stone-uncl': 1, 'H4': 2, 'H': 1, 'Iron-IVA': 1, 'CR2-an': 1, 'LL5': 2, 'CI1': 1, 'L/LL4': 1, 'Eucrite-mmict': 1, 'CV3': 1}  
   ```

 this should be fairly straight forward as to what the data represents, with the exception of the Class summary data which was inadvertably left as raw data which can be interpreted as the 
'class' and 'the amount found of the class'  within the Meteorite_Landings.json file.
   </details>
   <details> <summary> Additional Information </summary> 
   More data for the Meteorite_Landing.json file is available at https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
      to use this data in your directory or container use the command 
  
      wget https://raw.githubusercontent.com/wjallen/coe332-sample-data/main/ML_Data_Sample.json
   
       
   to obtain the added/updated Meteorite_Landings.json file.   
   </details>
   
</details>
