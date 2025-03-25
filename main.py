#coding:utf-8

import RPi.GPIO as GPIO
import time

#ピン番号の割り当て方式を「コネクタのピン番号」に設定
GPIO.setmode(GPIO.BOARD)

#使用するピン番号を代入
PIN_LARGE = 23
PIN_MODE = 24

PIN_IN1 = 7
PIN_IN2 = 8
PIN_IN3 = 14
PIN_IN4 = 15

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

#GPIOを開放
GPIO.cleanup()

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

print("End of program")
