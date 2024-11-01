import os
import requests
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
print("Puzzel:")
scrambledStation = input()

filteredStations = []

for station in stations:
    allCharsPresent = True
    for char in scrambledStation:
        if char.lower() not in station.lower():
            allCharsPresent = False
            break
    if allCharsPresent:
        filteredStations.append(station)
stations = filteredStations
strippedText = str(stations).replace('[','').replace(']','').replace("'","").replace("\n", "")
print(strippedText)
input()

