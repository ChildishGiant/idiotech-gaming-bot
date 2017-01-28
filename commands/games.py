from datetime import datetime
import urllib.request, re

#title regex  (.+?)(?=\d{1,2} \w{3}, \d{4,})    [:-1].strip()
titleRegex = "(.+?)(?=\d{1,2} \w{3}, \d{4,})"
#date regex (\d{1,2} \w{3}, \d{4,})|(TBA)
dateRegex = "(\d{1,2} \w{3}, \d{4,})|(TBA)"
#url regex (http:.*)
urlRegex = "(http:.*)"

def fetchLatest():

    final = ""
    count = 0

    f = urllib.request.urlopen("http://pastebin.com/raw/s5umVEVQ")
    lines = f.read().decode("utf-8").split("\n")

    for i in range(0,len(lines)):

        title = re.findall(titleRegex, lines[i])[0].strip()
        date = tuple(re.findall(dateRegex, lines[i])[0])[0]
        url = re.findall(urlRegex, lines[i])[0]

        if datetime.strptime(date, '%d %b, %Y').date() > datetime.now().date():
            final += "**{}** - Releases on **{}**. {}\n".format(title, date, url)
            count += 1

        if count >= 10:
            break

    return final
