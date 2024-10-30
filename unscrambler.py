import requests
import apikey

def getStations():
    key = apikey.apiKey
    url = "https://gateway.apiportal.ns.nl/nsapp-stations/v3?countryCodes=NL"
    header = {'Ocp-Apim-Subscription-Key': key}
    response = requests.get(url, headers=header).json()
    stationNames = [station['names']['long'] for station in response['payload'] if station['country'] == 'NL']
    return stationNames
stations = getStations()
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
strippedText = str(stations).replace('[','').replace(']','').replace("'","")
print(strippedText)
input()

