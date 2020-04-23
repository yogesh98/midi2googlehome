import sys
import mido
from mido import *
from mido.ports import MultiPort

if __name__ == "__main__":
    print("Trying")
    inports = []
    input_names = mido.get_input_names()
    for name in input_names:
        if "MINI" in name:
            inport = mido.open_input(name)
            break
    for msg in inport:
        print(msg)
