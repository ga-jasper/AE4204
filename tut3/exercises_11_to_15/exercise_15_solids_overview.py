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

from math import radians

import math
from parapy.core import Attribute, Part
from parapy.geom import *


class BuildingSolids(GeomBase):
    # ------------- elementary
    @Part
    def box(self):
        return Box(length=1, width=2, height=3, centered=True)

    @Part
    def cone(self):
        return Cone(radius1=1, radius2=0.4, height=2)

    @Part
    def sphere(self):
        return Sphere(radius=2)

    @Part
    def torus(self):
        return Torus(major_radius=3, minor_radius=1)

    @Part
    def wedge(self):
        return Wedge(dx=2, dy=1, dz=2, xmin=0.5, zmin=0.5, xmax=1.5, zmax=1.5)

    @Part
    def cube(self):
        return Cube(dimension=2)

    @Part
    def cylinder(self):
        return Cylinder(radius=1, height=2, angle=(math.pi * 3. / 2.))

    # ------------- built from curve(area)
    @Attribute
    def circles(self):
        c1 = Circle(radius=1.0, position=XOY)
        c2 = Circle(radius=2.0, position=XOY.translate('z', 5))
        c3 = Circle(radius=1.0, position=XOY.translate('z', 10))
        return c1, c2, c3

    @Part
    def ruled_sld(self):
        """Returns multiple (ruled) surfaces from multiple curves"""
        return RuledSolid(profiles=self.circles)

    @Part
    def lofted_sld(self):
        """Returns a single surface through multiple curves"""
        return LoftedSolid(profiles=self.circles)

    # ------------- built from surface(area)
    @Part
    def box1(self):
        return Box(height=1, length=1, width=1, centered=True)

    @Part
    def box2(self):
        return Box(height=2, length=2, width=2, centered=True)

    @Part
    def sld(self):
        return Solid(built_from=self.box2, holes=[self.box1])

    @Part
    def sewn_sld(self):
        return SewnSolid(built_from=self.box.faces)

    # ------------- Swept
    @Part
    def path(self):
        return BezierCurve(control_points=[Point(0, 0, 0), Point(0, -1, 0), Point(1, -1, 0),
                                           Point(1, 0, 0)])

    @Part
    def pipe_sld(self):
        return PipeSolid(path=self.path,
                         radius=0.1)

    @Part
    def profile(self):
        return Rectangle(width=1, length=1)

    @Part
    def extruded_sld(self):
        return ExtrudedSolid(island=self.profile, distance=1, direction=(0, 0, 1))

    @Part
    def swept_path(self):
        return InterpolatedCurve(points=[Point(0, 0, 0), Point(0, 1, 1), Point(0, 1, 2)])

    @Part
    def swept_sld(self):
        return SweptSolid(path=self.swept_path,
                          profile=self.profile)

    # ------------- Positioned
    @Part
    def translated_sld(self):
        return TranslatedShape(shape_in=self.pipe_sld,
                               displacement=Vector(0, 1, 0))

    @Part
    def rotated_sld(self):
        return RotatedShape(shape_in=self.pipe_sld,
                              rotation_point=Point(0, 0, 0),
                              vector=Vector(1, 0, 0),
                              angle=radians(90))

    @Part
    def transformed_sld(self):
        """axis to axis transformation """
        return TransformedShape(shape_in=self.pipe_sld,
                                from_position=OXY,
                                to_position=ZOX(z=2))

    @Part
    def mirrored_sld(self):
        """point mirror """
        return MirroredShape(shape_in=self.pipe_sld,
                             reference_point=Point(1, 1, 0))

    # ------------- Splitted
    @Part
    def plane(self):
        return Plane()

    @Part
    def splitted_sld(self):
        """Returns a wire consisting of two curves"""
        return SplitSolid(built_from=self.box,
                          tool=self.plane)

    @Part
    def local_splitted_sld(self):
        return LocalSplitSolid(built_from=self.box,
                               domain=self.box.faces[1],
                               tool=self.plane)

    # ------------- Chamfered / filleted
    @Attribute
    def table(self):
        e1, e2, e3, e4 = self.box.top_face.edges
        return (e1, e2, (e3, 0.2), (e4, 0.2))

    @Part
    def filleted_sld(self):
        return FilletedSolid(built_from=self.box,
                             radius=0.1,
                             edge_table=self.table)

    @Part
    def chamfered_sld(self):
        return ChamferedSolid(built_from=self.box,
                              distance=0.1,
                              edge_table=self.table)


if __name__ == '__main__':
    from parapy.gui import display

    obj = BuildingSolids()
    display(obj)
