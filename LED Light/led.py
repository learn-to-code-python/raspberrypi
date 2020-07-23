import RPi.GPIO as GPIO
import time

ledpin = 17


def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(ledpin, GPIO.OUT)
    GPIO.output(ledpin, GPIO.LOW)
    print(f'Using GPIO {ledpin}')


def main():
    setup()
    while True:
        GPIO.output(ledpin, GPIO.HIGH)
        print('LED ON')
        time.sleep(1)
        GPIO.output(ledpin, GPIO.LOW)
        print('LED OFF')
        time.sleep(1)


def destroy():
    GPIO.cleanup()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:  
        destroy()
