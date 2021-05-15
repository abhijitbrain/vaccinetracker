# Updated By Abhijit

import pyttsx3
import requests
from cowin_api import CoWinAPI
import time
import RPi.GPIO as GPIO

# Pins definitions
btn_pin = 4
# Set up pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(btn_pin, GPIO.IN)

speaker = pyttsx3.init()
cowin = CoWinAPI()

district_id = '446'
date = '14-05-2021'     # Optional. Takes today's date by default

def vaccineCheck18():
    cowin = CoWinAPI()
    counter = 0
    available_centers = cowin.get_availability_by_district(district_id, date, 18)
    center              =   available_centers["centers"]
    for i in range(0,len(center)) :
        for j in range(0,len(center[i]['sessions'])):
            available = available_centers['centers'][i]['sessions'][j]['available_capacity'];
            #print(available)
            if available > 0 :
                print("18+")
                print("Name : ", center[i]['name'])
                print("Available slots : ", available)
                print("Date : ", available_centers['centers'][i]['sessions'][j]['date'])
                counter+=1
        
    if counter == 0 :
        print("18+ Sorry No Slots Available")
    else :
        data = requests.post("https://maker.ifttt.com/trigger/vAvailable/with/key/cjnKf87f12oRWfsNuDNSF0?&value1=18")

def vaccineCheck45():
    counter = 0
    available_centers   =   cowin.get_availability_by_district(district_id, date, 45)
    center              =   available_centers["centers"]
    for i in range(0,len(center)) :
        for j in range(0,len(center[i]['sessions'])):
            available = available_centers['centers'][i]['sessions'][j]['available_capacity'];
            #print(available)
            if available > 0 :
                print("45+")
                print("Name : ", center[i]['name'])
                print("Available slots : ", available)
                print("Date : ", available_centers['centers'][i]['sessions'][j]['date'])
                counter+=1
        
    if counter == 0 :
        print("45+ Sorry No Slots Available")
    else :
        data = requests.post("https://maker.ifttt.com/trigger/vAvailable/with/key/cjnKf87f12oRWfsNuDNSF0?&value1=45")

def vaccineCheckV18():
    cowin = CoWinAPI()
    counter = 0
    available_centers = cowin.get_availability_by_district(district_id, date, 18)
    center              =   available_centers["centers"]
    for i in range(0,len(center)) :
        for j in range(0,len(center[i]['sessions'])):
            available = available_centers['centers'][i]['sessions'][j]['available_capacity'];
            #print(available)
            if available > 0 :
                print("18+")
                print("Name : ", center[i]['name'])
                print("Available slots : ", available)
                print("Date : ", available_centers['centers'][i]['sessions'][j]['date'])
                speaker.say('18+ Hey !')
                speaker.say(available)
                speaker.say('Slots available at')
                speaker.say(center[i]['name'])
                speaker.say('on')
                speaker.say(available_centers['centers'][i]['sessions'][j]['date'])
                speaker.runAndWait()
                counter+=1
        
    if counter == 0 :
        speaker.say('18+ Sorry No Slots Available')
        speaker.runAndWait()
        print("18+ Sorry No Slots Available")

def vaccineCheckV45():
    counter = 0
    available_centers   =   cowin.get_availability_by_district(district_id, date, 45)
    center              =   available_centers["centers"]
    for i in range(0,len(center)) :
        for j in range(0,len(center[i]['sessions'])):
            available = available_centers['centers'][i]['sessions'][j]['available_capacity'];
            #print(available)
            if available > 0 :
                print("45+")
                print("Name : ", center[i]['name'])
                print("Available slots : ", available)
                print("Date : ", available_centers['centers'][i]['sessions'][j]['date'])
                speaker.say('45+ !')
                speaker.say(available)
                speaker.say('Slots available at')
                speaker.say(center[i]['name'])
                #speaker.say('on')
                #speaker.say(available_centers['centers'][i]['sessions'][j]['date'])
                speaker.runAndWait()
                counter+=1
        
    if counter == 0 :
        speaker.say('45+ Sorry No Slots Available')
        speaker.runAndWait()
        print("45+ Sorry No Slots Available")

#state_id = '26'
#min_age_limit = 20      # Optional. By default returns centers without filtering by min_age_limit

#available_centers = cowin.get_availability_by_district(district_id, date, min_age_limit)
#center              =   available_centers["centers"]
#c_details           =   center[0]       # 50
#sessions            =   c_details['sessions']
#s_details           =   sessions[0]     #7
#available_capacity  =   s_details['available_capacity']

while True:
    if GPIO.input(btn_pin):
        print('Button Pressed')
        vaccineCheckV18()
        vaccineCheckV45()
    else:
        vaccineCheck18()
        vaccineCheck45()
        print('waiting for 10 min ......')
        time.sleep(600)

