import pyttsx3
import json,time
import requests
from win10toast import ToastNotifier


apikey="x5LwiyteKxh6pom9DREhp0h1OIx1"  #enter here your apikey

# function for text to speech
def speech(audio):
    engine=pyttsx3.init('sapi5')
    engine.setProperty('rate',175)
    engine.say(audio)
    engine.runAndWait()

#function for notification
def Notification(result):
    noti=ToastNotifier()
    noti.show_toast("live cricket",result,duration=10)

def match_id():
    url="https://cricapi.com/api/matches"
    
    news=requests.get(f"{url}?apikey={apikey}")
    news_d=json.loads(news.content)
    matches=news_d['matches']
    m={}
    for i,n in enumerate(matches):
        m[i]=n["unique_id"]
        print(i,n['unique_id'],n["team-2"]+ "vs " +n["team-1"])

    n=int(input("enter match number:"))#taking match id   
    print(m[n])
    return m[n]
def score(id):
    while True:
        url1='https://cricapi.com/api/cricketScore'
        ab=requests.get(f"{url1}?unique_id={id}&apikey={apikey}")
        match1=json.loads(ab.content)
        Notification(match1['stat'])#calling notification function
        result=match1['stat']
        speech(result)#calling speech function
        time.sleep(30)
if __name__ == "__main__":
    id=match_id()
    score(id)