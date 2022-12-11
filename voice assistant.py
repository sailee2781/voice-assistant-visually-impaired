import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import time
from bs4 import BeautifulSoup
import requests, json
import pyaudio


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    strTime = time.strftime("%H:%M:")
    if hour>=0 and hour<12:
        speak("Good Morning! the time is"  )
        speak(strTime)

    elif hour>=12 and hour<18:
        speak("Good Afternoon! the time is" )   
        speak({strTime})

    else:
        speak("Good Evening! the time is " ) 
        speak({strTime})

    speak("Hello Sir. Please tell me how may I help you")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)    
        print("Say that again please...")  
        return "None"
    return query



if True:
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'weather' in query:
             api_key = "7fb0aa01055b31bbbb4c0a84b382d0a5" #generate your own api key from open weather
             base_url = "http://api.openweathermap.org/data/2.5/weather?"
             speak("tell me which city")
             city_name = takeCommand()
             complete_url = base_url + "appid=" + api_key + "&q=" + city_name
             response = requests.get(complete_url)
             x = response.json()
             if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                r = ("in " + city_name + " Temperature is " +
             str(int(current_temperature - 273.15)) + " degree celsius " +
             ", atmospheric pressure " + str(current_pressure) + " hpa unit" +
             ", humidity is " + str(current_humidiy) + " percent"
             " and " + str(weather_description))
                print(r)
                speak(r)
                
                
        elif ("create a reminder list" in query or "reminder" in query):
            speak("What is the reminder?")
            data = takeCommand()
            speak("You said to remember that" + data)
            reminder_file = open("data.txt", 'a')
            reminder_file.write('\n')
            reminder_file.write(data)
            reminder_file.close()
            
        elif ("do you know anything" in query or "remember" in query):
            reminder_file = open("data.txt", 'r')
            speak("You said me to remember that: " + reminder_file.read())
            
        elif 'currency' in query and 'conver' in query:
            speak('I can convert, US dollar into indian rupee, and indian rupee into US dollar. Do you want to continue it?')
            query = takeCommand().lower()
            if 'y' in query or 'sure' in query or 'of course' in query:
                speak('which conversion you want to do? US dollar to indian rupee, or indian rupee to US dollar?')
                query = takeCommand().lower()
                if ('dollar' in query or 'US' in query) and ('to india' in query or 'to rupee' in query):
                    speak('Enter US Dollar')  
                    USD = float(input("Enter United States Dollar (USD):"))                                     
                    INR = USD * 81.70
                    inr = "{:.4f}".format(INR)
                    print(f"{USD} US Dollar is equal to {inr} indian rupee.")
                    speak(f'{USD} US Dollar is equal to {inr} indian rupee.')
                    speak("If you again want to do currency conversion then say, 'convert currency' " )
                elif ('india' in query or 'rupee' in query) and ('to US' in query or 'to dollar' in query or 'to US dollar'):
                    speak('Enter Indian Rupee')
                    INR = float(input("Enter Indian Rupee (INR):"))                                       
                    USD = INR/81.70
                    usd = "{:.3f}".format(USD)
                    print(f"{INR} indian rupee is equal to {usd} US Dollar.")
                    speak(f'{INR} indian rupee is equal to {usd} US Dollar.')
                    speak("If you again want to do currency conversion then say, 'convert currency' " )
                else:
                    speak("I cannot understand what did you say. If you want to convert currency just say 'convert currency'")
            else:
                print('ok sir')

        
      
