import sys
import os
import requests
import json
import time
from datetime import datetime
import pyjokes
import pyowm
from requests.api import request

import answer
filepath = "users.txt"

headers = {
    'Host': 'cdn-nv3-live.startrek.digitgaming.com',
    'User-Agent': 'UnityPlayer/2018.4.24f1 (UnityWebRequest/1.0, libcurl/7.52.0-DEV)',
    'Accept': '*/*',
    'Accept-Encoding': 'identity',
    'X-TRANSACTION-ID': 'cbe25dec-b436-4b44-8653-9b98bd079e1e',
    'X-PRIME-VERSION': '1.000.19139',
    'X-Suppress-Codes': '1',
    'Content-Type': 'application/json',
    'X-Api-Key': 'FCX2QsbxHjSP52B',
    'X-PRIME-SYNC': '0',
    'X-AUTH-SESSION-ID': 'da6dc51d415440b9a8f6152832a1dcba',
    'X-Unity-Version': '2018.4.24f1'
}
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

def current_milli_time():
    return round(time.time())


# url = "https://cdn-nv3-live.startrek.digitgaming.com/chat/v1/messages/n09d3eebd7834b49b8f0e1b162cc4d50/history/aie_176_1235645015628603909?limit=20&until="
# url = url+str(current_milli_time())+".12345"

# print(url)
payload = {}

users = []

def listenalliance():
    url = "https://cdn-nv3-live.startrek.digitgaming.com/chat/v1/messages/n09d3eebd7834b49b8f0e1b162cc4d50/history/aie_176_1235645015628603909?limit=20&until="
    url = url+str(current_milli_time())+".12345"
    response = requests.request("GET", url, headers=headers, data=payload)
    # print(response.encoding)
    responsetxt = response.text
    jsobj = json.loads(responsetxt)
    # print(jsobj)
    # obj = json.dumps(jsobj)
    try:
        os.system("cls")
        print(jsobj["messages"][len(jsobj["messages"])-1]["sdr"] + ">> "+jsobj["messages"][len(jsobj["messages"])-1]["txt"])
    except BaseException as ex:
        print(ex)
    if jsobj["messages"][len(jsobj["messages"])-1]["txt"].startswith("!"):
        if(jsobj["messages"][len(jsobj["messages"])-1]["txt"].upper() == "!add".upper()):
            usrid = jsobj["messages"][len(jsobj["messages"])-1]["aid"]
            msgac = "You have been added!"
            msgusr = "Welcome to Carl bot. Type !commands for a list of commands. Gib !help ein für eine detailierte Hilfe"
            if usrid in users:
                msgusr = "You are already added!"
            else:
                users.append(usrid)

            body = {
                "chn":  "aie_176_1235645015628603909",
                "txt": msgac,
                "cno": 4
            }
            r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
            body = {
                "chn":  "usr_"+usrid,
                "txt": msgusr,
                "cno": 4
            }
            r = requests.post(sendurl, data=json.dumps(body), headers=sendheaders)
            with open(os.path.join(sys.path[0], "users.txt"), "a") as f:
                f.write(usrid+"\n")
        answer.respond(jsobj, "aie_176_1235645015628603909", users)



def listenusers():
    
    for user in users:
        try:
            # print("Did a user scan with user: " + user)
            usrurl = "https://cdn-nv3-live.startrek.digitgaming.com/chat/v1/messages/n09d3eebd7834b49b8f0e1b162cc4d50/history/usr_" + \
                user + "?limit=20&until="
            usrurl = usrurl+str(current_milli_time())+".12345"
            responseusr = requests.request(
                "GET", usrurl, headers=headers, data=payload)
            responseusrtxt = responseusr.text
            jsobjusr = json.loads(responseusrtxt)

            # try:
            #     # print(jsobjusr["messages"])
            # except:
            #     pass

            answer.respond(jsobjusr, "usr_"+user, users)
        except BaseException as ex:
            pass


# on startup
with open(os.path.join(sys.path[0], "users.txt"), "r") as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    users = lines

while (True):

    try:
        listenalliance()
        listenusers()

    except Exception:
        print("Something is wrong")
    time.sleep(2)
