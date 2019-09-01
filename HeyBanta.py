import pyttsx3
import datetime
import win32com.client
import speech_recognition as sr
import wikipedia
import requests
import importlib

#Operating System
import OperatingSystem as od
c1=od.OpeartingSystem()




#Required For Setup of microsoft Speech Api for voice Recognition

engine=pyttsx3.init('sapi5')

#Get Installed Voices list
voices=engine.getProperty('voices')
    
#Set Engine Voice
engine.setProperty("voice",voices[0].id)

#computer will Speak in selected voice
def Speak(audio):
    '''
    it Will Take Input text And Speak.
    '''
    engine.say(audio)
    engine.runAndWait()
def WishMe():
    hour=int(datetime.datetime.now().hour)

    if(hour>=0 and hour<12):
        Speak("Good Morning")
    elif(hour>=12 and hour<18):
        Speak("Good Afternoon")
    else:
        Speak("Good Evening")
    Speak("Please tell me how may i help you")
def takeSound():
    '''
    It Takes Microphone input From user and
    return string output
    '''
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        print("Listening....")
        r.adjust_for_ambient_noise(source)
        r.pause_threshold=0.6
        audio=r.listen(source)
    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
    except:
        return "None"
    return query
    
def Rating(movie):
    url=r'http://www.omdbapi.com/?apikey=AddYourownkey&t={}'.format(movie.replace(" ","%20"))
    response=requests.get(url)
    if(response.status_code==200):
        res=response.json()
        if res['Response']=='False':
           return "None" 
        else:
            return res['imdbRating']
    else:
        return "None"
def Display(text):
    print(text)
def Movie(query):
    Display("\nUser:{}".format(query))
    Speak("Finding Movie rating")
    query=query.replace("rating","")
    query=query.replace("movie","")
    resp=Rating(query)
    if(resp!='None'):
        res='{} Movie have {} Rating Accordingly IMDB'.format(query,resp)
        Display('Computer:{}'.format(res))
        Speak(res)
    else:
        res='Movie Rating Not Found'
        Display('Computer:{}'.format(res))
        Speak(res)
def Wikipeda(query):
    Speak("Searching Wikipedia")
    query=query.replace("wikipedia","")
    result=wikipedia.summary(query,sentences=3)
    Speak(result)
    Speak("According to wikipedia")
def OpenWebsite(url):
    import webbrowser
    webbrowser.open(url)
if __name__=="__main__":
    WishMe()
    while True:
        query=takeSound().lower()
        print(query)
        if 'wikipedia' in query:
            Wikipeda(query)
        if 'rating' in query or 'movie' in query:
            Movie(query)
        if 'battery' in query or 'power' in query or 'charging kiti aahe' in query:
            res=c1.GetBattery()
            if(res['status']):
                Speak("currently Battery have {} Percent And Power Cabel {}".format(res['percent'],res['plugged']))
        if 'open website' in query or 'website' in query:
            Speak('Which Website Do you Want to Open')
            while True:
                qry=takeSound().lower()
                if(qry!='none'):
                    break
            resp='www.{}.com'.format(qry)
            print(resp,qry)
            OpenWebsite(resp)
            Speak("I am Opening {}".format(resp) )
        if 'time' in query:
            res=c1.CurrentTime()
            Speak(res)
        if 'quit' in query:
            Speak("Shutdown Process Started ")
            Speak("Quited Successfully")
            break
