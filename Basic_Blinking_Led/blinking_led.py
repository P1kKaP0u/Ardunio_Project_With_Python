import pyfirmata
import time

port = "COM4" # port number
board = pyfirmata.Arduino(port)
pin_green = 8 # green led pin
pin_red = 10 # red led pin


while True:

    board.digital[pin_green].write(1)
    board.digital[pin_red].write(1)

    time.sleep(0.5) # delay for 5 second

    board.digital[pin_green].write(0)
    board.digital[pin_red].write(0)

    time.sleep(0.5) # delay for 5 second

board.exit()

