import urllib.request

import json
from win10toast import ToastNotifier

import emoji


name="UCEfbRQVAzI1ZkGwYXs7VJVw"

key=ENTER_YOUR_KEY


data = urllib.request.urlopen("https://www.googleapis.com/youtube/v3/channels?part=statistics&id="+name+"&key="+key).read()
subs=json.loads(data)["items"][0]["statistics"]["subscriberCount"]




toaster= ToastNotifier()

a=emoji.emojize("You have %d" %int(subs) +" subscribers :penguin:")

toaster.show_toast("Sample",a)
