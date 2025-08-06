import RPi.GPIO as GPIO
import time
import tkinter as tk

l1 = 1
l2 = 1
l3 = 1
lm = 1
GPIO.setmode(GPIO.BCM)
GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(21, GPIO.OUT)


def light_1():
    global l1
    if l1%2 == 1:
        GPIO.output(26, True)
        l1 = 0 
    else:
        GPIO.output(26, False)
        l1 = 1
        
def light_2():
    global l2
    if l2%2 == 1:
        GPIO.output(21, True)
        l2 = 0
    else:
        GPIO.output(21, False)
        l2 = 1
        
def light_3():
    global l3
    if l3%2 == 1:
        GPIO.output(20, True)
        l3 = 0
    else:
        GPIO.output(20, False)
        l3 = 1
def master_switch():
    global lm
    if lm%2 == 1:
        GPIO.output(20, True)
        GPIO.output(26, True)
        GPIO.output(21, True)
        lm = 0
    else:
        GPIO.output(20, False)
        GPIO.output(21, False)
        GPIO.output(26, False)
        lm = 1
top = tk.Tk()
but1 = tk.Button(top, text="Light 1", command=light_1)
but2 = tk.Button(top, text="Light 2", command=light_3)
but3 = tk.Button(top, text="Light 3", command=light_2)
but4 = tk.Button(top, text="Master", command=master_switch)

but1.pack()
but2.pack()
but3.pack()
but4.pack()


try:
    while True:







        top.mainloop()


finally:
    GPIO.cleanup()
