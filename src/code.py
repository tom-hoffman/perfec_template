# SPDX-FileCopyrightText: 2025 Tom Hoffman & E-Cubed students
# SPDX-License-Identifier: MIT

# Modular Playground Application Template

# Module Description:
# 

import gc
import config

from midi_controller import Starting 
print("After midi controller: " + str(gc.mem_free()))

from model import ApplicationModel
print("After model: " + str(gc.mem_free()))

from board_controller import ActiveView

import usb_midi

from micropython import const

_CLOCK = const(b'\xF8')

# These "ports" are not to be confused with MIDI channels, etc.
_OUTIE = usb_midi.ports[1]

def send_clock(self):
    _OUTIE.write(_CLOCK)

tm = ApplicationModel()

bc = ActiveView(tm).update_mode()
bc.update_pixels()
print("After object creation: " + str(gc.mem_free()))
while True:
    pass
