#!/usr/bin/python
import urllib, json
import sys
import datetime
import os.path

format = "%H:%M:%S"
today = datetime.datetime.today()
s = today.strftime(format)
d = datetime.datetime.strptime(s, format)
t = d.strftime(format)
time = urllib.quote(t)
today = datetime.date.today()

#Set your wunderground.com Station ID and account password here.
STATIONID=""
PASSWORD=""

WEATHERFILE='/tmp/current-weather.json'
modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(WEATHERFILE))
duration = today - modified_date

print duration

WEATHERJSON=open(WEATHERFILE)
data = json.loads(WEATHERJSON.read())
temp = data["temperature"]
humidity = str(data["humidity"])
avgWindSpeed = str(data["avgWindSpeed"])
rain = str(data["rain"])
batteryLow = str(data["batteryLow"])
windDirection = str(data["windDirection"])
gustSpeed = str(data["gustSpeed"])
tempf = str(9.0/5.0 * temp + 32)


url = "http://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?ID=" + STATIONID + "&PASSWORD=" + PASSWORD + "&dateutc=" + str(today) + "+" + str(time) + "&winddir=" + windDirection + "&windspeedmph=" + avgWindSpeed + "&windgustmph=" + gustSpeed + "&tempf=" + tempf + "&rainin=" + rain + "&humidity=" + humidity + "&action=updateraw"
#print url
response = urllib.urlopen(url)
print response.read()
