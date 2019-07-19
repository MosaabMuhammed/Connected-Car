import json

# The path looks like this because I'm running my code in Linux!
# Feel free to modify it.
with open("/media/mosaab/Volume/Projects/Dell_Bootcamp/Mentor-ship/2_CarSimulator/data/car1.json") as json_file:
    data = json.load(json_file)
    for car in data:
        car = json.dumps(car)
        print(type(car))
