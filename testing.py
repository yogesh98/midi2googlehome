import sys
import mido
from mido import *


if __name__ == "__main__":
    inport = mido.open_input()

    for msg in inport:
        print(msg)