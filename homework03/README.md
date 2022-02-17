<details open>
<summary>  Mars Turbidity Calculations </summary>
   <details >
<summary>Folder Contents</summary>
This folder contains two python scripts, the first script labeled "analyze_water.py" 
which holds all of the calculations to obtain the turbidity of the water for the 5 most recent samples collected.
the second script labeled "test_analyze_water.py" is a simple tester to ensure that the first script functions the way it is inteded to. The purpose of this is to calculate the turbidity of the water found in the scenario give of mars.

</details>
<details >
<summary>** IMPORTANT FILE INFORMATION **</summary>
Before starting with the testing of any script you must download the following file 'turbidity_data'by following this link
['turbidity_data'](https://raw.githubusercontent.com/wjallen/turbidity/main/turbidity_data.json "turbidity_data")
to retrieve the file you can use wget with the link to get the file straight from the url.
   
</details>
<details >
<summary> How to Run the Code
</summary>
To begin running the code ensure that the turbidity_data.json file is downloaded and is within the same directory as the two scripts. Start by running the first python script "analyze_water.py" which reorders the list of samples into the 5 most recent samples and taken the average turbidity of the water, and also calculates the minumum time for the trubidity to return to a safe threshold. The output for the this file is as such 

```
Average turbidity based on most recent 5 entries =  0.6849 NTU
INFO: Turbidity is below threshold for safe use
Minimum time required to return below a safe threshold = 8.66 hours
```
This output can be interpreted as having the turbility below 1.0 NTU which means that the turbidity is below the threshold of safe use. 
The second script "test_analyze_water.py" does a simple tests to ensure that the calculations in the "analyze_water.py" script are running correctly.
</details>
</details>
