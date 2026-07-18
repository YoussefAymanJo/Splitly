print('Starting')

# Libraries import
import board
import busio
from kmk.kmk keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import layers
from kb import data_pin
from kmk.modules.modtap import ModTap
from kmk.modules.split import Split, SplitSide
from kmk.hid import HIDMODES

#define new keyboard
keyboard = KMKKeyboard()
layers_module = Layers()
keyboard.modules.apend(layers_module)
keyboard.col_pins =(board.GP8,board.GP21,board.GP19,board.GP15,board.GP16,board.GP26)
keyboard.row_pins = (board.GP1,board.GP2,board.GP4,board.GP6)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layerd())
keyboard.modules.append(ModTap())

_main,f_st,s_cd,l_st = 0,1,2,3
bksp_raise = KC.LT(s_cd,KC.BSPC)
spc_nav = KC.SPACE
rsft_oneshot = KC.OSM(KC.LSDT)
# keys definition
keyboard.keymap = [
    [
     KC.Y,KC.UKC.I,KC.O,KC.P,KC.DEL,
     KC.H,KC.J,KC.K,KC.L,KC.SCLN,KC.QUOT,
     KC.N,KC.M,KC.COMM,KC.DOT,KC.SLSH,KC.RALT,
     bksp_raise,spc_nav,rsft_oneshot,KC.NO,KC.NO,KC.NO,   
    ],
    [
       KC.CIRC,KC.AMPR,KC.ASTR,KC.TRNS,KC.TRNS,KC.TRNS,
       KC.N6,KC.N7,KC.N8,KC.N9,KC.N10,KC.TRNS,
       KC.TRNS,KC.TRNS,KC.TRNS,KC.RCBR,KC.TRNS,KC.TRNS,
       KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS, 
    ],
    [
        KC.TRNS,KC.TRNS,KC.UP,KC.TRNS,KC.TRNS,KC.TRNS,
        KC.LEFT,KC.DOWN,LC.RIGHT,KC.TRNS,KC.TRNS,KC.TRNS,
        KC.MPRV,KC.TRNS,KC.TRND,KC.TRNS,KC.TRNS,KC.TRNS,
        KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,
    ],
    [
       KC.F6,KC.F7,KC.F8,KC.F9,KC.10,KC.TRNS,
       KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,
       KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,
       KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS, 
    ]
]
split = Split(split_type =SplitType.BLE,split_Side = SplitSide.Right , split_target_left=True)

if __name__ == '__main__' :
    keyboard.go(hid_type = HIDMODES.BLE, ble_name='Right Corne Keyboard')