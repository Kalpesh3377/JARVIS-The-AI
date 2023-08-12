import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import random
import cv2
from matplotlib import pyplot as plt
from pywikihow import WikiHow, search_wikihow
import pyautogui
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voices',voices[0].id)
# text to speech
def speak(audio):
    engine.say(audio)
    # print(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am Jarvis sir. speed one tera byte memory 1 ziga byte Please tell me how may i help you")    


def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening......")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-hi')
        print(f"user said:{query}")
    except Exception as e:
        print(e)
        speak("say that again please...")
        return  "none"
    return query

def search_wikihow(query,max_results=10,lang='en-hi'):
    return list(WikiHow.search(query,max_results,lang))

if __name__ == "__main__":
    wishMe()
    while True: 
        query=takecommand().lower()

        if 'wikipedia' in query:
            speak("searching wikipedea...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            # print(results)
            speak(results)

        elif 'youtube' in query:
            speak("Ok,sir i am opening a youtube...")
            webbrowser.open("youtube.com")
        elif 'instagram' in query:
            speak("Ok,sir i am opening a instagram...")
            webbrowser.open("instagram.com")
        
        elif 'facebook' in query:
            speak("Ok,sir i am opening a facebook...")
            webbrowser.open("facebook.com")
        
        elif 'google' in query:
            speak("Ok,sir i am opening a google...")
            webbrowser.open("google.com")
        
        elif 'stack overflow' in query:
            speak("Ok,sir i am opening a stack owerflow...")
            webbrowser.open("stackoverflow.com")
        
        elif 'whatsapp' in query:
            speak("Ok,sir i am opening a whatsapp...")
            webbrowser.open("whatsapp.com")
        
        elif 'play music' in query:
            speak("Ok,sir i am playing a music for you...")
            music_dir='C:\\Users\\KALPESH\\OneDrive\\Desktop\\krishna song'
            songs=os.listdir(music_dir)
            ran=random.randint(0,len(songs)-1)
            os.startfile(os.path.join(music_dir,songs[ran]))
        
        elif 'play video' in query:
            speak("Ok,sir i am playing a video for you...")
            video_dir='C:\\Users\\KALPESH\\OneDrive\\Desktop\\scam1992'
            videos=os.listdir(video_dir)
            ran=random.randint(0,len(videos)-1)
            os.startfile(os.path.join(video_dir,videos[ran]))
        
        elif 'time' in query:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir,The time is {strtime}")
        
        elif 'open code' in query:
            speak("Ok,sir i am opening a vs code...")
            path="C:\\Users\\KALPESH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(path)
        
        elif 'open pycharm' in query:
            speak("Ok,sir i am opening a pycharm...")
            path="C:\\Program Files\\JetBrains\\PyCharm Community Edition 2021.2\\bin\\pycharm64.exe"
            os.startfile(path)
        
        elif 'word' in query:
            speak("Ok,sir i am opening a microsoft word...")
            path="C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE"
            os.startfile(path)
        
        elif 'sql' in query:
            speak("Ok,sir i am opening a sql...")
            path="C:\\oracle_application\\bin\\sqlplus.exe"
            os.startfile(path)
        
        elif 'chrome' in query:
            speak("Ok,sir i am opening a chrome...")
            path="C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(path)
        
        elif 'powerpoint' in query:
            speak("Ok,sir i am opening a powerpoint...")
            path="C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(path)
        
        elif 'command prompt' in query:
            speak("Ok,sir i am opening a command prompt...")
            path="C:\\Windows\\System32\\cmd.exe"
            os.startfile(path)
        
        elif 'team' in query:
            speak("Ok,sir i am opening a microsoft teams...")
            path="C:\\Users\\KALPESH\\OneDrive\\Desktop\\Microsoft Teams.lnk"
            os.startfile(path)
        
        elif 'idea' in query:
            speak("Ok,sir i am opening a intellij idea...")
            path="C:\\Program Files\\JetBrains\\IntelliJ IDEA Community Edition 2021.2.3\\bin\\idea64.exe"
            os.startfile(path)
        
        elif 'crypto' in query:
            webbrowser.open("crypto fear and greed index.com")
        
        elif 'search' in query:
            while True:
                speak("what you want to search")
                find=takecommand()
                if 'no' in find:
                    break
                else:
                    webbrowser.open(find+".com")

        elif 'camera' in query:
            speak("Ok,sir i am opening a camera...")
            cap=cv2.VideoCapture(0)
            if cap.isOpened():
                ret,frame=cap.read()
            else:
                ret=False
            img=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
            plt.imshow(img)
            plt.title('camera image')
            plt.show()
            cap.release()
            cv2.destroyAllWindows()
        
        elif 'shutdown' in query:
            speak("do you really want to shut down")
            reply=takecommand()
            if 'yes' in reply:
                speak("Ok,sir now i am shutdown your pc...")
                os.system('shutdown /s /t 1')
            else:
                speak("ok sir")
                continue
        elif 'restart' in query:
            speak("do you really want to restart")
            reply=takecommand()
            if 'yes' in reply:
                speak("Ok,sir now i am restart your pc...")
                os.system('shutdown /r /t 1')
            else:
                speak("ok sir")
                continue
        elif 'logout' in query:
            speak("do you really want to log out")
            reply=takecommand()
            if 'yes' in reply:
                speak("Ok,sir now i am logout your pc...")
                os.system('shutdown -l')
            else:
                speak("ok sir")
                continue
        
        elif 'activate how to do mode' in query:
            speak("How to do mode activated")
            while True:
                speak("please tell me what you want to know")
                how=takecommand()
                try:
                    if 'exit' in how or 'close' in how:
                        speak("ok sir, How to do mode is deactivate")
                        break
                    else :
                        max_results=1
                        how_to=search_wikihow(how,max_results)
                        assert len(how_to)==1
                        how_to[0].print()
                        speak(how_to[0].summary)
                except Exception as e:
                    speak("sorry sir,i am not able to find this")
        elif 'close' in query:
            speak("Thankyou for using me...")
            exit()
        elif 'volume up' or 'volumeup' in query:
            pyautogui.press("volumeup")
        elif 'volume down' or 'volumedown' in query:
            pyautogui.press("volumedown")
        elif 'volume mute' or 'volumemute' in query:
            pyautogui.press("volumemute")
