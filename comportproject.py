from tkinter import*
import serial
from time import process_time, sleep

from serial.serialutil import STOPBITS_ONE


master= Tk()
master.title("Comport GUI")
canvas = Canvas(master,height =800,width=1500,bg="lightgray")
canvas.pack()
textvar=StringVar()
comtext1=StringVar()
def exitfunc():
   
    master.quit()
    master.update()
    
def cleardata():
    
    comtext1.set("")
    textvar.set("")
    master.update()

    
def senddata():
   
    
    ser= serial.Serial(port='COM1',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=0.2)
    ser2= serial.Serial(port='COM2',baudrate=9600,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE,bytesize=serial.EIGHTBITS,timeout=0)
      
    while comtext1!="":
        text=comtext1.get()
        textvar.set(text)
       
        
        if(text!=""):
           
            
            ser.write(text.encode())
            
            sleep(0.2)
            data=ser2.readline()
            print(data)
            print(data.decode())
            
            master.update()
        else:
            if(ser.open() and ser2.open() ==True):
                ser.close()
                ser2.close()
                break
            
            
            
    
        
        
        
   
       









#labels
Com1Label=Label(master,bg="lightgray",text="COM1:Message Data",font="Verdana 12 bold")
Com1Label.place(x=500,y=300,height=30,width=250)
Com2Label=Label(master,bg="lightgray",text="COM2:Received Message",font="Verdana 12 bold")
Com2Label.place(x=900,y=300,height=30,width=250)
#TextBox 

Com1Text =Entry(master,width=20,textvariable=comtext1,font="Verdana 12")
Com1Text.place(x=500,y=350,height=30,width=250)
Com2TextLabel =Label(master,width=20,textvariable=textvar,font="Verdana 12",fg="black")
Com2TextLabel.place(x=900,y=350,height=30,width=250)
#buttons

exit  = Button(master,width=20,text = "Exit",command=exitfunc,font="Verdana 12",bg="white",fg="red")
clear =Button(master,width=20,text = "Clear",command=cleardata,font="Verdana 12",bg="white")
start = Button(master,width=20,text = "Start",command=senddata,font="Verdana 12",bg="white")

exit.place(x=1000,y=600,height=80,width=150)
clear.place(x=160,y=350,height=30,width=110)
start.place(x=160,y=500,height=30,width=110)
   






master.mainloop()






