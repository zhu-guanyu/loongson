from loongpio import LED
from loongpio import Button
from loongpio import TonalBuzzer
from loongpio import DistanceSensor#HC-SR04通过超声波来测量与最近的障碍物的距离。
from time import sleep

led0 = LED(GPIO1)
led1 = LED(GPIO2)
btn0 = Button(GPIO3)
btn1 = Button(GPIO4)
notes = ['C', 'D', 'E', 'F', 'G']
buzzer = TonerBuzzer(PWM0)

led0=0
led1=0

while True:
    sensor = DistanceSensor(trigger=3, echo=4)
    if sensor.distance >= 1
        if  btno == o and btn1 == o
            led0 =1
            led1=1
        elif  btno == 1 and btn1 == o
            led0 =0
            led1=1
        elif  btno == 0 and btn1 == 1
            led0 =1
            led1=0
        else 
            led0 =0
            led1=0
    else#若距离障碍物太近，则停止不动，并且发出警告
        led0 =0
        led1=0
        for note in notes:
        buzzer.play(note)
        sleep(1)
