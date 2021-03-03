from guizero import App, PushButton, Slider, TextBox
from gpiozero import AngularServo
import serial
from time import sleep
count = 0

def recordpos(slider1, slider2, pos1, pos2):
    print("Recording servo position")
    pos1.append(slider1.value)
    pos2.append(slider2.value)
    sleep(1)
    
def repeatpos(pos1, pos2):
    print("Repeating")
    i=0
    ser = serial.Serial('/dev/ttyACM0', 9600)
    ser.flush()   
    data = int(pos1.index(i))
    ser.write(str(data).encode('utf-8'))
    print(data)
    ser.flush()
    sleep(.5)
    data2 = int(pos2.index(i))
    ser.write(str(data2).encode('utf-8'))
    print(data2)
    sleep(1)

def work():
    recordpos(slider1, slider2, pos1, pos2)
def repeatit():
    repeatpos(pos1, pos2)

if __name__ == '__main__':
    pos1 = []
    pos1 = [0 for i in range(5)] 
    pos2 = []
    pos2 = [0 for i in range(5)] 
    app = App("W0402711 Lab 9", height = 300, width = 600, layout = "grid")
    slider1 = Slider(app, start = 0, end = 180, width='fill',grid=[2,0])
    slider2 = Slider(app,start=0,end=180,width='fill',grid=[3,0])
    button1 = PushButton(app, text='record', grid=[1,0], command=work)
    button2 = PushButton(app, text = "Run through positions", grid=[1,1], command=repeatit)
    count += 1
    app.display()
    
    
    