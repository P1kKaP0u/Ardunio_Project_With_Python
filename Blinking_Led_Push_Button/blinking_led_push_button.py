import pyfirmata
import time
from pyfirmata import util


port = "COM4" # port number
board = pyfirmata.Arduino(port)

it = pyfirmata.util.Iterator(board)
it.start()

pin_redLed = 8 # red LED pin number
pin_button = 10 # button pin number

board.digital[pin_button].mode = pyfirmata.INPUT # pin mode selection. Input or output


while True : 
        sw = board.digital[pin_button].read()
        if sw is True :
                board.digital[pin_redLed].write(1)
        else :
                board.digital[pin_redLed].write(0)
        time.sleep(0.1)

