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


class Aircraft(GeomBase):
    x_wing = Input(10)
    y_wing = Input(1)

    @Part
    def right_wing(self):
        return Wing(position=translate(self.position,
                                       'x', self.x_wing,
                                       'y', self.y_wing))


class Wing(GeomBase):
    span = Input(5)

    @Part
    def root_airfoil(self):
        return Airfoil()

    @Part
    def tip_airfoil(self):
        return Airfoil(position=translate(self.position,
                                          'y', self.span))


class Airfoil(GeomBase):
    pass


if __name__ == '__main__':
    from parapy.gui import display
    obj = Aircraft(x_wing=11, y_wing=1.5)
    display(obj)