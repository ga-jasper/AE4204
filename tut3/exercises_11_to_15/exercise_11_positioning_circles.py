#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2016-2018 ParaPy Holding B.V.
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


class Circles(GeomBase):

    radius = Input(1)

    @Part
    def crv1(self):
        return Circle(radius=self.radius,
                      color="red")

    # @Part
    # def crv2(self):
    #     """Single translation"""
    #     return Circle(radius=1,
    #                   position=translate(self.position,
    #                                      , # Fill in direction
    #                                      )) # Fill in distance

    # @Part
    # def crv3(self):
    #     """Multiple translations"""
    #     return Circle(radius=1,
    #                   position=translate(self.position,
    #                                      , # Fill in direction
    #                                      , # )) # Fill in distance
    #                                      ,  # Fill in direction
    #                                      ,  # )) # Fill in distance

    # @Part
    # def crv4(self):
    #     """Rotation"""
    #     return Circle(radius=1,
    #                   position=rotate(self.position,
    #                                   , # Fill in rotation axis
    #                                   , # Fill in angle in degrees
    #                                   deg=True))

    # @Part
    # def crv5(self):
    #     """translation and rotation"""
    #     return Circle(radius=1,
    #                   position=translate(rotate(self.position,
    #                                             ,
    #                                             ,
    #                                             deg=True),
    #                                      ,
    #                                      ,
    #                                      ,
    #                                      ))


if __name__ == '__main__':
    from parapy.gui import display
    display(Circles(radius=2))
