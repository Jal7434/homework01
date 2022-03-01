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

Additionally aside from running the main file a test file is installed and can be tested with pytest test_ml_data_analysis.json to ensure that
all the calculations found inside are done correctly.
</details>

</details>
