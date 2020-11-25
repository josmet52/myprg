#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import RPi.GPIO as GPIO
import math

from lib.time_mesure_lib import Exec_time_mesurment 
  
GPIO.setmode(GPIO.BCM)

pin_cmd = 23
pin_mes = 25

GPIO.setwarnings(False)

GPIO.setup(pin_cmd, GPIO.OUT)                    # broche 12 est une entree numerique
GPIO.setup(pin_mes, GPIO.IN)                   # broche 12 est une sortie numerique

print("mesure started")
GPIO.output(pin_cmd, GPIO.HIGH)

n_moy = 5
v_sleep = 0.01

v_offset = 0.01
v_trigger = 1.48

R1 = 100E3
C1 = 10E-6
T = R1 * C1

while True:
    i = 1
    t_avg = 0
    u_avg = 0
    while i <= n_moy:
        
        time.sleep(v_sleep) # pour décharger le condo
        GPIO.output(pin_cmd, GPIO.LOW)
        
        with Exec_time_mesurment() as etm:  
            while GPIO.input(pin_mes) == GPIO.LOW:
                pass
        t_elapsed = etm.interval  
        
        GPIO.output(pin_cmd, GPIO.HIGH)
        
        t_avg += t_elapsed
        u_avg += v_offset + ((v_trigger - v_offset) / (1 - math.exp(-round(t_elapsed/T,4)))) 
        i += 1
        
    t_avg = round(t_avg / n_moy, 4)
    u_avg = round(u_avg / n_moy, 1)
    
    str_2_print = "t mes = " + '{:.1f}'.format(t_avg * 1000) + \
        " u = " + '{:.1f}'.format(u_avg) 
    print(str_2_print)

    