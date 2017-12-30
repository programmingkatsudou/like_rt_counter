import RPi.GPIO as GPIO
import time
import twitter
import os
import sys

key = os.environ["TW_APIKEY"]
sec = os.environ["TW_APISEC"]
acc_token = os.environ["TW_ACCTOKEN"]
sec_token = os.environ["TW_SECTOKEN"]
myscreen_name = sys.argv[1]

GPIO.setmode(GPIO.BOARD)
GPIO.setup(37, GPIO.OUT)
GPIO.output(37, GPIO.LOW)
api = twitter.Api(key, sec, acc_token, sec_token)

try: 
    for line in api.GetUserStream():
        if "event" in line:
            #if line["event"] == "favorite" and line["source"]["screen_name"] != myscreen_name:
            if line["event"] == "favorite":
                print("kitazo")
                GPIO.output(37, GPIO.HIGH)
                time.sleep(3)
                GPIO.output(37, GPIO.LOW)
except KeyboardInterrupt:
    print("cleanup...\n")
finally:
    GPIO.cleanup()
