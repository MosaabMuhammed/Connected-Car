import time
import json
import random
import requests

# The path looks like this because I'm running my code in Linux!
# Feel free to modify it.
with open("/media/mosaab/Volume/Projects/Dell_Bootcamp/Mentor-ship/2_CarSimulator/data/car2.json") as json_file:
    data = json.load(json_file)
    for car in data:
        car = json.dumps(car)
        requests.post("http://localhost:8000", data=car)
        rand = random.randint(7, 13)
        print("New Data From Car (2) after: ", rand, "sec.")
        time.sleep(rand)