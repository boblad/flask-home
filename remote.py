from flask import Flask
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)

p = GPIO.PWM(12, 50)
p2 = GPIO.PWM(16, 50)

p.start(7.5)
p2.start(7.5)

app = Flask(__name__)

@app.route("/")
def hello():
    p2.ChangeDutyCycle(2.5)
    p.ChangeDutyCycle(12.5)
    time.sleep(0.5)
    p2.ChangeDutyCycle(7.5)
    p.ChangeDutyCycle(7.5)
    return "Success!"

if __name__ == "__main__":
    app.run()
