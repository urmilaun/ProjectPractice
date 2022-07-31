from ipaddress import summarize_address_range
import json
from multiprocessing.connection import Client
from multiprocessing.spawn import import_main_path
from random import random
from re import S 
import shutil
import sys
import time
from urllib.request import urlopen
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import requests
import subprocess


espeak_bin="espeak"


def speak(audio):
    process = subprocess.Popen(f"{espeak_bin} \"{audio}\"", shell=True, stdout=subprocess.PIPE)
    process.wait()
    if process.returncode !=0:
        print(f"error occuere with speak code = {process.returncode}")
    

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    assname = ("friday")  
    speak("I am  Assistant")       
       

def username():
    speak("what should i call you sir")  
    uname = takeCommand()  
    speak("welcome sir")
    speak(uname)
    columns = shutil.get_terminal_size().columns

    print("##########################".center(columns))
    print("welcome mr.",uname.center(columns))
    print("##########################".center(columns))


def takeCommand():
    

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



def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    #put gmail 
    server.login('sujitbhogil@gmail.com', '9881082406')
    server.sendmail('sujitbhogil@gmail.com', to, content)
    server.close()



if __name__ == "__main__":
    username()
    wishMe()
    while True:
    # if 1:
        
        query = takeCommand().lower()
       
        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences = 3)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("here you go to youtube\n")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("here you go to google\n")
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            speak("here you go to stackoerflow\n")
            webbrowser.open("stackoverflow.com")   

        elif 'play music' in query:
            speak("here you go with music\n")
            music_dir = 'E:\sd\Various Artists - 2021 Mega Hits (2021) Mp3 320kbps [PMEDIA] ⭐️'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            # use env variable
            codePath = "C:\\Users\\Haris\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
      
        
        elif 'open notepad' in query:
            # use env variable
            codePath = "C:\Windows\System32\notepad.exe"
            os.startfile(codePath)
      
        elif 'you can sleep' in query:
            speak("thanks for using me sir.   you have good day sir...!")
            sys.exit()
      
        elif 'play music' in query:
            speak("playing music ")
            music_dir = ""
            songs = os.listdir(music_dir)
            print(songs)
            random = os.startfile(os.path.join(music_dir, songs[1]))
          #closingapp

        elif 'close music' in query:
            speak("ok sir, closing sir")
            os.system("taskkill /f /im  wmplayer.exe ")


        elif 'email to sujit' in query:

            try:
                speak("What should I say?")
                content = takeCommand()
                to = "sujitbhogil@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend Urmila . I am not able to send this email")
                
        elif 'how are you ' in query:
            speak("i am fine, thank you")
            speak("how are you, sir")
 
        elif 'fine' in query or "good" in query:
            speak("It's good to know that your fine")
 
        elif "change my name to" in query:
            query = query.replace("change my name to", "")
            assname = query
 
        elif "change name" in query:
            speak("What would you like to call me, Sir ")
            assname = takeCommand()
            speak("Thanks for naming me")
 
        elif "what's your name" in query or "What is your name" in query:
            speak("My friends call me")
            speak(assname)
            print("My friends call me", assname)
 
        elif 'exit' in query:
            speak("Thanks for giving me your time")
            exit()
 
        elif "who made you" in query or "who created you" in query:
            speak("I have been created by sujit and his friend.")



       # elif "calculate" in query:
             
           # app_id = "Wolframalpha api id"
           # client = wolframalpha.Client(app_id)
           # indx = query.lower().split().index('calculate')
           # query = query.split()[indx + 1:]
           # res = client.query(' '.join(query))
           # answer = next(res.results).text
           # print("The answer is " + answer)
           # speak("The answer is " + answer)
 
        elif 'search' in query or 'play' in query:
             
            query = query.replace("search", "")
            query = query.replace("play", "")         
            webbrowser.open(query)
 
        elif "who i am" in query:
            speak("If you talk then definitely your human.")
 
        elif "why you came to world" in query:
            speak("Thanks to sujit . further It's a secret")
  
        elif 'power point presentation' in query:
            speak("opening Power Point presentation")
            #add path when we create final ppt

            power = r"C:\\Users\\GAURAV\\Desktop\\Minor Project\\Presentation\\Voice Assistant.pptx"
            os.startfile(power)
 
        elif 'is love' in query:
            speak("It is 7th sense that destroy all other senses")
 
        elif "who are you" in query:
            speak("I am your virtual assistant created by sujit")
 
        elif 'reason for you' in query:
            speak("I was created as a Minor project by Mister Urmila ")
 
       
        elif 'open bluestack' in query:
            appli = r"C:\\ProgramData\\BlueStacks\\Client\\Bluestacks.exe"
            os.startfile(appli)
 
        elif 'news' in query:
             
            try:
                jsonObj = urlopen('''https://newsapi.org / v1 / articles?source = the-times-of-india&sortBy = top&apiKey =\\times of India Api key\\''')
                data = json.load(jsonObj)
                i = 1
                 
                speak('here are some top news from the times of india')
                print('''=============== TIMES OF INDIA ============'''+ '\n')
                 
                for item in data['articles']:
                     
                    print(str(i) + '. ' + item['title'] + '\n')
                    print(item['description'] + '\n')
                    speak(str(i) + '. ' + item['title'] + '\n')
                    i += 1
            except Exception as e:
                 
                print(str(e))
 
         
        elif 'lock window' in query:
                speak("locking the device")
                ctypes.windll.user32.LockWorkStation()
 
        elif 'shutdown system' in query:
                speak("Hold On a Sec ! Your system is on its way to shut down")
                subprocess.call('shutdown / p /f')
                 
    
        elif "don't listen" in query or "stop listening" in query:
            speak("for how much time you want to stop friday from listening commands")
            a = int(takeCommand())
            time.sleep(a)
            print(a)
 
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.nl / maps / place/" + location + "")
 
        #elif "camera" in query or "take a photo" in query:
           #echo_via_pager.capture(0, "cofine Camera ", "img.jpg")
 
        elif "restart" in query:
            subprocess.call(["shutdown", "/r"])
             
        elif "hibernate" in query or "sleep" in query:
            speak("Hibernating")
            subprocess.call("shutdown / h")
 
        elif "log off" in query or "sign out" in query:
            speak("Make sure all the application are closed before sign-out")
            time.sleep(5)
            subprocess.call(["shutdown", "/l"])
 
        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('user1.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
         
        elif "show note" in query:
            speak("Showing Notes")
            file = open("User1.txt", "r")
            print(file.read())
            speak(file.read(6))
 
        elif "cofine" in query:
             
            wishMe()
            speak("cofine 1 point o in your service Mister")
            speak(assname)
 
        elif "weather" in query:
             
            # Google Open weather website
            # to get API of Open weather
            api_key = "Api key"
            base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
            speak(" City name ")
            print("City name : ")
            city_name = takeCommand()
            complete_url = base_url + "appid =" + api_key + "&q =" + city_name
            response = requests.get(complete_url)
            x = response.json()
             
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_pressure = y["pressure"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
             
            else:
                speak(" City Not Found ")
             
 
        elif "Good Morning" in query:
            speak("A warm" +query)
            speak("How are you Mister")
            speak(assname)
 
        # most asked question from google Assistant

 
        elif "how are you" in query:
            speak("I'm fine, glad you me that")
        

        elif 'open facebook' in query:
            speak("here you go to facebook\n")
            webbrowser.open("facebook.com")   

        elif 'open instagram' in query:
            speak("here you go to instagram\n")
            webbrowser.open("instagram.com")   

            
 
        # elif "" in query:

            # Command go here
            # For adding