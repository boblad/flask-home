from flask import Flask
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

application = Flask(__name__)

@application.route("/")
def hello():
    p = GPIO.PWM(12, 50)
    p2 = GPIO.PWM(16, 50)
    p.start(7.5)
    p2.start(7.5)
    time.sleep(0.5)
    p2.ChangeDutyCycle(2.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p2.ChangeDutyCycle(7.5)
    p.ChangeDutyCycle(7.5)
    p = None
    p2 = None
    return "Success!"

@application.errorhandler(500)
def internal_error(error):

    return error

if __name__ == "__main__":
    application.run(host='0.0.0.0', debug=True)
