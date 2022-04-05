from flask import Flask, request
import json 
import redis

app = Flask(__name__)

ml_data =[]

@app.route('/data', methods =['POST'])
def data_file():
    '''
    Opens json file and loads the dictionary used for all routes
    Returns:
      String to client showing that download of data is complete
    ''' 
    
    with open('ML_Data_Sample.json','r') as f:
               ml_data =json.load(f)
    rd = redis.Redis(host='172.17.0.24', port=6379, db=0)
    for d in ml_data['meteorite_landings']:
        rd.set(d['id'], json.dumps(d))    

    return "Data has Been Loaded to Redis.\n"

@app.route('/data', methods =['GET'])
def data_load():
    '''
    Returns list of data loaded from the json file to the application
    /data? displays all data from json file
    Use /data?start=(ID value between 10001 and 10300) to get specific information from the Json file
    Returns:
        JSON list of information
	
    '''
    rd =redis.Redis(host='172.17.0.24',port=6379, db=0)
    ID_list = []     
    for ID in rd.keys():
        ID_list.append(json.loads(ID))

    minID = min(ID_list) 
    maxID = max(ID_list)    

    start = request.args.get('start',minID)        
    if start:
        try:
            start = int(start) 
            if start < minID or start > maxID:
                return "Invalid ID, ID must be between 10001 and 10300.\n"
            data_list = []
            while start <= maxID:
                data_list.append(json.loads(rd.get(start)))
                start += 1
 
            if len(data_list) == 0:
                return "Invalid ID, ID must be between 10001 and 10300.\n"
       
            return json.dumps(data_list, indent=2)+'\n'
        except:
            return "Invalid ID, ID must between 10001 and 10300).\n"
   
    return "'Invalid ID, ID must be between 10001 and 10300..\n"
if __name__ == '__main__':
    app.run(debug =True, host ='0.0.0.0')
