<<<<<<< HEAD
import time
import datetime


from board import SCL, SDA
import busio

from adafruit_seesaw.seesaw import Seesaw


i_mean_max = 900

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)
touch = 0

if i_mean_max > 60:
    print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " Mesure started (average on "
          + str(    '{:.0f}'.format(i_mean_max / 60)) + " minute(s))")
else:
    print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " Mesure started (average on "
          + str(    '{:.0f}'.format(i_mean_max)) + " secondes)")

while True:

    i_mean = 0
    touch = 0
    temp = 0

    while i_mean < i_mean_max:
        i_mean += 1

        # read moisture level through capacitive touch pad
        touch += ss.moisture_read()

        # read temperature from the temperature sensor
        temp += ss.get_temp()
        time.sleep(1)

    print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " temp: " + str(
        '{:+.2f}'.format(temp / i_mean_max)) + "  moisture: " + str('{:+.0f}'.format(touch / i_mean_max)))

=======
import time
import datetime


from board import SCL, SDA
import busio

from adafruit_seesaw.seesaw import Seesaw


i_mean_max = 900

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)
touch = 0

if i_mean_max > 60:
    print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " Mesure started (average on "
          + str(    '{:.0f}'.format(i_mean_max / 60)) + " minute(s))")
else:
    print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " Mesure started (average on "
          + str(    '{:.0f}'.format(i_mean_max)) + " secondes)")

while True:

    i_mean = 0
    touch = 0
    temp = 0

    while i_mean < i_mean_max:
        i_mean += 1

        # read moisture level through capacitive touch pad
        touch += ss.moisture_read()

        # read temperature from the temperature sensor
        temp += ss.get_temp()
        time.sleep(1)

    print(str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " temp: " + str(
        '{:+.2f}'.format(temp / i_mean_max)) + "  moisture: " + str('{:+.0f}'.format(touch / i_mean_max)))

>>>>>>> 872d55debed5e8172dd3cf19d1d42c08d7623370
