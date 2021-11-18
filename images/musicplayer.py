from tkinter import *
from tkinter import font
from tkinter.font import BOLD 
import pygame


current_volume = float(0.5)


root = Tk()
root.title("My music player")
root.geometry("500x700")

bg = PhotoImage(file = "C:/Users/Dhruvi Dharia/Desktop/python/images/lofi1.png")

# create a label 
my_label = Label(root, image=  bg)
my_label.place(x = 0, y = 0, relwidth=1, relheight=1)

# text of the image 
my_text = Label(root, text="hello vi")
my_label.place()

# Labels 
Label(root, text="Custom music player", font=("Rubik", 16, BOLD), fg= "#7FFF00", bg = "black").place(relx= 0.5, rely=0, anchor="n")
Label(root, text="Please select a music track you would like to play", font=("Rubik", 12,BOLD),fg= "#7FFF00",bg="black").place(relx = 0.5, rely=0.1, anchor = "n")
Label(root, text="Volume").grid(sticky="N", row = 4)
song_title_label = Label(root, font=("Calibri", 16))
song_title_label.grid(stick="N", row = 3)
volume_label = Label(root, font=("Calibri", 16))
volume_label.grid(sticky="N", row = 5)

# buttons

Button(root, text = "-", font = ("Calibri", 20, BOLD),fg= "#00b001", bg = "black").place(relx=0, rely=1, anchor="sw")
Button(root, text = "+", font = ("Calibri", 20,BOLD ), fg= "#00b001", bg = "black").place(relx = 1, rely=1, anchor="se")

pause = PhotoImage(file="C:/Users/Dhruvi Dharia/Desktop/python/images/pause.png")
img_label = Label(image= pause)
img_label.place(relx = 0.6, rely=1, anchor= "sw")

pause_button = Button(root,image= pause )
pause_button.place(relx = 0.6, rely=1, anchor="sw")

resume =PhotoImage(file= "C:/Users/Dhruvi Dharia/Desktop/python/images/play.png")
resume_label = Label(image= resume)
resume_label.place(relx = 0.4, rely= 1,anchor="s" )

pygame.mixer.init()

def play():
    
        pygame.mixer.music.load('C:/Users/Dhruvi Dharia/Desktop/python/images/raatan.mp3')
        pygame.mixer.music.play(loops=0)
    
def play1():
    pygame.mixer.music.load('C:/Users/Dhruvi Dharia/Desktop/python/images/let.mp3')
    pygame.mixer.music.play(loops=0)

def play2():
    pygame.mixer.music.load('C:/Users/Dhruvi Dharia/Desktop/python/images/need.mp3')
    pygame.mixer.music.play(loops=0)

def play3():
    pygame.mixer.music.load('C:/Users/Dhruvi Dharia/Desktop/python/images/arms.mp3')
    pygame.mixer.music.play(loops=0)

def play4():
    pygame.mixer.music.load('C:/Users/Dhruvi Dharia/Desktop/python/images/king.mp3')
    pygame.mixer.music.play(loops=0)

def play5():
    pygame.mixer.music.load('C:/Users/Dhruvi Dharia/Desktop/python/images/tesher.mp3')
    pygame.mixer.music.play(loops=0)

def play6():
    pygame.mixer.music.load('C:/Users/Dhruvi Dharia/Desktop/python/images/arcade.mp3')
    pygame.mixer.music.play(loops=0)


def stop():
    pygame.mixer.music.stop()



song_button1 = Button(root, text="Raataan Lambiyan  Shershaah  ", font=("Rubik", 12, BOLD),fg="#7FFF00", borderwidth=0, bg ="black", command=play)
song_button1.place(relx = 0.15, rely=0.8, anchor="w")

song_button2 = Button(root, text="Alec Benjamin - Let Me Down Slowly", font=("Rubik", 12, BOLD),  command=play1  , fg ="#7FFF00",borderwidth=0, bg="black")
song_button2.place(relx = 0.15, rely=0.7, anchor="w")

song_button3 = Button(root, text="Doja Cat - Need To Know", font=("Rubik",12, BOLD), fg="#7FFF00", borderwidth=0, bg ="black",command=play2)
song_button3.place(relx = 0.15, rely = 0.6, anchor="w")

song_button4 = Button(root, text="XXXTENTACION & Lil Pump - Arms Around You ", font=("Rubik", 12, BOLD) ,fg=  "#7FFF00",bg = "black",borderwidth=0,  command=play3)
song_button4.place(relx = 0.15, rely = 0.5,anchor="w")

song_button5 = Button(root, text="King - Tu Aake Dekhle | The Carnival | The Last Ride ", font=("Rubik", 12, BOLD), bg ="black",fg="#7FFF00" ,command=play4)
song_button5.place(relx = 0.15, rely= 0.4, anchor="w")

song_button6 = Button(root, text="Arcade x Mann Mera (Mashup) Full Version|Gravero", font=("Rubik", 12, BOLD), bg = "black", fg ="#7FFF00", command=play6 )
song_button6.place(relx = 0.15, rely = 0.3, anchor="w")

stop_button = Button(root, text='stop', command= stop)
stop_button.place(relx = 0.5, rely= 1, anchor="s")

son1=PhotoImage(file="C:/Users/Dhruvi Dharia/Desktop/python/images/song1.png")
son1_label=Label(image=son1)
son1_label.place(relx=0.075, rely=0.4,anchor="w")

son2=PhotoImage(file="C:/Users/Dhruvi Dharia/Desktop/python/images/arm.png")
son2_label=Label(image=son2)
son2_label.place(relx=0.075, rely=0.5,anchor="w")

son3=PhotoImage(file="C:/Users/Dhruvi Dharia/Desktop/python/images/need1.png")
son3_label=Label(image=son3)
son3_label.place(relx=0.075, rely=0.6,anchor="w")

son4=PhotoImage(file="C:/Users/Dhruvi Dharia/Desktop/python/images/let1.png")
son4_label=Label(image=son4)
son4_label.place(relx=0.075, rely=0.7,anchor="w")

son5=PhotoImage(file="C:/Users/Dhruvi Dharia/Desktop/python/images/raatan.png")
son5_label=Label(image=son5)
son5_label.place(relx=0.075, rely=0.8,anchor="w")

son6=PhotoImage(file="C:/Users/Dhruvi Dharia/Desktop/python/images/arcade1.png")
son6_label=Label(image=son6)
son6_label.place(relx=0.075, rely=0.3,anchor="w")


root.mainloop()




