#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016 ParaPy Holding B.V.
#
# This file is subject to the terms and conditions defined in
# the license agreement that you have received with this source code
#
# THIS CODE AND INFORMATION ARE PROVIDED "AS IS" WITHOUT WARRANTY OF ANY
# KIND, EITHER EXPRESSED OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND/OR FITNESS FOR A PARTICULAR
# PURPOSE.


from parapy.core import *
from parapy.geom import *


class Boxes(GeomBase):

    bwidth = Input(1)
    blength = Input(1)
    bheight = Input(1)

    @Part
    def red_box(self):
        return Box(width=self.bwidth,
                   length=self.blength,
                   height=self.bheight,
                   color="red")

    @Part
    def yellow_box(self):
        return Box(width=self.bwidth,
                   length=self.blength,
                   height=self.bheight,
                   position=rotate(translate(self.position, 'x', 3, 'y', 3),  # translate first, then rotate
                                   'x', 10, deg=True),
                   color="yellow")

    @Part
    def blue_box(self):
        return Box(width=self.bwidth,
                   length=self.blength,
                   height=self.bheight,
                   position=translate(rotate(self.position, 'x', 60, deg=True),  # rotate first, then translate
                                      'x', 3, 'y', 3),
                   color="blue")


if __name__ == '__main__':
    from parapy.gui import display
    obj = Boxes(bwidth=1.5, blength=1, bheight=0.8)
    display(obj)
