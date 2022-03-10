import json
import datetime
import time
import os

#Number of daily timesteps between 10am-00am
usernum = [0]*28
x = 0

#File directory
directory = 'data_processing/week28feb'

for file in os.listdir(directory):
    if file.endswith(".json"):
        x+=1

        # Open json file       
        file = directory+'/'+file
        with open(file) as json_file:
            data = json.load(json_file)

        # Extract up to timestamp:activity key value pair
        activity = data['Summary']['Users']['Chart']

        # Sort keys
        sortedkeys = sorted(activity.keys())

        #Iterate through timesteps 
        i = 0

        #Iterate through kv pairs
        for key in sortedkeys:
            #print(key, activity[key]['Active'])
            usernum[i] += activity[key]['Active']
            i += 1
print(i)
print(usernum)

