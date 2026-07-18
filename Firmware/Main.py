print("starting")

import board 
import busio
from kmk.kmk_keyboard import KMKKeynboard
from kmk.keys import KC
from kmk.scanners import DioderOrientation
from kmk.modules.layers import Layers
from kmk.modules.modtap import ModTap
from kmk.extensions.display import Display, TextEntry, ImageEntry
from kmk.extensions.display.ssd1306 import SSD1306
from kmk.modules.split import Split , SplitSide
from kmk.hid import HIDModes


keyboard = KMKKeynboard()
keyboard.col_pins(board.GP8,board.GP21,board.GP20,board.GP19,board.GP15,board.GP14)
keyboard.row_pins(board.GP1,board.GP2,board.GP4,board.GP6)
keyboard.diode_orientation = DioderOrientation.COL2ROW
keyboard.modules.append(Layers())
keyboard.modules.append(ModTap())
_main, f_st,S_cd,l_st = 0,1,2,3

Clt_ESCE = KC.MT(KC.ESC.KC.LCTL)
ent_super = KC.MT(KC.ENTER, KC.LGUI)
tab_lower = KC.LT(f_st,KC.TAB)

i2c_bus  =  busio.I2C(board.GP,board.GP)
display_driver = SSD1306( i2c = i2c_bus, device_address = 0x3c),
display = Display(
    display = display_driver,
    entries = 
        [
        TextEntry(text='@Youssef', x = 128,y=0,x_anchor = 'R',y_anchor = 'T'),
        ImageEntry(image = "D:\Splitly\Splitly\Firmware\vert_cat.bmp",x=0,y=0),
        ],
        height = 64,
        of_time = 1200,
        brightness = 0.5,
        brightness_step = 0.2,
        dim_time  = 500,
        dim_target = 0.1,
)
keyboard.extensions.append(display)
split = Split (
    split_side = Split.LEFT,
    uart_flip = True,
)
keyboard.modules.append_split(split)
keyboard.keymap = [
    # _main
    [
        KC.TAB,KC.Q,KC.W,KC.E,KC.R,KC.T,
        KC.ALT,KC.A,KC.S,KC.D,KC.F,KC.G,
        KC.LSFT,KC.Z,KC.X,KC.C,KC.V,KC.B,
        KC.NO,KC.NO,KC.NO,Clt_ESCE,ent_super,tab_lower,
    ]
    ,
    # f_st
    [
        KC.TRNS,KC.EXLM,KC.AT,KC.HASH,KC.DLR,KC.PERC,
        KC.TRNS,KC.N1,KC.N2,KC.N3,KC.N4,KC.N5,
        KC.TRNS,KC.TRNS,KC.TILD,KC.TRNS,KC.TRNS,KC.LCBR,
        KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,
    ]
    ,
    # S_cd
    [
        KC.TRNS,KC.DEL,KC.TRNS.KC.UNDS,KC.PLUS,KC.PGUP,
        KC.TRNS,KC.HOME,KC.END,KC.EQL,KC.TRNS,KC.PGDN,
        KC.TRNS,KC.TRNS,KC.TRNS,KC.LCTL(KC.C),KC.LCTL(KC.V),KC.TRNS,
        KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,
    ]
    , # l_st
    [
       KC.TRNS,KC.F1,KC.F2,KC.F3,KC.F4,KC.F5,
       KC.TRNS,KC.F11,KC.F12,KC.TRNS,KC.TRNS,KC.TRNS,
       KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,
       KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,KC.TRNS,
       ]
]

if __name__ == '__main__' :
    keyboard.go()