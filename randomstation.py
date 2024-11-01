import requests
import os
import random
if not os.path.exists("stations.json"):
    url = "https://gist.githubusercontent.com/PatrickkikALT/2a597bebb4a3f16138fff82ae56a99ce/raw/e45bbb89a7b3852b1f1317edc3f6e12ab3c14023/stations.json"
    response = requests.get(url)
    json = response.text
    with open("stations.json", "w", encoding="utf-8") as f:
        for station in json:
            f.write(station)
stations = []
for s in open("stations.json", "r", encoding="utf-8"):
    stations.append(s.strip())

print("Random station picker")
os.system("pause")
while True:
    if (len(stations) == 0):
        print("No more stations left.")
    else:
        randomStation = random.choice(stations)
        print(randomStation)
        stations.remove(randomStation)
        os.system("pause")
