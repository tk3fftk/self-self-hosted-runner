#coding:utf-8

import RPi.GPIO as GPIO
import time

#ピン番号の割り当て方式を「コネクタのピン番号」に設定
GPIO.setmode(GPIO.BOARD)

#使用するピン番号を代入
PIN_LARGE = 16 # GPIO23
PIN_MODE = 18 # GPIO24

PIN_IN1 = 26 # GPIO8
PIN_IN2 = 24 # GPIO7
PIN_IN3 = 8 # GPIO14
PIN_IN4 = 10 # GPIO15

#各ピンを出力ピンに設定
print("setting up GPIO...")

GPIO.setup(PIN_LARGE, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(PIN_MODE, GPIO.OUT, initial = GPIO.LOW)

GPIO.setup(PIN_IN1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(PIN_IN2, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(PIN_IN3, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(PIN_IN4, GPIO.OUT, initial = GPIO.LOW)

print("finished setting up GPIO")

def func_forward():
    GPIO.output(PIN_IN1, GPIO.HIGH)
    GPIO.output(PIN_IN2, GPIO.LOW)
    GPIO.output(PIN_IN3, GPIO.HIGH)
    GPIO.output(PIN_IN4, GPIO.LOW)

def func_back():
    GPIO.output(PIN_IN1, GPIO.LOW)
    GPIO.output(PIN_IN2, GPIO.HIGH)
    GPIO.output(PIN_IN3, GPIO.LOW)
    GPIO.output(PIN_IN4, GPIO.HIGH)

def func_brake():
    GPIO.output(PIN_IN1, GPIO.HIGH)
    GPIO.output(PIN_IN2, GPIO.HIGH)
    GPIO.output(PIN_IN3, GPIO.HIGH)
    GPIO.output(PIN_IN4, GPIO.HIGH)

while True:
    #3秒前進する
    func_forward()
    time.sleep(3.0)
    #3秒ブレーキ
    func_brake()
    time.sleep(3.0)
    #3秒バック
    func_back()
    time.sleep(3.0)
    #3秒ブレーキ
    func_brake()
    time.sleep(3.0)

#GPIOを開放
GPIO.cleanup()

print("End of program")
