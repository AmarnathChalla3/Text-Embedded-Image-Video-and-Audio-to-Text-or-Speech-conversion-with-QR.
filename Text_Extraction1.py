from tkinter import *
from pytesseract import pytesseract
import wave, math, contextlib
import speech_recognition as sr
from moviepy.editor import AudioFileClip
from moviepy.editor import VideoFileClip
import pyttsx3 as pp
import pyqrcode
from PIL import Image
root = Tk()
root.geometry('1000x600+80+10')
root.title('TEXT EXTRACTION FROM MULTI-MEDIA DEVELOPED BY TEAM SGMA')
root.resizable(0, 0)
meaning = ''
peopleimage = PhotoImage(file='people.png')
searchimage = PhotoImage(file='search.png')
audioimage = PhotoImage(file='microphone.png')
speakerimage = PhotoImage(file='speaker.png')
timage = PhotoImage(file='t button.png')
qrimage = PhotoImage(file='qr.png')

rrimage = PhotoImage(file='Amar01.png')
cbimage = PhotoImage(file='Mani0.png')
shaimage = PhotoImage(file='Santhosh0.png')
gnimage = PhotoImage(file='Gnani0.png')

engine = pp.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # [0]for male

def peptxt():
    newWindow = Toplevel(root)
    newWindow.title("TEAM SGMA")
    newWindow.geometry("600x550")
    Label(newWindow, text="Team members", font=('castellar', 20, 'bold'), fg='red3',bg='whitesmoke').pack()

    Label1 = Label(newWindow, text='Challa.Amarnath\n Reg.no : 99210041022', font=('castellar', 15, 'bold'), fg='red3',
                   bg='whitesmoke')
    Label1.place(x=200, y=100)

    Label1 = Label(newWindow, text='Ch.SriManikanta\n Reg.no : 9921004140', font=('castellar', 15, 'bold'), fg='red3',
                   bg='whitesmoke')
    Label1.place(x=200, y=250)

    Label1 = Label(newWindow, text='Ch.J.Santhosh Kumar\n Reg.no : 9921004135', font=('castellar', 15, 'bold'), fg='red3',
                   bg='whitesmoke')
    Label1.place(x=200, y=400) 
    
    Label1 = Label(newWindow, text='C.C.Gnaneshwar Naidu\n Reg.no : 9921004142', font=('castellar', 15, 'bold'), fg='red3',
                   bg='whitesmoke')
    Label1.place(x=200, y=550)

    pic1 = Button(newWindow, image=rrimage, bd=0, activebackground='whitesmoke', cursor='hand2')
    pic1.place(x=50, y=80)

    pic2 = Button(newWindow, image=cbimage, bd=0, activebackground='whitesmoke', cursor='hand2')
    pic2.place(x=50, y=225)

    pic3 = Button(newWindow, image=shaimage, bd=0, activebackground='whitesmoke', cursor='hand2')
    pic3.place(x=50, y=380)
    
    pic4 = Button(newWindow, image=gnimage, bd=0, activebackground='whitesmoke', cursor='hand2')
    pic4.place(x=50, y=535)


def imgtxt():
    newWindow = Toplevel(root)
    newWindow.title("IMAGE TO TEXT CONVERSION - DEVELOPED BY TEAM SGMA")
    newWindow.geometry("900x600")
    Label(newWindow,text="Image to text extraction window", font=('castellar', 20, 'bold'), fg='red3', bg='whitesmoke').pack()

    Label1 = Label(newWindow, text='Enter the File Name / PATH', font=('castellar', 15, 'bold'), fg='red3', bg='whitesmoke')
    Label1.place(x=50, y=70)

    Label2 = Label(newWindow, text='Extracted Text :', font=('castellar', 15, 'bold'), fg='red3',bg='whitesmoke')
    Label2.place(x=50, y=210)

    entry = Entry(newWindow, font=('Times New Roman', 18, 'italic'), bd=8, relief=GROOVE,width=30,)
    entry.place(x=50, y=130)
    entry.focus_set()

    textarea = Text(newWindow, font=('Times New Roman', 18, 'italic'), bd=8, relief=GROOVE, height=9, width=60, wrap='word')
    textarea.place(x=50, y=250)

    textarea1 = Text(newWindow, font=('Times New Roman', 18, 'italic'), bd=8, relief=GROOVE, height=1, width=6,
                    wrap='word')
    textarea1.place(x=300, y=200)

    def search():
        A = entry.get()
        path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        textarea1.insert(END,"20%")
        textarea1.delete("1.0", "end")
        path_to_image = (A)
        textarea1.insert(END,"40%")
        textarea1.delete("1.0", "end")
        pytesseract.tesseract_cmd = path_to_tesseract
        textarea1.insert(END, "60%")
        textarea1.delete("1.0", "end")
        img = Image.open(path_to_image)
        textarea1.insert(END, "80%")
        textarea1.delete("1.0", "end")
        text=pytesseract.image_to_string(img)
        print(text)
        textarea1.insert(END, "100%")
        textarea.delete(1.0, END)
        textarea.insert(END, text)

    def audio():
        engine.say(textarea.get(1.0, END))
        engine.runAndWait()

    def qr():
        A = entry.get()
        path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
        path_to_image = (A)
        pytesseract.tesseract_cmd = path_to_tesseract
        img = Image.open(path_to_image)
        text = pytesseract.image_to_string(img)
        s = text
        url = pyqrcode.create(s)
        url.png('myqr.png', scale=8)
        img = Image.open('myqr.png')
        img.show()

    searchButton = Button(newWindow, image=searchimage, bd=0, activebackground='whitesmoke', cursor='hand2',
                          command=search)
    searchButton.place(x=500, y=120)

    audioButton = Button(newWindow, image=speakerimage, bd=0, activebackground='whitesmoke', cursor='hand2',
                   command=audio)
    audioButton.place(x=600, y=120)

    qrButton = Button(newWindow, image=qrimage, bd=0, activebackground='whitesmoke', cursor='hand2',
                      command=qr)
    qrButton.place(x=700, y=120)


def videotxt():
    newWindow = Toplevel(root)
    newWindow.title("VIDEO TO TEXT CONVERSION - DEVELOPED BY TEAM SGMA")
    newWindow.geometry("900x600")
    Label(newWindow, text="Video to text extraction window", font=('castellar', 20, 'bold'), fg='red3', bg='whitesmoke').pack()

    Label1 = Label(newWindow, text='Enter the Video File Name / PATH :', font=('castellar', 15, 'bold'), fg='red3', bg='whitesmoke')
    Label1.place(x=50, y=120)

    Label2 = Label(newWindow, text='Extracted Text :', font=('castellar', 15, 'bold'), fg='red3', bg='whitesmoke')
    Label2.place(x=50, y=210)

    entry = Entry(newWindow, font=('Times New Roman', 18, 'italic'), bd=8, relief=GROOVE, width=25)
    entry.place(x=420, y=110)
    entry.focus_set()

    textarea = Text(newWindow, font=('Times New Roman', 18, 'italic'), bd=8, relief=GROOVE, height=9, width=60, wrap='word')
    textarea.place(x=50, y=250)

    textarea1 = Text(newWindow, font=('Times New Roman', 18, 'italic'), bd=8, relief=GROOVE, height=1, width=8,
                     wrap='word')
    textarea1.place(x=300, y=200)

    textarea2 = Text(newWindow, font=('Times New Roman', 18, 'italic'), bd=8, relief=GROOVE, height=1, width=14,
                     wrap='word')
    textarea2.place(x=440, y=200)
    textarea1.insert(END, " 0%")
    textarea2.insert(END, "Please wait..")

    def search():
        B = entry.get()
        transcribed_audio_file_name = "transcribed_speech.wav"
        
        video_clip = VideoFileClip(B)
        audioclip = video_clip.audio
        audioclip.write_audiofile(transcribed_audio_file_name)
        
        r = sr.Recognizer()
        with sr.AudioFile(transcribed_audio_file_name) as source:
            audio = r.record(source)
        text = r.recognize_google(audio)
        
        with open("transcription.txt", "w") as f:
            f.write(text)
        
        textarea1.delete("1.0", "end")
        textarea1.insert(END, " 100%")

    def text():
        fa = open("transcription.txt", "r")
        content = fa.read()
        textarea.delete(1.0, END)
        textarea.insert(END, content)
        fa.close()

    def qr():
        fa = open("transcription.txt", "r")
        content = fa.read()
        s = content
        url = pyqrcode.create(s)
        url.png('myqr.png', scale=8)
        img = Image.open('myqr.png')
        img.show()

    searchButton = Button(newWindow, image=searchimage, bd=0, activebackground='whitesmoke', cursor='hand2',
                          command=search)
    searchButton.place(x=750, y=100)

    textButton = Button(newWindow, image=timage, bd=0, activebackground='whitesmoke', cursor='hand2',
                          command=text)
    textButton.place(x=650, y=170)

    qrButton = Button(newWindow, image=qrimage, bd=0, activebackground='whitesmoke', cursor='hand2',
                      command=qr)
    qrButton.place(x=750, y=170)



def audiotxt():
    newWindow = Toplevel(root)
    newWindow.title("AUDIO TO TEXT CONVERSION - DEVELOPED BY TEAM SGMA")
    newWindow.geometry("900x600")
    Label(newWindow, text="Audio to text extraction window", font=('castellar', 20, 'bold'), fg='red3', bg='whitesmoke').pack()

    Label2 = Label(newWindow, text='Extracted Text :', font=('castellar', 15, 'bold'), fg='red3', bg='whitesmoke')
    Label2.place(x=50, y=210)

    Label1 = Label(newWindow, text='Enter the file name/path :', font=('castellar', 15, 'bold'), fg='red3', bg='whitesmoke')
    Label1.place(x=50, y=45)

    entry = Entry(newWindow, font=('Times New Roman', 18, 'italic'), bd=8, relief=GROOVE, width=30)
    entry.place(x=50, y=80)
    entry.focus_set()

    textarea1 = Text(newWindow, font=('Times New Roman', 18, 'italic'), bd=8, relief=GROOVE, height=1, width=40, wrap='word')
    textarea1.place(x=50, y=140)

    textarea = Text(newWindow, font=('Times New Roman', 18, 'italic'), bd=8, relief=GROOVE, height=9, width=60, wrap='word')
    textarea.place(x=50, y=250)

    txt2 = "Click on mic and say something.......... "
    print(txt2)
    textarea1.insert(END,txt2)

    def search():
        A = entry.get()
        filename = A
        r = sr.Recognizer()
        with sr.AudioFile(filename) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data)
            print(text)
        textarea.delete(1.0, END)
        textarea.insert(END, text)

    def mic():
        textarea.delete(1.0, END)
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Please say something")
            audio = r.listen(source)
            textarea1.delete(1.0, END)
            txt2 = "Recognizing now ... "
            textarea1.insert(END, txt2)
        try:
            text = ("You said: " + r.recognize_google(audio))
        except:
            text = ('Your voice is not clear please say it again!!')
        print(text)
        textarea.delete(1.0, END)
        textarea.insert(END, text)

    def audio():
        engine.say(textarea.get(1.0, END))
        engine.runAndWait()


    micButton = Button(newWindow, image=audioimage, bd=0, activebackground='whitesmoke', cursor='hand2',
                          command=mic)
    micButton.place(x=570, y=130)

    searchButton = Button(newWindow, image=searchimage, bd=0, activebackground='whitesmoke', cursor='hand2',
                       command=search)
    searchButton.place(x=450, y=70)

    audioButton = Button(newWindow, image=speakerimage, bd=0, activebackground='whitesmoke', cursor='hand2',
                   command=audio)
    audioButton.place(x=660, y=130)


#BACKGROUND IMAGE
bgimage = PhotoImage(file='bg.png')
bgLabel = Label(root, image=bgimage)
bgLabel.place(x=0, y=0)
#LABEL
enterwordLabel = Label(root, text='Text Extraction', font=('castellar', 29, 'bold'), fg='red3', bg='whitesmoke')
enterwordLabel.place(x=280, y=20)

imgtotxtimage = PhotoImage(file='button_image-to-text.png')
videototxtimage = PhotoImage(file='button_video-to-text.png')
audiototxtimage = PhotoImage(file='button_audio-to-text.png')


imgtotxt = Button(root, image=imgtotxtimage , bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                      command=imgtxt)
imgtotxt.place(x=350, y=200)

pep = Button(root, image=peopleimage , bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                      command=peptxt)
pep.place(x=50, y=50)

videototxt = Button(root, image=videototxtimage, bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                      command=videotxt)
videototxt.place(x=350, y=300)

audiototxt = Button(root, image=audiototxtimage , bd=0, bg='whitesmoke', activebackground='whitesmoke', cursor='hand2',
                      command=audiotxt)
audiototxt.place(x=350, y=400)

root.mainloop()