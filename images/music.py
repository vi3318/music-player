from tkinter import *
from tkinter import font
from tkinter.font import BOLD 
import pygame
import time
import os
import pyaudio

current_volume = float(0.5)

root = Tk()
root.title("My music player")
root.geometry("500x600")

bg = PhotoImage(file = "C:/Users/Dhruvi Dharia/Desktop/python/images/peach.png")

# create a label 
my_label = Label(root, image=bg)
my_label.place(x = 0, y = 0, relwidth=1, relheight=1)

# text of the image 
my_text = Label(root, text="hello vi")
my_label.place()

exit_button = Button(root, text="Exit", command=root.destroy)
exit_button.place(relx = 1, rely = 0, anchor="w")





# Labels 
Label(root, text="Custom music player", font=("Phosphate", 20, BOLD), fg= "black", bg = "floralwhite").place(relx= 0.5, rely=0, anchor="n")
Label(root, text="Please select a music track you would like to play", font=("Rubik", 12,BOLD),fg= "black",bg="floralwhite").place(relx = 0.5, rely=0.15, anchor = "n")

profilepic=PhotoImage(file="C:/Users/Dhruvi Dharia/Desktop/python/images/h1.gif")
profile=Label(root, image=profilepic)
profile.place(relx=0, rely=0)

# buttons

Button(root, text = "-", font = ("Calibri", 20, BOLD),fg= "black", bg = "white").place(relx=0, rely=1, anchor="sw")
Button(root, text = "+", font = ("Calibri", 20,BOLD ), fg= "black", bg = "white").place(relx = 1, rely=1, anchor="se")

pygame.mixer.init()

def play():
    
        pygame.mixer.music.load('C:/Users/Dhruvi Dharia/Desktop/python/images/remix.mp3')
        pygame.mixer.music.play(loops=0)
        
def playvid():
    os.system("love.mp4")
    
def play1():
    pygame.mixer.music.load('C:/Users/Dhruvi Dharia/Desktop/python/images/let.mp3')
    pygame.mixer.music.play(loops=0)
    
def playvid1():
    os.system("letvid.mp4")

def play2():
    pygame.mixer.music.load('C:/Users/Dhruvi Dharia/Desktop/python/images/need.mp3')
    pygame.mixer.music.play(loops=0)

def playvid2():
    os.system("need.mp4")

def play3():
    pygame.mixer.music.load('C:/Users/Dhruvi Dharia/Desktop/python/images/arms.mp3')
    pygame.mixer.music.play(loops=0)

def playvid3():
    os.system("arms.mp4")

def play4():
    pygame.mixer.music.load('C:/Users/Dhruvi Dharia/Desktop/python/images/king.mp3')
    pygame.mixer.music.play(loops=0)

def playvid4():
    os.system("tu.mp4")

def play5():
    pygame.mixer.music.load('C:/Users/Dhruvi Dharia/Desktop/python/images/tesher.mp3')
    pygame.mixer.music.play(loops=0)

def play6():
    pygame.mixer.music.load('C:/Users/Dhruvi Dharia/Desktop/python/images/arcade.mp3')
    pygame.mixer.music.play(loops=0)
    
    

def playvid6():
    os.system("gravero.mp4")


def stop():
    pygame.mixer.music.stop()

global paused
paused=False

def pause(is_paused):
    global paused
    paused= is_paused
    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        pause= True

def playmusiic():
        
    pygame.mixer.music.unpause()


pause1 = PhotoImage(file="C:/Users/Dhruvi Dharia/Desktop/python/images/pause.png")
img_label = Label(image= pause1)


pause_button = Button(root,image= pause1 , bg="black",command= lambda: pause(paused))
pause_button.place(relx = 0.5, rely=1, anchor="s")

resume =PhotoImage(file= "C:/Users/Dhruvi Dharia/Desktop/python/images/play.png")
resume_label = Button(image= resume, bg="black",command=playmusiic)
resume_label.place(relx = 0.45, rely= 1,anchor="se" )


song_button1 = Button(root, text="  love nwantiti(feat.Dj Yo! & AL'EL)- Remix   ", font=("Rubik", 12, BOLD),fg="black", borderwidth=0, bg="#FFE4C4", command=play)
song_button1.place(relx = 0.15, rely=0.79, anchor="w")

song1_button = Label(root, text= "  CKay, DJ Yo, AX'EL", font=("Rubik", 9, BOLD), bg="#FFE4C4", fg="grey")
song1_button.place(relx = 0.16, rely=0.8)

song_button2 = Button(root, text="  Let Me Down Slowly", font=("Rubik", 12, BOLD),  command=play1  , fg=  "black",borderwidth=0, bg="#FFE4C4")
song_button2.place(relx = 0.15, rely=0.69, anchor="w")

song2_button=Label(root, text="  Alec Benjamin", font=("Rubik", 9, BOLD), bg="#FFE4C4", fg="grey")
song2_button.place(relx=0.16, rely=0.7)

song_button3 = Button(root, text="  Need to Know", font=("Rubik",12, BOLD), borderwidth=0, fg=  "black",bg ="#FFE4C4",command=play2)
song_button3.place(relx = 0.15, rely = 0.59, anchor="w")

song3_button = Label(root, text="  Dojo Cat", font=("Rubik",9, BOLD), fg="grey", bg="#FFE4C4")
song3_button.place(relx = 0.16, rely = 0.6)


song_button4 = Button(root, text="  Arms Around You(feat. Maluma & Swae Lee) ", font=("Rubik", 12, BOLD) ,fg=  "black",bg = "#FFE4C4",borderwidth=0,  command=play3)
song_button4.place(relx = 0.15, rely = 0.49,anchor="w")

song4_button=Label(root, text="  XXXTENTACION & Lil Pump ", font=("Rubik",9, BOLD), fg="grey", bg="#FFE4C4")
song4_button.place(relx=0.16, rely=0.5)

song_button5 = Button(root, text="  Tu Aake Dekhle | The Carnival | The Last Ride ", font=("Rubik", 12, BOLD), bg ="#FFE4C4",borderwidth=0,fg="black" ,command=play4)
song_button5.place(relx = 0.15, rely= 0.39, anchor="w")

song5_button=Label(root, text="   King ", font=("Rubik",9, BOLD), fg="grey", bg="#FFE4C4")
song5_button.place(relx=0.16, rely=0.4)

song_button6 = Button(root, text="   Arcade x Mann Mera (Mashup) Full Version|Gravero", font=("Rubik", 12, BOLD), bg = "#FFE4C4",borderwidth=0, fg ="black", command=play6 )
song_button6.place(relx = 0.15, rely = 0.29, anchor="w")

song4_button=Label(root, text="   Gravero mashup ", font=("Rubik",9, BOLD), fg="grey", bg="#FFE4C4")
song4_button.place(relx=0.16, rely=0.3)


stopimage=PhotoImage(file="C:/Users/Dhruvi Dharia/Desktop/python/images/stop1.png")
stop_button = Button(image=stopimage, bg="black",command= stop)
stop_button.place(relx = 0.6, rely= 1, anchor="s")

son1=PhotoImage(file="C:/Users/Dhruvi Dharia/Desktop/python/images/tu.png")
son1_label=Button(image=son1, command=playvid4, borderwidth=0)
son1_label.place(relx=0.075, rely=0.4,anchor="w")

son2=PhotoImage(file="C:/Users/Dhruvi Dharia/Desktop/python/images/arm1.png")
son2_label=Button(image=son2, command=playvid3, borderwidth=0)
son2_label.place(relx=0.075, rely=0.5,anchor="w")

son3=PhotoImage(file="C:/Users/Dhruvi Dharia/Desktop/python/images/need1.png")
son3_label=Button(image=son3, command=playvid2, borderwidth=0)
son3_label.place(relx=0.075, rely=0.6,anchor="w")

son4=PhotoImage(file="C:/Users/Dhruvi Dharia/Desktop/python/images/let1.png")
son4_label=Button(image=son4, command=playvid1, borderwidth=0)
son4_label.place(relx=0.075, rely=0.7,anchor="w")

son5=PhotoImage(file="C:/Users/Dhruvi Dharia/Desktop/python/images/love2.png")
son5_label=Button(image=son5, command=playvid, borderwidth=0)
son5_label.place(relx=0.075, rely=0.8,anchor="w")

son6=PhotoImage(file="C:/Users/Dhruvi Dharia/Desktop/python/images/arcade.png")
son6_label=Button(image=son6,command=playvid6,borderwidth = 0,relief="groove")
son6_label.place(relx=0.075, rely=0.3,anchor="w")


root.mainloop()

