#!/usr/bin/env python

from effectlayer import EffectLayer

class Lightning(EffectLayer):
    '''
    An effect layer to add more responsive interactivity.  Simulate a lightning
    bolt fired from the lower to upper dodecahedron, flowing across the axon
    bridge.  Intended to be listed as the last layer in a playlist entry.  When
    a button is pressed and the lightning bolt is firing, the entire frame will
    be overwritten.  When not firing, the frame is passed through unchanged.

                                    -- mct, Wed Oct 28 16:48:53 PDT 2015
    '''

    # Number of LEDs in each section
    num_lower = 20
    num_axon  = 27
    num_upper = 50

    lower_offset = 0
    axon_offset  = 20
    upper_offset = 20+27

    r1, g1, b1 = (0, 0, 255)
    r2, g2, b2 = (255, 0, 0)

    # The formatting of the 'sequence' array below is pretty wonky, but it lets
    # us rapidly prototype patterns using ASCII.  The first element is the RGB
    # color for the lower dodeca, the second is an 27-byte long ASCII string
    # where each character represents one LED in the axon, and the last is the
    # RGB color for the upper dodeca.

    sequence = (
        # Starting on lower dodeca
        #[( r1 * 0.5,  g1 * 0.5,  b1 * 0.5 ), '___________________________', ( r2 * 0.0,  g2 * 0.0,  b2 * 0.0 )],
        #[( r1 * 0.6,  g1 * 0.6,  b1 * 0.6 ), '___________________________', ( r2 * 0.0,  g2 * 0.0,  b2 * 0.0 )],
        #[( r1 * 0.7,  g1 * 0.7,  b1 * 0.7 ), '___________________________', ( r2 * 0.0,  g2 * 0.0,  b2 * 0.0 )],
        #[( r1 * 0.8,  g1 * 0.8,  b1 * 0.8 ), '___________________________', ( r2 * 0.0,  g2 * 0.0,  b2 * 0.0 )],
        #[( r1 * 0.9,  g1 * 0.9,  b1 * 0.9 ), '___________________________', ( r2 * 0.0,  g2 * 0.0,  b2 * 0.0 )],
        #[( r1 * 0.9,  g1 * 0.9,  b1 * 0.9 ), '___________________________', ( r2 * 0.0,  g2 * 0.0,  b2 * 0.0 )],
        #[( r1 * 1.0,  g1 * 1.0,  b1 * 1.0 ), '___________________________', ( r2 * 0.0,  g2 * 0.0,  b2 * 0.0 )],
        #[( r1 * 1.0,  g1 * 1.0,  b1 * 1.0 ), '___________________________', ( r2 * 0.0,  g2 * 0.0,  b2 * 0.0 )],

        # Lightning flash across axon
        [( r1 * 1.0,  g1 * 1.0,  b1 * 1.0 ), '@@@@@______________________', (r2 * 0.0,  g2 * 0.0,   b2 * 0.0, )],
        [( r1 * 0.9,  g1 * 0.9,  b1 * 0.9 ), '225@@@@@@__________________', (r2 * 0.0,  g2 * 0.0,   b2 * 0.0, )],
        [( r1 * 0.7,  g1 * 0.7,  b1 * 0.7 ), '____225@@@@@@______________', (r2 * 0.0,  g2 * 0.0,   b2 * 0.0, )],
        [( r1 * 0.5,  g1 * 0.0,  b1 * 0.0 ), '________225@@@@@@__________', (r2 * 0.0,  g2 * 0.0,   b2 * 0.0, )],
        [( r1 * 0.3,  g1 * 0.0,  b1 * 0.0 ), '____________225@@@@@@______', (r2 * 0.0,  g2 * 0.0,   b2 * 0.0, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '________________225@@@@@@__', (r2 * 0.0,  g2 * 0.0,   b2 * 0.0, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '___________________225@@@@@', (r2 * 0.0,  g2 * 0.0,   b2 * 0.0, )],

        # Hitting upper dodeca
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '_____________________225@@@', (r2 * 1.0,  g2 * 1.0,   b2 * 1.0, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '______________________225@@', (r2 * 1.0,  g2 * 1.0,   b2 * 1.0, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '_______________________225@', (r2 * 1.0,  g2 * 1.0,   b2 * 1.0, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '________________________225', (r2 * 1.0,  g2 * 1.0,   b2 * 1.0, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '_________________________22', (r2 * 1.0,  g2 * 1.0,   b2 * 1.0, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '__________________________1', (r2 * 1.0,  g2 * 1.0,   b2 * 1.0, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '___________________________', (r2 * 1.0,  g2 * 1.0,   b2 * 1.0, )],

        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '___________________________', (r2 * 1.0,  g2 * 1.0,   b2 * 1.0, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '___________________________', (r2 * 0.9,  g2 * 0.9,   b2 * 0.9, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '___________________________', (r2 * 0.8,  g2 * 0.8,   b2 * 0.8, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '___________________________', (r2 * 0.7,  g2 * 0.7,   b2 * 0.7, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '___________________________', (r2 * 0.6,  g2 * 0.6,   b2 * 0.6, )],

        # Blanking afterwards
        #[( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '___________________________', (r2 * 0.0,  g2 * 0.0,   b2 * 0.0, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '___________________________', (r2 * 0.0,  g2 * 0.0,   b2 * 0.0, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '___________________________', (r2 * 0.0,  g2 * 0.0,   b2 * 0.0, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '___________________________', (r2 * 0.0,  g2 * 0.0,   b2 * 0.0, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '___________________________', (r2 * 0.0,  g2 * 0.0,   b2 * 0.0, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '___________________________', (r2 * 0.0,  g2 * 0.0,   b2 * 0.0, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '___________________________', (r2 * 0.0,  g2 * 0.0,   b2 * 0.0, )],
        [( r1 * 0.0,  g1 * 0.0,  b1 * 0.0 ), '___________________________', (r2 * 0.0,  g2 * 0.0,   b2 * 0.0, )],
    )

    def __init__(self):
        self.index = 0
        self.armed = False
        self.firing = False

    def render(self, model, params, frame):
        button = True in params.buttonState

        if not self.armed and not button:
            self.armed = True
            print "Lightning: Armed"

        if self.armed and not self.firing and button:
            print "Lightning: Firing"
            self.firing = True
            self.armed = False
            self.index = 0

        if not self.firing:
            return

        lower_color, axon_string, upper_color = self.sequence[self.index]

        for i in range(self.num_lower):
            frame[self.lower_offset + i] = lower_color

        for i in range(self.num_upper):
            frame[self.upper_offset + i] = upper_color

        for i, value in enumerate(axon_string):
            r, g, b = (255, 255, 255)

            if   value in ('@', 'W'): frame[self.axon_offset + i] = (r,     g,     b    )
            elif value in ('1',    ): frame[self.axon_offset + i] = (r*.1,  g*.1,  b*.1 )
            elif value in ('2',    ): frame[self.axon_offset + i] = (r*.2,  g*.2,  b*.2 )
            elif value in ('3',    ): frame[self.axon_offset + i] = (r*.3,  g*.3,  b*.3 )
            elif value in ('4',    ): frame[self.axon_offset + i] = (r*.4,  g*.4,  b*.4 )
            elif value in ('5',    ): frame[self.axon_offset + i] = (r*.5,  g*.5,  b*.5 )
            elif value in ('6',    ): frame[self.axon_offset + i] = (r*.6,  g*.6,  b*.6 )
            elif value in ('7',    ): frame[self.axon_offset + i] = (r*.7,  g*.7,  b*.7 )
            elif value in ('8',    ): frame[self.axon_offset + i] = (r*.8,  g*.8,  b*.8 )
            elif value in ('9',    ): frame[self.axon_offset + i] = (r*.9,  g*.9,  b*.9 )
            elif value in ('R',    ): frame[self.axon_offset + i] = (255,   0,   0)
            elif value in ('G',    ): frame[self.axon_offset + i] = (  0, 255,   0)
            elif value in ('B',    ): frame[self.axon_offset + i] = (  0,   0, 255)
            else:                     frame[self.axon_offset + i] = (  0,   0,   0)

        # The red channel is out on this LED, don't use it.
        frame[18] = (0,0,0)

        # Scale from [0..255] to [0..1]
        for i in range(len(frame)):
            for j in range(len(frame[i])):
                frame[i][j] /= 255.0

        self.index += 1
        if self.index >= len(self.sequence):
            self.firing = False
            print "Lightning: Done firing"
