import tkinter as tk
import boto3 as b3
import os
import sys
from tempfile import gettempdir
from contextlib import closing
main=tk.Tk()
main.geometry("600x350")
main.title("TTS Translator Polly")
Example=tk.Text(main,height=12)
Example.pack()
def readtranslated():
    aws_cons=b3.session.Session(profile_name='awstts')
    ttsclient=aws_cons.client(service_name="polly",region_name='ap-south-1',)
    translateclient=aws_cons.client(service_name="translate",region_name='ap-south-1')
    result=Example.get("1.0","end")
    responsetran=translateclient.translate_text(Text=result,SourceLanguageCode='en',TargetLanguageCode='es')
    print(responsetran)
    translatedresult=responsetran.get('TranslatedText')
    responseread=ttsclient.synthesize_speech(OutputFormat='mp3',VoiceId='Brian',Text=translatedresult,Engine='neural')
    print(responseread)
    if "AudioStream" in responseread:
        with closing(responseread['AudioStream']) as audio:
            output=os.path.join(gettempdir(),"speech.mp3")
            try:
                with open(output,"wb") as file:
                    file.write(audio.read())
            except IOError as error:
                print(error)
                sys.exit(-1)
    else:
        print("No Audio Found")
        sys.exit(-1)
    if sys.platform=='win32':
        os.startfile(output)
def read():
    aws_cons=b3.session.Session(profile_name='awstts')
    ttsclient=aws_cons.client(service_name="polly",region_name='ap-south-1',)
    result=Example.get("1.0","end")
    responseread=ttsclient.synthesize_speech(OutputFormat='mp3',VoiceId='Brian',Text=result,Engine='neural')
    print(responseread)
    if "AudioStream" in responseread:
        with closing(responseread['AudioStream']) as audio:
            output=os.path.join(gettempdir(),"speech.mp3")
            try:
                with open(output,"wb") as file:
                    file.write(audio.read())
            except IOError as error:
                print(error)
                sys.exit(-1)
    else:
        print("No Audio Found")
        sys.exit(-1)
    if sys.platform=='win32':
        os.startfile(output)
ButtonRead=tk.Button(main,height=2,width=12,text="Read Translated",command=readtranslated)
ButtonRead.pack() 
ButtonRead1=tk.Button(main,height=2,width=12,text="Read",command=read)
ButtonRead1.pack()
main.mainloop()