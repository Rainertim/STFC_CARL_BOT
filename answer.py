import sys
import os
import requests
import json
import time
from datetime import datetime
import pyjokes
import pyowm
from requests.api import request
import stfc_database



sendurl = "https://cdn-nv3-live.startrek.digitgaming.com/chat/v1/messages/n09d3eebd7834b49b8f0e1b162cc4d50/send"

sendheaders = {
    "Host": "cdn-nv3-live.startrek.digitgaming.com",
    "User-Agent": "UnityPlayer/2018.4.24f1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)",
    "Accept": "*/*",
    "Accept-Encoding": "identity",
    "X-TRANSACTION-ID": "cbe25dec-b436-4b44-8653-9b98bd079e1e",
    "X-PRIME-VERSION": "1.000.19139",
    "X-Suppress-Codes": "1",
    "Content-Type": "application/json",
    "X-Api-Key": "FCX2QsbxHjSP52B",
    "X-PRIME-SYNC": "0",
    "X-AUTH-SESSION-ID": "da6dc51d415440b9a8f6152832a1dcba",
    "X-Unity-Version": "2018.4.24f1",
    "Content-Length": "93",
}




def respond(jsobj, chn, users):
    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper() == "!help".upper()):
        msg = ["||        WELCOME TO CARL BOT       ||",
               "==>!takeover > Takeover information ",
               "==>!discord > Discord Link          ",
               "==>!motivate (name) > Motivate      ",
               "==>!pizza > get pizza               ",
               "==>!joke/!witz/!chuck > get a joke   ",
               "==>!add > add the bot to your pm's ",
               "==>!crew (ship) > get crew suggestions for the ship",
               "==>!weather/wetter (location)       ",
               "==>!info (ship) (tier) (tier) > get a link for the upgrade cost between 2 tiers"]
        for m in msg:
            body = {
                "chn": chn,
                "txt": m,  # todaytakeover,
                "cno": 4
            }
            r = requests.post(sendurl, data=json.dumps(body),
                              headers=sendheaders)
    # if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper() == "!alert".upper()):
    #     msg = jsobj["messages"][len(jsobj["messages"])-1]["txt"].split("-")
    #     for user in users:
    #         chn = "usr_"+user
    #         body = {
    #             "chn": chn,
    #             "txt": msg,  # todaytakeover,
    #             "cno": 4
    #         }
    #         r = requests.post(sendurl, data=json.dumps(body),
    #                           headers=sendheaders)
    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper() == "!joke".upper()):
        print("hjaaa")
        joke = pyjokes.get_joke(language='en', category='all')
        body = {
            "chn": chn,
            "txt": joke,  # todaytakeover,
            "cno": 4
        }
        print("Heyyyaaaa")
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper() == "!witz".upper()):
        joke = pyjokes.get_joke(language='de', category='all')
        body = {
            "chn": chn,
            "txt": joke,  # todaytakeover,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper() == "!chuck".upper()):
        joke = pyjokes.get_joke(language='de', category='chuck')
        body = {
            "chn": chn,
            "txt": joke,  # todaytakeover,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)

    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper() == "!daily".upper() or jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper() == "!dailies".upper()):
        joke = "https://stfc.space/events"
        body = {
            "chn": chn,
            "txt": joke,  # todaytakeover,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper() == "!takeover".upper()):
        takeoverdict = {
            "Monday": "No Takeover today/Keine GÜ Heute",
            "Tuesday": "No Takeover today/Keine GÜ Heute",
            "Wednesday": "No Takeover today/Keine GÜ Today",
            "Thursday": "Burran 12:00 UTC Join here: [Burran Alpha-System S:1593338589], Brijac 14:00 UTC Today Join Here: [Brijac Alpha-System S:962542656]",
            "Friday": "Comst 09:00 UTC Join here: [Comst Beta-System S:1066722677], Saldeti 12:00 UTC Today Join Here:[Saldeti Alpha-System S:1123110021]",
            "Saturday": "Barasa 16:00 UTC (EVENT RESET) Today Join Here: [Barasa Alpha-System S:539879784]",
            "Sunday": "No Takeover today/Keine GÜ Heute",
        }
        # usermsg = input("Gimme a message to send: ")

        now = datetime.now()
        day = now.strftime("%A")
        # current_time = now.strftime("%H:%M:%S")
        todaytakeover = takeoverdict[day]
        body = {
            "chn":  chn,
            "txt": todaytakeover,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper() == "!pizza".upper()):
        joke = "🍕🍕🍕🍕🍕🍕🍕"
        body = {
            "chn": chn,
            "txt": joke,  # todaytakeover,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper().startswith("!alert".upper())):
        joke = jsobj["messages"][len(jsobj["messages"])-1]["txt"].split("-")[1]
        body = {
            "chn": "aie_176_1235645015628603909",
            "txt": joke,  # todaytakeover,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
        t = "DONE"
        body = {
            "chn":  chn,
            "txt": t,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper().startswith("!motivate".upper())):
        joke = jsobj["messages"][len(jsobj["messages"])-1]["txt"].split(" ")[1]
        joke = "Go go go go go "+joke
        body = {
            "chn": chn,
            "txt": joke,  # todaytakeover,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper().startswith("!takeover -a".upper())):
        takeoverdict = {
            "Monday": "No Takeover today/Keine GÜ Heute",
            "Tuesday": "No Takeover today/Keine GÜ Heute",
            "Wednesday": "No Takeover today/Keine GÜ Today",
            "Thursday": "Burran 12:00 UTC Join here: [Burran Alpha-System S:1593338589], Brijac 14:00 UTC Today Join Here: [Brijac Alpha-System S:962542656]",
            "Friday": "Comst 09:00 UTC Join here: [Comst Beta-System S:1066722677], Saldeti 12:00 UTC Today Join Here:[Saldeti Alpha-System S:1123110021]",
            "Saturday": "Barasa 16:00 UTC (EVENT RESET) Today Join Here: [Barasa Alpha-System S:539879784]",
            "Sunday": "No Takeover today/Keine GÜ Heute",
        }
        # usermsg = input("Gimme a message to send: ")

        now = datetime.now()
        day = now.strftime("%A")
        # current_time = now.strftime("%H:%M:%S")
        todaytakeover = takeoverdict[day]
        body = {
            "chn":  "aie_176_1235645015628603909",
            "txt": todaytakeover,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
        todaytakeover = "DONE"
        body = {
            "chn":  chn,
            "txt": todaytakeover,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper().startswith("!discord".upper())):
        joke = "https://discord.gg/WWza3eAaWS"
        body = {
            "chn": chn,
            "txt": joke,  # todaytakeover,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper().startswith("!help".upper())):
        try:
            msg = jsobj["messages"][len(
                jsobj["messages"])-1]["txt"].split(" ")[1]
        except:
            pass
        msg = stfc_database.get_Helps()[msg.upper()]
        if msg == "":
            msg = "Bitte einen Befehl angeben. Please add a command"
        body = {
            "chn": chn,
            "txt": msg,  # todaytakeover,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)

    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper() == ("!commands".upper())):
        msg = "Commands: !takeover, !motivate (name), !crew (ship), !weather/wetter (ort/location), !pizza, !joke/witz/chuck"
        body = {
            "chn": chn,
            "txt": msg,  # todaytakeover,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
    ## WEATHER ENGLISH ##
    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper().startswith("!weather".upper())):
        OpenWMap = pyowm.OWM("46ae4905c88f79737b7a237bbdc94323")
        mgr = OpenWMap.weather_manager()
        Weather = mgr.weather_at_place(
            jsobj["messages"][len(jsobj["messages"])-1]["txt"].split(" ")[1])
        Data = Weather.weather
        w = Data.detailed_status
        print(w)
        msg = "Weather in " + jsobj["messages"][len(jsobj["messages"])-1]["txt"].split(" ")[1] + " ==> " + w + " ==> Temperatur: " + str(
            Data.temperature(unit='celsius')["temp"]) + " Humidity: " + str(Data.humidity)
        # msg = "Wetter in " + jsobj["messages"][len(jsobj["messages"])-1]["txt"].split(" ")[1] + " ==> Temperatur: " + str(Data.temperature(unit='celsius')["temp"])  + "Luftfeuchtigkeit: " + str(Data.humidity())
        body = {
            "chn": chn,
            "txt": msg,  # todaytakeover,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)

    ## WETTER DEUTSCH ##
    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper().startswith("!wetter".upper())):
        OpenWMap = pyowm.OWM("46ae4905c88f79737b7a237bbdc94323")
        mgr = OpenWMap.weather_manager()
        Weather = mgr.weather_at_place(
            jsobj["messages"][len(jsobj["messages"])-1]["txt"].split(" ")[1])
        Data = Weather.weather
        w = Data.detailed_status
        print(w)
        msg = "Wetter in " + jsobj["messages"][len(jsobj["messages"])-1]["txt"].split(" ")[1] + " ==> " + w + " ==> Temperatur: " + str(
            Data.temperature(unit='celsius')["temp"]) + " Luftfeuchtigkeit: " + str(Data.humidity)
        # msg = "Wetter in " + jsobj["messages"][len(jsobj["messages"])-1]["txt"].split(" ")[1] + " ==> Temperatur: " + str(Data.temperature(unit='celsius')["temp"])  + "Luftfeuchtigkeit: " + str(Data.humidity())
        body = {
            "chn": chn,
            "txt": msg,  # todaytakeover,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper() == "!kacknoobs".upper()):
        msg = "Kacknoobs: 1. Didooo 2. Uchi"
        body = {
            "chn": chn,
            "txt": msg,  # todaytakeover,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper().startswith("!crew".upper())):

        ship = jsobj["messages"][len(jsobj["messages"])-1]["txt"].split(" ")[1]
        # current_time = now.strftime("%H:%M:%S")

        info = stfc_database.get_Crews()[ship.upper()]

        body = {
            "chn":  chn,
            "txt": info,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
    
    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper().startswith("!scrap".upper())):
        ship = jsobj["messages"][len(jsobj["messages"])-1]["txt"].split(" ")[1]
        output = stfc_database.get_Scraps()
        output = output[ship.upper()]
        for o in output:
            body = {
                "chn":  chn,
                "txt": o,
                "cno": 4
            }
            r = requests.post(sendurl, data=json.dumps(body),
                              headers=sendheaders)
    if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper().startswith("!info".upper()) or jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper().startswith("!ship".upper())):
        print("blob")
        ship = jsobj["messages"][len(jsobj["messages"])-1]["txt"].split(" ")[1].upper()
        t =jsobj["messages"][len(jsobj["messages"])-1]["txt"].split(" ")[2]
        print("blab")
        t1 = 0
        try:
            t1 = jsobj["messages"][len(jsobj["messages"])-1]["txt"].split(" ")[3] 
        except:
            print("bleb")
            try: 
                t1 = int(t)+1
                t1 = str(t1)
            except BaseException as ex:
                print(ex + "Conc")
        try:
            query = stfc_database.get_Link(t,t1,ship)
        except BaseException as ex:
            print(ex)
        body = {
            "chn":  chn,
            "txt": query,
            "cno": 4
        }
        r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
    
