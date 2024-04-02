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


from math import pi

from parapy.geom import *
from parapy.core import *


class StairCase(GeomBase):
    """StairCase assembles ``n_step`` steps. Both dimensions and color of
    individual steps are parameterized. Rules for step ``color`` and
    ``position`` rules demonstrate ``child.index`` notation.
    """

    n_step = Input(20)
    w_step = Input(3)
    l_step = Input(1)
    h_step = Input(1)
    t_step = Input(0.2)
    colors = Input(["red", "green", "blue", "yellow", "orange"])


    # @Part
    # def steps(self):
    #     """Translation in a sequence"""
    #     return Box(quantify=self.n_step,
    #                width=self.w_step,
    #                length=self.l_step,
    #                height=self.t_step,
    #                color=self.colors[child.index % len(self.colors)],
    #                position=translate()
    #                )


class SpiralStairCase(StairCase):
    """Spiraling version of the basic StairCase. Positioning of steps now
    requires additional rotation. Moreover, the staircase assembles extra
    inner and outer columns. Outer column has custom display settings.
    """

    radius = Input(1)
    n_revol = Input(1)

    @Attribute
    def angle_step(self):
        """Angle over which each next step should rotate w.r.t. former."""
        return self.n_revol * 2 * pi / (self.n_step - 1)

    # @Part
    # def steps(self):
    #     """Translation and rotation in a sequence"""
    #     return Box(quantify=self.n_step,
    #                width=self.w_step,
    #                length=self.l_step,
    #                height=self.t_step,
    #                color=self.colors[child.index % len(self.colors)],
    #                position=
    #                )

    @Part
    def inner_column(self):
        return Cylinder(radius=self.radius,
                        height=self.h_step * self.n_step,
                        color="black")

    @Part
    def outer_column(self):
        return Cylinder(radius=self.radius + self.w_step,
                        height=self.inner_column.height,
                        color="black",
                        display_mode="wireframe",
                        isos=(20, 5))


if __name__ == '__main__':
    from parapy.gui import display

    obj1 = StairCase()
    obj2 = SpiralStairCase()
    str_stairs = StairCase(n_step=20, w_step=1.5, l_step=1.0, h_step=0.25,
                           t_step=0.18, label='straight_stairs')
    sp_stairs = SpiralStairCase(n_step=20, w_step=1.5, l_step=1.0, h_step=0.25,
                          t_step=0.18, radius=0.5, n_revol=2, label='spiral_stairs')
    display([str_stairs, sp_stairs])
