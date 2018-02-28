#!/usr/bin/python
import urllib, json
import sys
import datetime

def signal_handler(signal, frame):
    sys.exit(0)

def set_exit_handler(func):
    signal.signal(signal.SIGTERM, func)
def on_exit(sig, func=None):
    print "exit handler triggered"
    sys.exit(1)


format = "%H:%M:%S"
today = datetime.datetime.today()
s = today.strftime(format)
d = datetime.datetime.strptime(s, format)
t = d.strftime(format)
time = urllib.quote(t)
today = datetime.date.today()
print time
STATIONID=""
PASSWORD=""

WEATHERFILE='/tmp/weather.json'

file = open(WEATHERFILE, "r")
lineList = file.readlines()
WEATHERJSON = lineList[len(lineList)-1]

data = json.loads(WEATHERJSON)
temp = data["temperature_C"]
humidity = str(data["humidity"])
avgWindSpeed = str(data["speed"])
rain = str(data["rain"])
#batteryLow = str(data["batteryLow"])
windDirection = str(data["direction_deg"])
gustSpeed = str(data["gust"])
tempf = str(9.0/5.0 * temp + 32)
print str(today)
#timejson = data[time]

url = "http://weatherstation.wunderground.com/weatherstation/updateweatherstation.php?ID=" + STATIONID + "&PASSWORD=" + PASSWORD + "&dateutc=" + str(today) + "+" + str(time) + "&winddir=" + windDirection + "&windspeedmph=" + avgWindSpeed + "&windgustmph=" + gustSpeed + "&tempf=" + tempf + "&rainin=" + rain + "&humidity=" + humidity + "&action=updateraw"

print url
response = urllib.urlopen(url)
print response.read()
