import sys
import mido
from mido import *
from mido.ports import MultiPort

if __name__ == "__main__":
    print("Trying")
    inports = []
    input_names = mido.get_input_names()
    for name in input_names:
    	print(name)
    	inports.append(mido.open_input(name))
    multi = MultiPort(inports)
    for msg in multi:
        print(msg)
