'''
Created on Mar 16, 2019

@author: mosaab
'''
import json

# The path looks like this because I'm running my code in Linux!
# Feel free to modify it.
with open("/media/mosaab/Volume/Projects/Dell_Bootcamp/Mentor-ship/2_CarSimulator/data/car1.json") as json_file:
    data = json.load(json_file)
    lat = 34
    lng = 38
    for car in data:
        car['lat'] = 0
        car['lng'] = 0
    for car in data:
        car['lat'] += lat
        car['lng'] += lng
        lat += 1
        lng += 1
        print(car)
with open("/media/mosaab/Volume/Projects/Dell_Bootcamp/Mentor-ship/2_CarSimulator/data/car1.json", 'w') as f:
    f.write(json.dumps(data))