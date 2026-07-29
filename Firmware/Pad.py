print("Starting")

import board
import busio 

from kmk.kmk_Keyboard import KMKKeyboard
form kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.encoder import EncoderHandler
from kmk.extensions.rgb import RGB


keyboard = KMKKeyboard()
keyboard.col_pins = (board.GP13,board.GP14,board.GP22,board.GP22)
keyboard.row_pins = (board.GP0,board.GP3,board.GP6,board.GP8,board.GP10,board.GP11)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    KC.NO,KC.NO,KC.NO,KC.NO,
    KC.P7,KC.P8,KC.P9,KC.PPLS,
    KC.P4,KC.P5,KC.P6,KC.NO,
    KC.P1,KC.P2,KC.P3,KC.PENT,
    KC.P0,KC.PDOT,KC.NO,KC.NO,

]
encoder_handler = EncoderHandler()
encoder_handler.pins = (
    (board.GP19,board.GP18,None),
    (board.GP17,board.GP16,None)
)

rgb_light = RGB (
    pixe_pin = board.GP20,
    num_pixels = 2,
    sat_default = 100,
    hue_default = 0 ,
    val_deafault = 100,
)
if __name__=='__main__':
    keyboard.go()

    