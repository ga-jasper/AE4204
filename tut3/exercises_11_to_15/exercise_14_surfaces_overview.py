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

from parapy.core import Attribute, Part
from parapy.geom import *


class BuildingSurfaces(GeomBase):
    # ------------- elementary
    @Part
    def planar_srf(self):
        return Plane(reference=Point(0, 0, 0),
                     normal=Vector(1, 0, 0))

    @Part
    def rectangular_srf(self):
        return RectangularSurface(width=2.0, length=1.0)

    @Part
    def rectangular_face(self):
        return RectangularFace(width=2.0, length=1.0)

    @Part
    def cylindrical_srf(self):
        return CylindricalSurface(radius=1, height=2)

    @Part
    def circular_face(self):
        return CircularFace(radius=1.0)

    @Part
    def spherical_srf(self):
        return SphericalSurface(radius=1)

    @Part
    def toroidal_srf(self):
        return ToroidalSurface(major_radius=5, minor_radius=1)

    @Attribute
    def pts(self):
        return ((Point(0, 0, 0), Point(1, 1, 0), Point(2, 0, 0)),
                (Point(0, 0, 1), Point(1, -1, 1), Point(2, 0, 1)),
                (Point(0, 0, 2), Point(1, 1, 2), Point(2, 0, 2)))

    @Part
    def bezier_srf(self):
        return BezierSurface(control_points=self.pts)

    @Part
    def bspline_srf(self):
        return BSplineSurface(control_points=self.pts)

    # # ------------- derived from elementary surfaces
    @Part
    def fitted_srf(self):
        """Based on a BSplineSurface."""
        return FittedSurface(points=self.pts)

    @Part
    def interpolated_srf(self):
        """Based on a BSplineSurface."""
        return InterpolatedSurface(points=self.pts)

    # ------------- built from curve(area)
    @Part
    def face(self):
        return Face(island=Circle(radius=1))

    @Attribute
    def circles(self):
        c1 = Circle(radius=1.0, position=XOY)
        c2 = Circle(radius=2.0, position=XOY.translate('z', 5))
        c3 = Circle(radius=1.0, position=XOY.translate('z', 10))
        return c1, c2, c3

    @Part
    def ruled_srf(self):
        """Returns a single (ruled) surface from 2 curves"""
        return RuledSurface(curve1=self.circles[0],
                            curve2=self.circles[1])

    @Part
    def ruled_shell(self):
        """Returns multiple (ruled) surfaces from multiple curves"""
        return RuledShell(profiles=self.circles)

    @Part
    def lofted_srf(self):
        """Returns a single surface through multiple curves"""
        return LoftedSurface(profiles=self.circles)

    @Part
    def lofted_shell(self):
        return LoftedShell(profiles=self.circles)

    # ------------- built from surface(area)
    @Attribute
    def face1(self):
        return Box(length=1, height=1, width=1).top_face

    @Attribute
    def face2(self):
        return Box(length=1, height=1, width=1).front_face

    @Part
    def shell(self):
        return SewnShell(built_from=[self.face1, self.face2])

    # ------------- Swept
    @Part
    def path(self):
        return BezierCurve(control_points=[Point(0, 0, 0), Point(0, 1, 0), Point(1, 1, 0),
                                           Point(1, 0, 0)])

    @Part
    def pipe_srf(self):
        return PipeSurface(path=self.path,
                           radius=0.1)

    @Part
    def line_segment(self):
        return LineSegment(start=Point(0, 0, 0),
                           end=Point(1, 0, 0))

    @Part
    def profile(self):
        return Rectangle(width=1, length=1)

    @Part
    def extruded_shell(self):
        return ExtrudedShell(profile=self.profile, distance=1, direction=(0, 0, 1))

    @Part
    def pipe_shell(self):
        return PipeShell(path=self.path, radius=0.2)

    # ------------- Positioned
    @Part
    def translated_srf(self):
        return TranslatedSurface(surface_in=self.rectangular_srf,
                                 displacement=Vector(0, 1, 0))

    @Part
    def translated_plane(self):
        return TranslatedPlane(built_from=self.planar_srf, displacement=1)

    @Part
    def rotated_srf(self):
        return RotatedSurface(surface_in=self.rectangular_srf,
                              rotation_point=Point(0, 0, 0),
                              vector=Vector(1, 0, 0),
                              angle=radians(90))

    @Part
    def transformed_srf(self):
        """axis to axis transformation """
        return TransformedSurface(surface_in=self.rectangular_srf,
                                  from_position=XOY,
                                  to_position=ZOX(z=2))

    @Part
    def mirrored_srf(self):
        """point mirror """
        return MirroredSurface(surface_in=self.rectangular_srf,
                               reference_point=Point(1, 1, 0))

    # ------------- Splitted
    @Attribute
    def box_shell(self):
        return Box(1, 1, 1, centered=True).outer_shell

    @Part
    def splitted_srf(self):
        """Returns a wire consisting of two curves"""
        return SplitSurface(built_from=self.box_shell,
                            tool=self.planar_srf)

    @Part
    def local_splitted_srf(self):
        return LocalSplitSurface(built_from=self.box_shell,
                                 domain=self.box_shell.faces[5],
                                 tool=self.planar_srf)

    # ------------- Dimensioned
    @Part
    def scaled_srf(self):
        return ScaledSurface(surface_in=RectangularSurface(width=2.0, length=1.0),
                             reference_point=Point(0, 0, 0),
                             factor=2)

    @Part
    def extended_srf(self):
        return ExtendedSurface(surface_in=FittedSurface(points=[[Point(0, 0, 0), Point(1, 0, 0)],
                                                                [Point(0, 1, 0), Point(1, 1, 0)]]),
                               distance=1.0,
                               side='all')

    @Part
    def trimmed_srf(self):
        return TrimmedSurface(built_from=RectangularFace(1, 1),
                              island=Circle(0.25))

    # ------------- Chamfered / filleted

    @Part
    def filleted_surface(self):
        return FilletedFace(built_from=self.rectangular_face, radius=0.1)

    @Part
    def chamfered_face(self):
        return ChamferedFace(built_from=self.rectangular_face, distance=0.1)

    @Part
    def box(self):
        return Box(width=1, length=1, height=1)

    @Attribute
    def table(self):
        e1, e2, e3, e4 = self.box.top_face.edges
        return (e1, e2, (e3, 0.2), (e4, 0.2))

    @Part
    def filleted_shell(self):
        return FilletedShell(built_from=self.box.outer_shell,
                             radius=0.1,
                             edge_table=self.table)

    @Part
    def chamfered_shell(self):
        return ChamferedShell(built_from=self.box.outer_shell,
                              distance=0.1,
                              edge_table=self.table)


if __name__ == '__main__':
    from parapy.gui import display
    obj = BuildingSurfaces(label="ParaPy_surfaces")
    display(obj)
