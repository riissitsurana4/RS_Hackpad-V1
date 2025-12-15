import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

keyboard = KMKKeyboard()

keyboard.col_pins = (
    board.GPIO28,  # COL1
    board.GPIO29,  # COL2
    board.GPIO0,  # COL3
    board.GPIO1,  # COL4
)

keyboard.row_pins = (
    board.GPIO26,  # ROW1
    board.GPIO27,  # ROW2
)

keyboard.diode_orientation = DiodeOrientation.COL2ROW


keyboard.keymap = [
    [
        KC.Q, KC.W, KC.E, KC.R,
        KC.A, KC.S, KC.D, KC.F,
    ]
]


if __name__ == "__main__":
    keyboard.go()