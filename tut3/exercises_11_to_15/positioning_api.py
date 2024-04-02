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


from math import pi, degrees, radians

from parapy.geom import *

# ------- Point API --------
pt1 = Point(1, 2, 3)
pt2 = Point(3, 4, 5)
pt1[0]
# 1
pt1.x
# 1
for i in pt1:
    print(i)
# 1
# 2
# 3
list(pt1)
# [1, 2, 3]
-pt1
# Point(-1, -2, -3)
pt1 - pt2
# Vector(2, 2, 2)
pt1 - pt2
# Vector(-2, -2, -2)
pt1.distance(pt2)
# 3.46...
pt1.midpoint(pt2)
# Point(2, 3, 4)
pt1.interpolate(pt2, 0.75)
# Point(2.5, 3.5, 4.5)
pt1.translate(x=1)
# Point(2, 2, 3)
pt1.rotate('z', pi/2)
pt1.rotate('z', 90, deg=True)
pt1.rotate90('z')
# Point(-2, 1, 3)
pt1.rotate_around(pt2, 'z', pi/2)
pt1.rotate_around(pt2, 'z', 90, deg=True)
pt1.rotate90_around(pt2, 'z')
# Point(5, 2, 3)
pt1.project(pt2, 'z')
# Point(3, 4, 3)
pt1.project(pt2, 'y', 'z')
# Point(3, 2, 3)
pt1.polygon('x', 1, 'y', 2)
# [Point(1, 2, 3), Point(2, 2, 3), Point(2, 4, 3)]
ORIGIN
# Point(0, 0, 0)

# -------- Position API ----------
p1 = Position(pt1, XY)
p2 = Position(pt1, YZ)
p1[0], p1.x
# (1, 1)
p1.location
# Point(1, 2, 3)
p2.orientation
# Orientation(x=Vector(0.0, 1.0, 0.0),
#             y=Vector(0.0, 0.0, 1.0),
#             z=Vector(1.0, 0.0, 0.0))
p1.Vx, p1.Vy
# (Vector(1, 0, 0), Vector(0, 1, 0))
p2.Vx, p2.Vy
# (Vector(0, 1, 0), Vector(0, 0, 1))
-p1
# Position(-1, -2, -3)
p1.translate(x=1), p2.translate(x=1)
# (Position(2, 2, 3), Position(1, 3, 3))
p1.get_point(x=1), p2.get_point(x=1)
# (Point(2, 2, 3), Point(1.0, 3.0, 3.0))
XOY, YOZ, ZOX
# ...

# -------- translate() --------
pt = Point(1, 0, 0)
translate(pt, 'x', 1)
# Point(2, 0, 0)
translate(pt, x=1)
# Point(2, 0, 0)
translate(pt, Vector(1, 0, 0), 1)
# Point(2, 0, 0)
translate(pt, 'x', 1, 'y', 1)
# Point(2, 1, 0)

pos = Position(pt).rotate90('z')
translate(pos, 'x', 1)
# Position(1, 1, 0)
translate(pos, x=1)
# Position(1, 1, 0)
translate(pos, Vector(1, 0, 0), 1)
# Position(2, 0, 0)
translate(pos, 'x', 1, 'y', 1)
# Point(0, 1, 0)

# -------- rotate() --------
pt = Point(1, 0, 0)
rotate(pt, 'z', pi/2.)
Point(0, 1, 0)
rotate(pt, 'z', radians(90))
Point(0, 1, 0)
rotate(pt, 'z', 90, deg=True)
Point(0, 1, 0)
rotate90(pt, 'z')
Point(0, 1, 0)
rotate90(pt, 'z', ref=Point(0.5, 0, 0))
Point(0.5, 0.5, 0.0)

pos = Position(pt).rotate90('z')
translate(pos, 'x', 1)
# Position(1, 1, 0)
translate(pos, x=1)
# Position(1, 1, 0)
translate(pos, Vector(1, 0, 0), 1)
# Position(2, 0, 0)
translate(pos, 'x', 1, 'y', 1)
# Point(0, 1, 0)


# ------ Position example -------
p1 = translate(XOY, x=3, y=3, z=1)
p2 = rotate90(p1, 'z')
p3 = translate(p2, x=2)
