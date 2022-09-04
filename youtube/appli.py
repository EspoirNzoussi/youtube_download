import tkinter.messagebox
import pywhatkit
from  tkinter import*
from tkinter import filedialog
from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube
import shutil
import pywhatkit

#********************************************Les Fonctions de youtub***********************************************
def youtube():
    titre= title.get()
    pywhatkit.playonyt(titre)

def clear_rechech():
    title.set("")

#********************************************Les Fonctions de whatsapp***********************************************
def send():
    message=fmsg.get()
    hours=int(lhrs.get())
    minutes=int(lmins.get())
    mobiles=mobile.get()
    pywhatkit.sendwhatmsg(mobiles,message,hours,minutes)
    
def clear():
    fmsg.set("")
    lhrs.set("")
    lmins.set("")
    mobile.set("")

def quitter():
    quitter= tkinter.messagebox.askyesno("whatsapp Auto","Etez-vous de vouloir quitter?")
    if quitter > 0:
        root.destroy()
        return

def formulaire():
    root.geometry("900x500+0+0")
    root.resizable(width=False, height=False)



def Whatsapp():
    root.geometry("400x500+0+0")
    root.resizable(width=False, height=False)
#******************************************Debut du programme***********************************
root=Tk()
root.config(background='#E3E1F0')
#root.title("MON APLLICATION")
root.geometry("400x500+0+0")
root.resizable(width=False, height=False)

#****************************Whatsapp declaration de type***************************************
fmsg=StringVar()
lhrs=StringVar()
lmins=StringVar()
mobile=StringVar()

#****************************youtube declaration de type****************************************
title=StringVar()

#****************************Declaration des menus**********************************************
whatsapp= Frame(root)
whatsapp.grid()

barmenu= Menu(whatsapp)
menu1 = Menu(barmenu, tearoff=0)
barmenu.add_cascade(label="Recherche",menu=menu1)
menu1.add_command(label="Whatsapp", command=Whatsapp)
menu1.add_command(label="Formulaire", command=formulaire)

menu2 = Menu(barmenu, tearoff=0)
barmenu.add_cascade(label="Formulaire",menu=menu2)
menu2.add_command(label="recherche youtube")
menu2.add_command(label="recherche google")

menu3 = Menu(barmenu, tearoff=0)
barmenu.add_cascade(label="Apropos",menu=menu3)
menu3.add_command(label="recherche youtube")
menu3.add_command(label="recherche google")

menu4 = Menu(barmenu, tearoff=0)
barmenu.add_cascade(label="Aide",menu=menu4)
menu4.add_command(label="recherche youtube")
menu4.add_command(label="recherche google")

menu5 = Menu(barmenu, tearoff=0)
barmenu.add_cascade(label="Quitter l'application",menu=menu5)
menu5.add_command(label="Quitter", command=quitter)

root.config(menu=barmenu)

#titre generale whatsapp Auto
lbltitre =Label(root,bd = 20, relief = RIDGE, text = "whatsapp Auto ", font = ("Arial", 30,'bold'), bg = "#00DB00", fg="white")
lbltitre.place(x = 0, y = 0, width = 400)

numero= Label(root, text="Numéro", font = ("Arial", 14) ,bg='#00DB00', fg="white")
numero_saisi= Entry(root, textvariable=mobile, bd=4, font=("Arial", 13))
numero_saisi.place(x=100, y=150, width=260)
numero.place(x=10, y=150)

message= Label(root, text="Message", font = ("Arial", 14) ,bg='#00DB00', fg="white")
message_saisi= Entry(root, textvariable=fmsg, bd=4, font=("Arial", 13))
message_saisi.place(x=100, y=200, width=260)
message.place(x=10, y=200)

heure= Label(root, text="Heure", font = ("Arial", 14) ,bg='#00DB00', fg="white")
heure_saisi= Entry(root, textvariable= lhrs, bd=4, font=("Arial", 13))
heure_saisi.place(x=100, y=250, width=60)
heure.place(x=10, y=250)

minutes= Label(root, text="Minutes", font = ("Arial", 14) ,bg='#00DB00', fg="white")
minutes_saisi= Entry(root, textvariable=lmins, bd=4, font=("Arial", 13))
minutes_saisi.place(x=100, y=300, width=60)
minutes.place(x=10, y=300)

bouton_Envoyer = Button(root, text = "Envoyer", font = ("Arial", 16),bg = "darkblue", fg = "yellow", command=send)
bouton_Envoyer.place(x=25, y= 390, width=130)

bouton_supprimer = Button(root, text = "Supprimer", font = ("Arial", 16),bg = "darkblue", fg = "yellow", command=clear)
bouton_supprimer.place(x=250, y= 390, width=130)

#Titre Téléchargement Youtub
lbltitre =Label(root,bd = 20, relief = RIDGE, text = "Téléchargement Youtub", font = ("Arial", 30,'bold'), bg = "#FA1408", fg="white")
lbltitre.place(x = 420, y = 0, width = 480)

def select_path():
    path = filedialog.askdirectory()
    path_label.config(text=path)

def download_file():
    get_link = link_feild.get()

    user_path = path_label.cget("text")
    root.title("Téléchargement de......")

    mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    shutil.move(mp4_video, user_path)
    root.title("Téléchargement terminé ! Télécharger un autre fichier....")
#declaration de canvas
canvas = Canvas(root,width=500, height=500)
canvas.place()

logo_image = PhotoImage(file="yt.png")
logo_image = logo_image.subsample(2,2)

canvas.create_image(250, 80, image=logo_image)

#****************************Recherche youtube**********************************************
titre_saisi= Entry(root, textvariable=title, bd=4, font=("Arial", 13))
titre_chanson= Label(root, text="Entrer le titre", font = ("Arial", 14) ,bg='#E3E1F0')
recherche_btn = Button(root, text="recherchez", command=youtube,font = ("Arial", 16),bg = "#FA1408", fg = "yellow")
supprimer_btn = Button(root, text="supprimer", command=clear_rechech,font = ("Arial", 16),bg = "#FA1408", fg = "yellow")

titre_saisi.place(x=480, y=150,width=260)
titre_chanson.place(x=760, y=150,)
recherche_btn.place(x=450, y=100, width=150)
supprimer_btn.place(x=650, y=100, width=150)

#****************************mettre le lien**********************************************
link_feild = Entry(root, bd=4, font=("Arial", 13) )
link_label = Label(root, text="Entrer le lien",background="#E3E1F0", font=('Roboto', 15))
link_feild.place(x=480, y=200, width=260)
link_label.place(x=760, y=200)
link_feild.get()
link_label=StringVar()

path_label = Label(root, text="Sélectionnez le chemin de téléchargement",background="#E3E1F0", font=('roboto', 15))
select_btn = Button(root, text="Sélectionnez", command=select_path,font = ("Arial", 16),bg = "#FA1408", fg = "yellow")
path_label.place(x=440, y=250)
select_btn.place(x=530, y=300, width=150)

dwnd = PhotoImage(file="R.png")
download_btn = Button(root, image=dwnd, borderwidth=0,background='#E3E1F0', command=download_file , text="Téléchargement", font=('roboto',15))
download_btn.place(x=410, y=350)


root.mainloop()