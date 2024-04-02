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

from math import pi

from parapy.core import *
from parapy.geom import *


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

    @Part
    def steps(self):
        return Box(quantify=self.n_step,
                   width=self.w_step,
                   length=self.l_step,
                   height=self.t_step,
                   color=self.colors[child.index % len(self.colors)],
                   position=translate(self.position,
                                      'y', child.index * self.l_step,
                                      'z', child.index * self.h_step))


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

    @Part
    def steps(self):
        return Box(quantify=self.n_step,
                   width=self.w_step,
                   length=self.l_step,
                   height=self.t_step,
                   color=self.colors[child.index % len(self.colors)],
                   position=translate(
                       rotate(self.position,
                              'z', child.index * self.angle_step),
                       'x', self.radius,
                       'z', child.index * self.h_step))

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


# =============================================================================
# Syntactical Variations
# =============================================================================

class StairCase2(StairCase):
    """Subclass of StairCase that shows child.previous syntax."""

    @Part
    def steps(self):
        return Box(quantify=self.n_step,
                   width=self.w_step,
                   length=self.l_step,
                   height=self.t_step,
                   color=self.colors[child.index % len(self.colors)],
                   position=self.position
                            if child.index == 0
                            else translate(child.previous.position,'y', self.l_step, 'z', self.h_step))

class StairCase3(StairCase):
    """Subclass of StairCase that lists step positions inside a dedicated
    ``positions`` Attribute.
    """

    @Attribute
    def positions(self):
        lst = []
        for i in range(self.n_step):
            dy = i * self.l_step
            dz = i * self.h_step
            pos = translate(self.position, 'y', dy, 'z', dz)
            lst.append(pos)
        return lst

    @Part
    def steps(self):
        return Box(quantify=self.n_step,
                   width=self.w_step,
                   length=self.l_step,
                   height=self.t_step,
                   color=self.colors[child.index % len(self.colors)],
                   position=self.positions[child.index])


class SpiralStairCase2(SpiralStairCase):
    """Subclass of SpiralStairCase that shows child.previous syntax."""

    @Part
    def steps(self):
        return Box(quantify=self.n_step,
                   width=self.w_step,
                   length=self.l_step,
                   height=self.t_step,
                   color=self.colors[child.index % len(self.colors)],
                   position=translate(self.position, 'x', self.radius)
                   if child.index == 0
                   else translate(
                       rotate(child.previous.position,
                              'z', self.angle_step,
                              ref=self.position),
                       'z', self.h_step))


class SpiralStairCase3(SpiralStairCase):
    """Subclass of SpiralStairCase that lists step positions inside a
    dedicated ``positions`` Attribute.
    """

    @Attribute
    def positions(self):
        lst = []
        for i in range(self.n_step):
            a = i * self.angle_step
            dz = i * self.h_step
            pos = rotate(self.position, 'z', a)
            pos = translate(pos, 'x', self.radius, 'z', dz)
            lst.append(pos)
        return lst

    @Part
    def steps(self):
        return Box(quantify=self.n_step,
                   width=self.w_step,
                   length=self.l_step,
                   height=self.t_step,
                   color=self.colors[child.index % len(self.colors)],
                   position=self.positions[child.index])


if __name__ == '__main__':
    from parapy.gui import display
    colors = ["red", "green", "blue", "yellow", "orange"]


    obj1 = StairCase(n_step=20, w_step=3, l_step=1, h_step=1, t_step=0.2, colors = colors, label="staircase")
    obj2 = SpiralStairCase(n_step=20, w_step=3, l_step=1, h_step=1, t_step=0.2, colors = colors, label="spiralStaircase")
    obj3 = StairCase2(label="staircase2")
    obj4 = StairCase3(label="staircase3")
    obj5 = SpiralStairCase2(n_step=20, w_step=3, l_step=1.2, h_step=1.2, t_step=0.1, colors = colors, label="spiralStaircase2")
    obj6 = SpiralStairCase3(n_step=20, w_step=3, l_step=0.8, h_step=0.8, t_step=0.8, colors = colors, label="spiralStaircase3")
    display([obj1,obj2,obj3,obj4,obj5,obj6])
