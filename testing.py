import sys
import midi
from midi import MidiConnector
if __name__ == "__main__":

    conn = MidiConnector('/dev/serial0')

    while True:
        print(conn.read())
