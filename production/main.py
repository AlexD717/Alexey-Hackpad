# You import all the IOs of your board
import board

# These are imports from the kmk library
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.keys import KC
from kmk.modules.macros import Macros
from kmk.modules.encoder import EncoderHandler

# This is the main instance of your keyboard
keyboard = KMKKeyboard()

# Add the macro extension
macros = Macros()
keyboard.modules.append(macros)

# Add the encoder handler module
encoder_handler = EncoderHandler()
keyboard.modules.append(encoder_handler)
keyboard.encoder_pins = ((board.GP1, board.GP2),)  # Define your encoder pins here
encoder_handler.map = [
    ((KC.VOLD, KC.VOLU),),
]

# Define your pins here!
keyboard.col_pins = (board.GP26, board.GP27, board.GP28, board.GP29)
keyboard.row_pins = (board.GP6, board.GP7)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.modules.append(Layers())

LAYER_TOGGLE = KC.TG(1)

# Here you define the buttons corresponding to the pins
# Look here for keycodes: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/keycodes.md
# And here for macros: https://github.com/KMKfw/kmk_firmware/blob/main/docs/en/macros.md
keyboard.keymap = [
    # Layer 0
    [
        KC.MACRO("Hello, friend!\n"),
        KC.MACRO("email@example.com\n"),
        KC.MACRO("Have a great day!\n"),
        LAYER_TOGGLE,

        KC.MACRO([KC.LGUI(KC.E)]),
        KC.MACRO([
            KC.LCTRL(KC.LSHIFT(KC.ESC))
        ]),
        KC.MACRO([
            KC.LGUI(KC.R),
            KC.DELAY(300),
            *[KC(c) for c in "calc"],
            KC.ENTER
        ]),
        KC.PLAY_PAUSE,
    ],

    # Layer 1: Alternative shortcuts/macros
    [
        KC.MACRO("Layer 1 macro A\n"),
        KC.MACRO("Layer 1 macro B\n"),
        KC.MACRO("Layer 1 macro C\n"),
        LAYER_TOGGLE,

        KC.MACRO([KC.LCTRL(KC.C)]),
        KC.MACRO([KC.LCTRL(KC.V)]),
        KC.MACRO([KC.LALT(KC.F4)]),
        KC.PLAY_PAUSE,
    ]
]


# Start kmk!
if __name__ == '__main__':
    keyboard.go()