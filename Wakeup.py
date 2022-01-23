from tkinter import *
import datetime
import time
from threading import *
import random
import playsound as ps
from time import strftime
from time import sleep
import threading

# Create Object


# Set geometry

# Use Threading

def setmusic():
    global root
    root = Tk()

    x = '1'
    l1 = Label(root, text="Ringtone set to r" + x, font=("Helvetica 15 bold"))
    global e1
    e1 = Entry(root, text="Ringtone 1", width=100, border=20)
    title=Label(root, text="select te music", font=("Helvetica 15 bold")).pack()
    m = Frame(root)
    m.pack()


    Label(m,  text="Ringtone1", font=("Helvetica 15 ")).grid(row=0,column=0)
    Label(m, text="Ringtone2", font=("Helvetica 15 ")).grid(row=1,column=0)
    Label(m, text="Ringtone3", font=("Helvetica 15 ")).grid(row=2,column=0)
    Label(m, text="Ringtone4", font=("Helvetica 15 ")).grid(row=3,column=0)
    Button(m, text="set", font=("Helvetica 15"), command=setmusic1).grid(row=0,column=1)
    Button(m, text="set", font=("Helvetica 15"), command=setmusic2).grid(row=1,column=1)

    Button(m, text="set", font=("Helvetica 15"), command=setmusic3).grid(row=2,column=1)

    Button(m, text="set", font=("Helvetica 15"), command=setmusic4).grid(row=3,column=1)
    Button(m, text="play", font=("Helvetica 15"), command=playmusic1).grid(row=0,column=2)
    Button(m, text="play", font=("Helvetica 15"), command=playmusic2).grid(row=1,column=2)

    Button(m, text="play", font=("Helvetica 15"), command=playmusic3).grid(row=2,column=2)

    Button(m, text="play", font=("Helvetica 15"), command=playmusic4).grid(row=3,column=2)
    #l1.pack()

       
def setmusic1():
    global ringtone
    ringtone="C:\\Users\\uma36\\Downloads\\alarm.mp3"
    Label(root, text="Ringtone set to r1", font=("Helvetica 15 bold")).pack()
    sleep(5)
    root.destroy()
def setmusic2():
    global ringtone
    ringtone= "C:\\Users\\uma36\\Downloads\\alarm_clock.mp3"
    Label(root, text="Ringtone set to r2", font=("Helvetica 15 bold")).pack()
    sleep(5)
    root.destroy()
def setmusic3():
    global ringtone
    ringtone="C:\\Users\\uma36\\Downloads\\alarm_alarm.mp3"

    Label(root, text="Ringtone set to r3", font=("Helvetica 15 bold")).pack()
    sleep(5)
    root.destroy()
def setmusic4():
    global ringtone
    ringtone="C:\\Users\\uma36\\Downloads\\wake_up.mp3"
    Label(root, text="Ringtone set to r4", font=("Helvetica 15 bold")).pack()
    sleep(5)
    root.destroy()
def playmusic1():
    ps.playsound("C:\\Users\\uma36\\Downloads\\alarm.mp3")
def playmusic2():
    ps.playsound("C:\\Users\\uma36\\Downloads\\alarm_clock.mp3")
def playmusic3():
    ps.playsound("C:\\Users\\uma36\\Downloads\\alarm_alarm.mp3")
def playmusic4():
    ps.playsound("C:\\Users\\uma36\\Downloads\\wake_up.mp3")
    
def Question():
    value=random.randint(1,10)
    if(value==1):
        question="569+23 "
        ans='592'
        o1='500'
        o2='578'
        o3=ans
        o4='595'

    if (value == 2):
        question = "Which country are the Giza Pyramids in?"
        ans = ' Egypt.'
        o1 = 'Uk'
        o2 = 'India'
        o4 = ans
        o3 = 'Italy'

    if (value == 3):
        question = " Which is the longest river on the earth?"
        ans = 'Nile'
        o3 = 'Ganga'
        o2 = 'Krishna'
        o1 = ans
        o4 = 'yammuna'

    if(value==4):
        question = "7+45*78 "


        ans='3517'
        o3 = '500'
        o1 = '4000'
        o2 = ans
        o4 = '5400'

    if (value == 5):
        question = "Who invented Computer "

        ans = ' Charles Babbage'
        o3 = 'marks'
        o1 = 'James Bond'
        o2 = ans
        o4 = 'michel'

    if(value==6):
        question="456+562+369"
        ans='1387'
        o3 = '2387'
        o2 = '1587'
        o1 = ans
        o4 = '5405'

    if(value==7):
        question="145*3"
        ans='435'
        o3 = '450'
        o2 = '425'
        o1 = ans
        o4 = '540'
    if(value==8):
        question="3547*2"
        ans='7094'
        o3 = '7504'
        o1 = '7004'
        o2 = ans
        o4 = '5400'
    if(value==9):
        question="1458+589"
        ans='2047'
        o3 = '2509'
        o2 = '3200'
        o4 = ans
        o1 = '5407'
    if(value==10):
        question="1235+965"
        ans='2200'
        o3 = '2500'
        o2 = '2600'
        o1 = ans
        o4 = '3500'

    return question, ans, o1, o2, o3, o4

class Sound(Thread):
    global answered
    def run(self):
        while True:
            ps.playsound(ringtone)

            if answered:
                break
    def stop(self):
        return False
class Alarm(Thread):
    def run(self):
        hi = Label(myWindow, text="alarm set", font=("Helvetica 15 bold")).pack()
        while True:
            global set_alarm_time
            set_alarm_time=f"{hour.get()}:{minute.get()}:{second.get()}"
            #time.sleep(1)
            current_time=datetime.datetime.now().strftime("%H:%M:%S")

            strtime1=str(set_alarm_time)
            hour1=strtime1[:2]
            minute1=strtime1[3:5]
            #print(minute1)

            strtime2=str(current_time)
            hour2=strtime2[:2]
            minute2=strtime2[3:5]
            #print(minute2)
            currentm=int(minute1)
            global alarmtimem
            global alarmtimeh
            global ringtone

            alarmtimem=int(minute2)
            currenttimeh=int(hour1)
            alarmtimeh=int(hour2)
            if current_time==set_alarm_time:
                print("Time to wake up")


                q.pack(pady=10)


                q1.pack(pady=10)

                oframe.pack()
                Button(oframe, text=o1, font=("Helvetica 15"),command=setans1).pack(pady=20,side=LEFT)
                Button(oframe, text=o2, font=("Helvetica 15"),command=setans2).pack(pady=20,side=LEFT)

                Button(oframe, text=o3, font=("Helvetica 15"),command=setans3).pack(pady=20,side=LEFT)

                Button(oframe, text=o4, font=("Helvetica 15"),command=setans4).pack(pady=20,side=LEFT)

                t.start()
                sleep(2)
                c.start()

class Check(Thread):
    def run(self):
        global answered
        global set_alarm_time
        while(answered==False):
            time = set_alarm_time
            ctime = datetime.datetime.now()-datetime.timedelta(minutes=1)
            ctimes=ctime.strftime("%H:%M:%S")

            print((myanswer, ans))
            if myanswer == ans or time == ctimes:


                answered=True
                t.join()
                oframe.destroy()
                q.destroy()
                q1.destroy()
                a.join()


def time():
    
    str=strftime("%H : %M : %S %p")
    
    lbl.config(text=str)
    
    lbl.after(1000,time)

def setans1():
    global myanswer
    myanswer=o1
    print(myanswer)
def setans2():
    global myanswer
    myanswer=o2
    print(myanswer)
def setans3():
    global myanswer
    myanswer=o3
    print(myanswer)
def setans4():
    global myanswer
    myanswer=o4
    print(myanswer)
answered=False
myanswer=""
question,ans,o1,o2,o3,o4=Question()
t = Sound()
c= Check()
myWindow=Tk()

myWindow.title("Digital Clock")

lbl=Label(myWindow,font=("Algerian",50),background="black",foreground="cyan")
lbl.pack()
Button(myWindow,text="Set Ringtone",font=("Helvetica 15"),command=setmusic).pack(pady=20)
q=Label(myWindow, text="Question", font=("Helvetica 20 bold"), fg="blue")
q1=Label(myWindow, text=question, font=("Helvetica 12 "), fg="blue")
oframe = Frame(myWindow)
#calling time function
time()
Label(myWindow,text="Alarm Clock",font=("Helvetica 20 bold"),fg="blue").pack(pady=10)

Label(myWindow,text="Set Time",font=("Helvetica 15 bold")).pack()
ringtone="C:\\Users\\chand\\Desktop\\ringtone4.mp3"
frame = Frame(myWindow)
frame.pack()

hour = StringVar(myWindow)
hours = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23', '24'
		)
hour.set(hours[0])

hrs = OptionMenu(frame, hour, *hours)
hrs.pack(side=LEFT)

minute = StringVar(myWindow)
minutes = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
minute.set(minutes[0])

mins = OptionMenu(frame, minute, *minutes)
mins.pack(side=LEFT)

second = StringVar(myWindow)
seconds = ('00', '01', '02', '03', '04', '05', '06', '07',
		'08', '09', '10', '11', '12', '13', '14', '15',
		'16', '17', '18', '19', '20', '21', '22', '23',
		'24', '25', '26', '27', '28', '29', '30', '31',
		'32', '33', '34', '35', '36', '37', '38', '39',
		'40', '41', '42', '43', '44', '45', '46', '47',
		'48', '49', '50', '51', '52', '53', '54', '55',
		'56', '57', '58', '59', '60')
second.set(seconds[0])

secs = OptionMenu(frame, second, *seconds)
secs.pack(side=LEFT)
a=Alarm()
Button(myWindow,text="Set Alarm",font=("Helvetica 15"),command=a.start).pack(pady=20)

mainloop()


