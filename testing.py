import sys

import pygame
import pygame.midi
from pygame.locals import *

def _print_device_info():
    for i in range( pygame.midi.get_count() ):
        r = pygame.midi.get_device_info(i)
        (interf, name, input, output, opened) = r

        in_out = ""
        if input:
            in_out = "(input)"
        if output:
            in_out = "(output)"

        print ("%2i: interface :%s:, name :%s:, opened :%s:  %s" %
               (i, interf, name, opened, in_out))

if __name__ == "__main__":
    pygame.init()
    pygame.fastevent.init()
    event_get = pygame.fastevent.get
    event_post = pygame.fastevent.post

    pygame.midi.init()

    _print_device_info()

    try:
        device_id = int( sys.argv[-1] )
    except:
        device_id = None

    if device_id is None:
        input_id = pygame.midi.get_default_input_id()
    else:
        input_id = device_id

    print ("using input_id :%s:" % input_id)

    pygame.display.set_mode((1,1))



    going = True
    while going:
        events = event_get()
        for e in events:
            if e.type in [QUIT]:
                going = False
            if e.type in [KEYDOWN]:
                going = False
            if e.type in [pygame.midi.MIDIIN]:
                print (e)

        if i.poll():
            midi_events = i.read(10)
            # convert them into pygame events.
            midi_evs = pygame.midi.midis2events(midi_events, i.device_id)

            for m_e in midi_evs:
                event_post( m_e )

    del i
    pygame.midi.quit()

    # pygame.init()
    #
    # pygame.midi.init()
    # input_id = pygame.midi.get_default_input_id()
    # i = pygame.midi.Input(input_id)
    #
    # screen = pygame.display.set_mode((400, 300))
    #
    # print("Starting")
    #
    # try:
    #     running = True
    #
    #     while running:
    #
    #         if i.poll():
    #             print(i.poll)
    # except(KeyboardInterrupt, SystemExit):
    #     pygame.midi.quit()
    #     pygame.quit()