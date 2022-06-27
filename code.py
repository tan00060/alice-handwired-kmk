print("Ming Alice Keyboard")
import board

from kmk.extensions.peg_oled_display import Oled, OledDisplayMode, OledReactionType, OledData
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()
keyboard.debug_enabled = True

oled_ext = Oled(
    OledData(
        corner_one={0:OledReactionType.STATIC,1:["layer"]},
        corner_two={0:OledReactionType.LAYER,1:["1","2","3","4"]},
        corner_three={0:OledReactionType.LAYER,1:["base","raise","lower","adjust"]},
        corner_four={0:OledReactionType.LAYER,1:["qwerty","nums","shifted","leds"]}
        ),
        toDisplay=OledDisplayMode.TXT,flip=True)



keyboard.extensions.append(oled_ext)

layers_ext = Layers()
keyboard.modules = [layers_ext]
keyboard.modules.append(Layers())

        
XXXXXXX = KC.NO
_______ = KC.TRNS

LAYER1 = KC.MO(1)
LAYER2 = KC.MO(2)
SPACE_TAP = KC.LT(1, KC.SPACE)



keyboard.SCL=board.GP7
keyboard.SDA=board.GP6
keyboard.col_pins = (board.GP15, board.GP14, board.GP13, board.GP12, board.GP11, board.GP10, board.GP9, board.GP8, board.GP26, board.GP22, board.GP21, board.GP20, board.GP19, board.GP18, board.GP17, board.GP16 )
keyboard.row_pins = (board.GP0, board.GP1, board.GP2 , board.GP3, board.GP4)
keyboard.diode_orientation = DiodeOrientation.ROW2COL

keyboard.keymap = [

    #   COL15       COL14       COL13    COL12    COL11      COL10    COL9     COL8       COL26      COL22      COL21     COL20      COL19       COL18         COL17       COL16                                
    [
        KC.DELETE,  KC.ESCAPE,  KC.N1,   KC.N2,   KC.N3,     KC.N4,   KC.N5,   KC.N6,     KC.N7,     KC.N8,     KC.N9,    KC.N0,     KC.MINUS,   KC.EQUAL,     KC.BSLASH,    KC.GRAVE,
        KC.PGUP,    KC.TAB,     KC.Q,    KC.W,    KC.E,      KC.R,    KC.T,    XXXXXXX,   KC.Y,      KC.U,      KC.I,     KC.O,      KC.P,       KC.LBRACKET,  KC.RBRACKET, KC.BSPC,
        KC.PGDN,    KC.LCTL,    KC.A,    KC.S,    KC.D,      KC.F,    KC.G,    XXXXXXX,   KC.H,      KC.J,      KC.K,     KC.L,      KC.SCOLON,  KC.QUOTE,     XXXXXXX,     KC.ENTER,
        XXXXXXX,    KC.LSFT,    KC.Z,    KC.X,    KC.C,      KC.V,    KC.B,    XXXXXXX,   KC.B,      KC.N,      KC.M,     KC.COMM,   KC.DOT,     KC.SLSH,      KC.RSFT,     LAYER2,
        XXXXXXX,    KC.LGUI,    XXXXXXX, KC.LALT, SPACE_TAP, XXXXXXX, LAYER1,   SPACE_TAP,  XXXXXXX,   XXXXXXX,   XXXXXXX,  KC.RALT,   XXXXXXX,    XXXXXXX,      XXXXXXX,     KC.RCTRL
 
    ],


    #   COL15       COL14     COL13      COL12     COL11      COL10     COL9      COL8       COL26      COL22      COL21          COL20             COL19              COL18     COL17    COL16 
    #   LOWER                               
    [
        _______,    _______,  _______,   _______,  _______,   _______,  _______,  _______,   _______,   _______,   _______,       _______,           _______,          _______,  _______, _______,
        _______,    _______,  _______,   KC.UP,    _______,   _______,  _______,  XXXXXXX,   _______,   _______,   _______,       _______,           _______,          _______,  _______, _______,
        _______,    _______,  KC.LEFT,   KC.DOWN,  KC.RIGHT,  _______,  _______,  XXXXXXX,   _______,   _______,   _______,       _______,           _______,          _______,  XXXXXXX, _______,
        _______,    _______,  _______,   _______,  _______,   _______,  _______,  XXXXXXX,   _______,   _______,   KC.AUDIO_MUTE, KC.AUDIO_VOL_DOWN, KC.AUDIO_VOL_UP,  _______,  _______, _______,
        _______,    _______,  XXXXXXX,   _______,  _______,   XXXXXXX,  _______,  _______,   XXXXXXX,   XXXXXXX,   XXXXXXX,       _______,           _______,          _______,  XXXXXXX, _______

    ],   

    #   COL15       COL14     COL13      COL12     COL11      COL10     COL9      COL8       COL26      COL22      COL21     COL20    COL19    COL18     COL17    COL16      
    #   RAISE                          
    [
        _______,    _______,  _______,   _______,  _______,   _______,  _______,  _______,   _______,   _______,   _______,  _______, _______, _______,  _______, _______,
        _______,    _______,  _______,   _______,  _______,   _______,  _______,  XXXXXXX,   _______,   _______,   _______,  _______, _______, _______,  _______, _______,
        _______,    _______,  _______,   _______,  _______,   _______,  _______,  XXXXXXX,   _______,   _______,   _______,  _______, _______, _______,  XXXXXXX, _______,
        _______,    _______,  _______,   _______,  _______,   _______,  _______,  XXXXXXX,   _______,   _______,   _______,  _______, _______, _______,  _______, _______,
        _______,    _______,  XXXXXXX,   _______,  _______,   XXXXXXX,  _______,  _______,   XXXXXXX,   XXXXXXX,   XXXXXXX,  _______, _______, _______,  XXXXXXX, _______

    ],
]

if __name__ == '__main__':
    keyboard.go()

