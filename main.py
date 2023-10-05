from tkinter import *
import json
from difflib import get_close_matches
from tkinter import messagebox
import pyttsx3

engine = pyttsx3.init() #This creates instance of Engine class

voice = engine.getProperty('voices')
engine.setProperty('voice', voice[1].id)
# Functionality part


def search():
    data = json.load(open('data.json'))
    word = EnterWordEntry.get()
    word = word.lower()
    if word in data:
        meaning = data[word]
        Textarea.delete(1.0, END)
        for item in meaning:
            Textarea.insert(END, U'\u2022'+item+'\n\n')

    elif len(get_close_matches(word, data.keys()))>0:
        close_match = get_close_matches(word, data.keys())[0]
        res = messagebox.askyesno('Confirm', 'Did you mean '+close_match+' instead?')
        if res==True:
            EnterWordEntry.delete(0,END)
            EnterWordEntry.insert(END, close_match)
            meaning = data[close_match]
            Textarea.delete(1.0, END)
            for item in meaning:
                Textarea.insert(END, u'\u2022' + item + '\n\n')
        else:
            messagebox.showerror('Error','The word does not exist please recheck it')
            EnterWordEntry.delete(0, END)
            Textarea.delete(1.0, END)
    else:
        messagebox.showinfo('Information','The word does not exist')
        EnterWordEntry.delete(0, END)
        Textarea.delete(1.0, END)


def clear():
    EnterWordEntry.delete(0, END)
    Textarea.delete(1.0, END)


def iexit():

    ress = messagebox.askyesno('Confirm', 'Do you want to exit?')

    if ress==True:
        root.destroy()
    else:
        pass


def wordaudio():
    engine.say(EnterWordEntry.get())
    engine.runAndWait()


def meaningaudio():
    engine.say(Textarea.get(1.0, END))
    engine.runAndWait()
# GUI part


root = Tk()
root.geometry('1000x626+100+30')
root.title('Talking Dictionary')
root.resizable(0, 0)

bgImage = PhotoImage(file='bg.png')
bgLabel = Label(root, image=bgImage)
bgLabel.place(x=0, y=0)

EnterWordLabel = Label(root, text='Enter Word', font=('Areal', 29, 'bold'), foreground='Black', background='whitesmoke')
EnterWordLabel.place(x=530, y=20)

EnterWordEntry = Entry(root, font=('arial', 23, 'bold'), justify=CENTER, bd=8, relief=GROOVE)
EnterWordEntry.place(x=510, y=80)

SearchImage = PhotoImage(file='search.png')
SearchButton=Button(root,image=SearchImage,bd=0,bg='whitesmoke',cursor='hand2',activebackground='whitesmoke',command=search)
SearchButton.place(x=620, y=150)

MicImage = PhotoImage(file='mic.png')
MicButton = Button(root, image=MicImage, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke', command=wordaudio)
MicButton.place(x=710, y=153)

MeaningLabel = Label(root, text='Meaning', font=('Areal', 29, 'bold'), foreground='Black', background='whitesmoke')
MeaningLabel.place(x=580, y=240)

Textarea = Text(root, font=('areal', 18, 'bold'), width=34, height=8, bd=8, relief=GROOVE)
Textarea.place(x=460, y=300)

AudioImage = PhotoImage(file='microphone.png')
AudioButton = Button(root, image=AudioImage, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke', command=meaningaudio)
AudioButton.place(x=530, y=555)

ClearImage = PhotoImage(file='clear.png')
ClearButton = Button(root, image=ClearImage, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke', command=clear)
ClearButton.place(x=660, y=555)

ExitImage = PhotoImage(file='exit.png')
ExitButton = Button(root, image=ExitImage, bd=0, bg='whitesmoke', cursor='hand2', activebackground='whitesmoke', command=iexit)
ExitButton.place(x=790, y=555)


def enter_function(event):
    SearchButton.invoke()


root.bind('<Return>', enter_function)

root.mainloop()
