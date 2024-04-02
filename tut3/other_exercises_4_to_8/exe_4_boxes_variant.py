from math import radians

from parapy.core import *
from parapy.geom import *


class Boxes(GeomBase):

    bwidth = Input(1)
    blength = Input(1)
    bheight = Input(1)

    @Part
    def box1(self):
        return Box(width=self.bwidth,
                   length=self.blength,
                   height=self.bheight, color="red")

    @Part
    def box_translated(self):
        return Box(width=self.bwidth,
                   length=self.blength,
                   height=self.bheight,
                   position=(translate(self.position, 'x', 3, 'y', 3)),
                   color="yellow")

    @Part
    def box_translated_and_then_rotated(self):
        return Box(width=self.bwidth,
                   length=self.blength,
                   height=self.bheight,
                   position=rotate(translate(self.position, 'x', 3, 'y', 3),
                                   "x", 60, deg=True),
                   color="yellow")

    @Part
    def box_rotated(self):
        return Box(width=self.bwidth,
                   length=self.blength,
                   height=self.bheight,
                   position=rotate(self.position,
                                   Vector(1, 0, 0),
                                   radians(60)),
                   color="orange")

    @Part
    def box_rotated_and_then_translated(self):
        return Box(width=self.bwidth,
                   length=self.blength,
                   height=self.bheight,
                   position=translate(rotate(self.position,"x",radians(60)),
                                      'x',3,'y', 3),
                   color="orange")



if __name__ == '__main__':
    from parapy.gui import display
    obj = Boxes(bwidth=1.5, blength=1, bheight=0.8)
    display(obj)
