import customtkinter as cs
import tkinter
from tkinter import *
from tkinter import filedialog
import win32clipboard as cb
from pathlib import Path
import os
import pytube

cs.set_appearance_mode("system")
cs.set_default_color_theme('dark-blue')

app = cs.CTk()
app.geometry("600x500")
app.title("Khmer YouTube Downloader - Rean Computer 101")

def PastLink(): #read from clipboard
    cb.OpenClipboard()
    # text_link.configure(textvariable=str(cb.GetClipboardData()))
    text_link.delete(0, 200)
    text_link.insert(1,str(cb.GetClipboardData()))
    cb.CloseClipboard()

#configure font:
font_en = cs.CTkFont(family="Roboto", size=14)
font_kh = cs.CTkFont(family="Khmer OS Muol", size=16)
font_kh_bokor = cs.CTkFont(family="Khmer OS Bokor", size=16)

label_app = cs.CTkLabel(app, text="កម្មវិធីទាញយកយ៉ូធូបវីដេអូ​ ជំនាន់ទី១", font=font_kh)
label_app.place(x=125,y=10)

# # font_e.configure(family="New Font")

URL = StringVar()
x_pos = 15
y_pos = 50

# downloads_path = str(Path.home() / "Downloads")
#read path from file 
f = open("./CustomTKinter/down.txt",'r')
downloads_path = f.readline()
if len(downloads_path)<1: 
    downloads_path = str(Path.home() / "Downloads")
f.close()

def writeToPath(path):
    f = open('./CustomTKinter/down.txt','w')
    f.write(path)
    f.close()

def select_path():
    #allow use to select any folder to store
    global downloads_path 
    downloads_path = filedialog.askdirectory()
    download_label.destroy()
    download_p = Label(app,font=font_en)
    download_p.place(x=x_pos,y=y_pos+80)
    download_p.config(text=downloads_path)

    writeToPath(downloads_path)
     
def OpenDownloadFolder():
    #open specific window explorer window
    path = os.path.realpath(downloads_path)
    os.startfile(path)

def DownloadYouTubeVideoHighQTY():
    link = text_link.get()
    print(link)
    yt = pytube.YouTube(link)
    status_label.config(text="កំពុងទាញយកវីដេអូ សូមរងចាំ")
    yt.streams.get_highest_resolution().download(downloads_path)
    status_label.config(text="អរគុណ ទាញយកបានជោគជ័យ")

text_link = cs.CTkEntry(app,width=440, height=32,corner_radius=15, 
                        font=font_en,placeholder_text_color='silver',placeholder_text="Paste YouTube Link Here")
text_link.place(x=x_pos,y=y_pos)

button = cs.CTkButton(master=app,width=120,height=32,border_width=0,
                        corner_radius=15,text="Paste",command=PastLink)
button.place(x=x_pos + 450,y=y_pos)

label_Path = cs.CTkLabel(app,font=font_kh_bokor,text="ទីតាំងរក្សាទុកវីដេអូ")
label_Path.place(x=x_pos,y=y_pos+40)

change_folder = cs.CTkButton(app,text='Change Folder',font=font_en, command=select_path)
change_folder.place(x=x_pos + 130,y=y_pos+50)

open_downloadFolder = cs.CTkButton(app, text="Open", font=font_en, command=OpenDownloadFolder)
open_downloadFolder.place(x=x_pos + 200,y=y_pos+50)

download_label = Label(app,font=font_en, text=downloads_path)
download_label.place(x=x_pos,y=y_pos+80)

download_button = cs.CTkButton(app, text="ទាញយកវីដេអូ", font=font_kh_bokor,command=DownloadYouTubeVideoHighQTY)
download_button.pack(padx=100,pady=200)

status_label = Label(app,text="សកម្មភាព: ទំនេរ",font=font_kh_bokor)
status_label.pack()


if __name__ == "__main__":
    app.mainloop()

