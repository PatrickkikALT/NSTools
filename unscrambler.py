stations = open('stations.json', 'r')
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

