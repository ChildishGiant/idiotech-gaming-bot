import settings
from datetime import datetime
import pytz

def getTime():
    timezones = ""
    zone = settings.timezones[0]
    time = datetime.now(pytz.timezone(zone))
    timezones += "**" + zone + " " + "**" + ": {0}".format(time.strftime("%I:%M %p")) + " "
    for zone in settings.timezones[1:]:
        time = datetime.now(pytz.timezone(zone))
        timezones += "| **" + zone + " " + "**" + ": {0}".format(time.strftime("%I:%M %p")) + " "
    return timezones

def getTimezone(loc):
    """
    Function to get local time in cities
    :return: Dictionary with {"city":"%I:%M %p"}
    """

    places = {}
    output = {}
    now_utc = datetime.now(pytz.timezone('UTC'))

    #Making a dictionary of different possible inputs and their corresponding tz
    loc = loc.lower()

    #Standard timezone format
    for zone in pytz.all_timezones:
        places[zone.lower()] = zone


    #Country codes and shorthands
    for nation in pytz.country_timezones:
        if type(nation) is list:
            nation = nation[0]

        longhand = pytz.country_timezones(nation)

        if type(longhand) is list:
            longhand =longhand[0]

        places[nation.lower()] = longhand
        try:
            code = (pytz.timezone(nation).localize(datetime.now()).tzname()).lower()
            places[code] = longhand
        except pytz.exceptions.UnknownTimeZoneError:
            continue


    for key, value in places.items():

        if loc in key.split("/"):
            place = value

        elif loc in key:
            place = value


    if "place" in locals():
        time = now_utc.astimezone(pytz.timezone(place))
        fmttime = time.strftime('%I:%M %p')
        output[loc] = fmttime
        return "Current time in **{0}** is **{1}**".format(place, output[loc])
    else:
        return "**Location/Timezone not found**"
