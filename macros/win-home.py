from adafruit_hid.keycode import Keycode  # REQUIRED if using Keycode.* values

app = {  # REQUIRED dict, must be named 'app'
    "name": "HOME",  # Application name
    "macros": [  # List of button macros...
        # COLOR    LABEL    KEY SEQTEAM
        # 1st row ----------
        (0x004000, "< Back", [Keycode.ALT, Keycode.LEFT_ARROW]),
        (0x004000, "Fwd >", [Keycode.ALT, Keycode.RIGHT_ARROW]),
        (0x400000, "Up", [Keycode.SHIFT, " "]),  # Scroll up
        # 2nd row ----------
        (0x202000, "- Size", [Keycode.CONTROL, Keycode.KEYPAD_MINUS]),
        (0x202000, "Size +", [Keycode.CONTROL, Keycode.KEYPAD_PLUS]),
        (0x400000, "Down", " "),  # Scroll down
        # 3rd row ----------
        (0x101010, "Taskmgr", [Keycode.CONTROL, Keycode.SHIFT, Keycode.ESCAPE]),
        (0x991000, "Brave", [Keycode.WINDOWS, "3"]),  # For opening personal programs they must be pinned to taskbar.
        # The bind number is tied to the order on the task bar (1 indexed)
        (0x000040, "Steam", [Keycode.WINDOWS, "1"]),
        # 4th row ----------
        (0x202000, "Copy", [Keycode.CONTROL, "c"]),
        (0x202000, "Paste", [Keycode.CONTROL, "v"]),
        (0x101010, "FileEx", [Keycode.WINDOWS, "2"]),  # Hack-a-Day in new win
        # Encoder button ---
        (0x000000, "", [Keycode.CONTROL, "w"]),  # Close tab
    ],
}
# Write your code here :-)
