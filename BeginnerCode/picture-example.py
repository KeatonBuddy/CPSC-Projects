"""
This program is so simple that I don't need the usual DISCLAIMER...

Example of using the Color and Picture data types from the booksite library.
"""

from color import Color
from picture import Picture
import stddraw

turquoise = Color(64, 224, 208)
stddraw.setPenColor(turquoise)
stddraw.setPenRadius(0.025)
stddraw.rectangle(.1, .1, .8, .8)

my_picture = Picture('karel.png')
stddraw.picture(my_picture, 0.5, 0.6)

stddraw.setPenColor(stddraw.BLACK)
stddraw.setFontSize(64)
stddraw.text(0.5, 0.25, 'I live!')
stddraw.show()
