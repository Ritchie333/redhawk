#!/usr/bin/python3

from skoolkit import html
from skoolkit.graphics import Frame, Udg
from skoolkit.skoolhtml import HtmlWriter

class RedhawkHtmlWriter(HtmlWriter):

    def print_udg( self, cwd, addr, fName, width, height, attr ):
        udgs = []

        for y in range( 0, height ):

            line = []

            for x in range( 0, width ):
                yoff = y * width * 8
                ptr = addr + yoff + x
                data = []
                for i in range( 0, 8 ):
                    data.append( self.snapshot[ ptr + ( i * width ) ])
                line.append( Udg( attr, data ) )

            udgs.append( line )

        frame = Frame( udgs, 2 )
        return self.handle_image( frame, fName, cwd )