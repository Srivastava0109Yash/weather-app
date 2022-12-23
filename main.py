from tkinter import *
import tkinter as tk

import pylab as p
from geopy.geocoders import Nominatim
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import *
import requests
import pytz
from PIL import Image,ImageTk


root=Tk()
root.title("Weather App")
root.geometry("900x500+300+200")


root.resizable(False,False)

def getweather():
    try:
        city=textfield.get()

        geolocator=Nominatim(user_agent='geoapiExercises')
        location=geolocator.geocode(city)
        obj=TimezoneFinder()
        result =obj.timezone_at(lng=location.longitude,lat=location.latitude)

        home = pytz.timezone(result)
        local_time = datetime.now(home)
        current_time = local_time.strftime("%I:%M %p")
        clock.config(text=current_time)
        name.config(text="CURRENT WEATHER")

        api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=bc0b2567dc6bf6e44852f9b48959408b"
        json_data = requests.get(api).json()

    # current

        temp = int(json_data['main']['temp'] - 273.15)
        hum = json_data['main']['humidity']
        press = json_data['main']['pressure']
        wind = json_data['wind']['speed']
        desc = json_data['weather'][0]['description']
        condition=json_data['weather'][0]['main']

        t.config(text=(temp,"°"))
        c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
        w.config(text=wind)
        h.config(text=hum)
        d.config(text=desc)
        p.config(text=press)

        

    except Exception as e:
        messagebox.showerror("Weather App","Invalid Entry!!")





#search box:

search_image=PhotoImage(file="C:/Users/Yash/weather app(api)/Rounded Rectangle 3.png",)
myimage=Label(image=search_image)
myimage.place(x=20,y=28)

textfield=tk.Entry(root,justify="center",width=17,font=("poppins",25,"bold"),bg="#203243",border=0,fg="white")
textfield.place(x=50,y=40)
textfield.focus()

Search_icon=PhotoImage(file="C:/Users/Yash/weather app(api)/Layer 6.png")
m1=Button(image=Search_icon,borderwidth=0,cursor="hand2",bg='#203243',command=getweather)
m1.place(x=390,y=32)

#logo

logo=PhotoImage(file="C:/Users/Yash/weather app(api)/logo.png")

Logo=Label(image=logo)
Logo.place(x=150,y=100)

#bottom box
image=Image.open('C:/Users/Yash/weather app(api)/Rounded Rectangle 1.png')
img=image.resize((850, 100))
Frame_image=ImageTk.PhotoImage(img)
Frame=Label(image=Frame_image)
Frame.pack(padx=5,pady=5,side=BOTTOM)

#time
name=Label(root,font=("arial",15,"bold"))
name.place(x=30,y=100)

clock=Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)



#label
label1=Label(root,text="WIND",font=("Helvetica",15,"bold"),fg="white",bg="#203243")
label1.place(x=120,y=400)

label2=Label(root,text="HUMIDITY",font=("Helvetica",15,"bold"),fg="white",bg="#203243")
label2.place(x=250,y=400)

label3=Label(root,text="DESCRIPTION",font=("Helvetica",15,"bold"),fg="white",bg="#203243")
label3.place(x=430,y=400)

label4=Label(root,text="PRESSURE",font=("Helvetica",15,"bold"),fg="white",bg="#203243")
label4.place(x=650,y=400)

t=Label(font=("arial",70,"bold"),fg="#ee666d")
t.place(x=400,y=150)

c=Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w=Label(text="...",font=("arial",15,"bold"),bg="#203243")
w.place(x=120,y=430)

h=Label(text="...",font=("arial",15,"bold"),bg="#203243")
h.place(x=280,y=430)

d=Label(text="...",font=("arial",15,"bold"),bg="#203243")
d.place(x=450,y=430)

p=Label(text="...",font=("arial",15,"bold"),bg="#203243")
p.place(x=670,y=430)








root.mainloop()
