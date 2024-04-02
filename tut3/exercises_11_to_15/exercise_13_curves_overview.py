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

from math import pi, radians
from parapy.geom import *
from parapy.core import *


class Curves(Base):

    @Part
    def curve_definition(self):
        return CurveDefinition()

    @Part
    def curve_modification(self):
        return CurveModification()


class CurveDefinition(Base):

    @Part
    def elementary_curves(self):
        return ElementaryCurves(color="red")

    @Part
    def derived_curves(self):
        return DerivedCurves(color="black")

    @Part
    def built_from_curves(self):
        return BuiltFromCurves(color="yellow")


class CurveModification(Base):

    @Part
    def positioned_curves(self):
        return PositionedCurves()

    @Part
    def splitted_curves(self):
        return SplittedCurves()

    @Part
    def dimensioned_curves(self):
        return DimensionedCurves()

    @Part
    def chamfered_filleted_curves(self):
        return ChamferedFilletedCurves()


# -----------------------------Definition-----------------------------------------

# ------------- elementary curves


class ElementaryCurves(Base):

    @Part
    def line(self):
        return Line(reference=Point(0, 0, 0),
                    direction=Vector(1, 0, 0))

    @Part
    def circle(self):
        return Circle(radius=1)

    @Part
    def ellipse(self):
        return Ellipse(major_radius=2,
                       minor_radius=1)

    @Part
    def bezier_crv(self):
        return BezierCurve(control_points=[Point(0, 0, 0), Point(0, 1, 0), Point(1, 1, 0),
                                           Point(1, 0, 0)])

    @Part
    def bspline_crv(self):
        return BSplineCurve(control_points=[Point(0, 0, 0), Point(0, 1, 0), Point(1, 1, 0),
                                            Point(1, 0, 0)],
                            degree=2)

# ------------- derived curves


class DerivedCurves(Base):

    # ------------- derived from elementary curves
    @Part
    def line_segment(self):
        return LineSegment(start=Point(0, 0, 0),
                           end=Point(1, 0, 0))

    @Part
    def line_segment1(self):
        return LineSegment(start=Point(0, 0, 0),
                           end=Point(1, 0, 0))

    @Part
    def line_segment2(self):
        return LineSegment(start=Point(1, 0, 0),
                           end=Point(2, 2, 0))

    @Part
    def edge_segment(self):
        return EdgeSegment(start=Point(0, 0, 0),
                           end=Point(1, 0, 0))

    @Part
    def arc(self):
        """Based on a Circle."""
        return Arc(radius=1.5, angle=pi)

    @Part
    def arc3p(self):
        """Based on a Circle."""
        return Arc3P(point1=Point(-1, 0, 0),
                     point2=Point(0, 1, 0),
                     point3=Point(1, 0, 0))

    @Part
    def fitted_crv(self):
        """Based on a BSplineCurve."""
        return FittedCurve(points=[Point(0, 0, 0), Point(0, 1, 0), Point(1, 1, 0), Point(1, 0, 0)])

    @Part
    def interpolated_crv(self):
        """Based on a BSplineCurve with tangency constraints."""
        return InterpolatedCurve(points=[Point(0, 0, 0), Point(1, 0, 0)],
                                 initial_tangent=Vector(0, 1, 0),
                                 final_tangent=Vector(0, -1, 0))


# ------------- Built from curves

class BuiltFromCurves(Base):

    @Part
    def ref_line_segment1(self):
        return LineSegment(start=Point(0, 0, 0),
                           end=Point(1, 0, 0),
                           color="red")

    @Part
    def ref_line_segment2(self):
        return LineSegment(start=Point(1, 0, 0),
                           end=Point(3, 3, 3),
                           color="green")

    @Part
    def ref_fitted_crv(self):
        """Based on a BSplineCurve."""
        return FittedCurve(points=[Point(0, 0, 0), Point(0, 1, 0), Point(1, 1, 0), Point(1, 0, 0)], color="orange")

    @Part
    def wire(self):
        return Wire(curves_in=[self.ref_fitted_crv, self.ref_line_segment1], line_thickness=2)

    @Part
    def composed_crv(self):
        return ComposedCurve(built_from=[self.ref_line_segment1, self.ref_line_segment2], line_thickness=2)

# -----------------------------modification-----------------------------------------

# ------------- Positioned


class PositionedCurves(Base):

    @Part
    def ref_line_segment(self):
        return LineSegment(start=Point(0, 0, 0),
                           end=Point(1, 0, 0),
                           color="blue")

    @Part
    def translated_crv(self):
        return TranslatedCurve(curve_in=self.ref_line_segment,
                               displacement=Vector(0, 1, 0))

    @Part
    def rotated_crv(self):
        return RotatedCurve(curve_in=self.ref_line_segment,
                            rotation_point=Point(0, 0, 0),
                            vector=Vector(0, 0, 1),
                            angle=radians(90))

    @Part
    def transformed_crv(self):
        """axis to axis transformation """
        return TransformedCurve(curve_in=self.ref_line_segment,
                                from_position=OXY,
                                to_position=ZOX(z=1))

    @Part
    def mirrored_crv(self):
        """point mirror """
        return MirroredCurve(curve_in=self.ref_line_segment,
                             reference_point=Point(0, 1, 0))

# ------------- Splitted


class SplittedCurves(Base):

    @Part
    def ref_line_segment(self):
        return LineSegment(start=Point(0, 0, 0),
                           end=Point(1, 0, 0),
                           color="blue")

    @Part
    def splitted_crv(self):
        """Returns a wire consisting of two curves"""
        return SplitCurve(curve_in=self.ref_line_segment,
                          tool=Point(0.5, 0, 0))

    @Part
    def splitted_edge(self):
        return SplitEdge(built_from=self.ref_line_segment,
                         tool=Point(0.2, 0, 0))


# ------------- Dimensioned


class DimensionedCurves(Base):

    @Part
    def ref_line_segment(self):
        return LineSegment(start=Point(0, 0, 0),
                           end=Point(1, 0, 0),
                           color="blue")

    @Part
    def scaled_crv(self):
        return ScaledCurve(curve_in=self.ref_line_segment,
                           reference_point=Point(0, 0, 0),
                           factor=2)

    @Part
    def extended_crv(self):
        return ExtendedCurve(curve_in=self.ref_line_segment,
                             to_point=Point(2, 1, 0))

    @Part
    def trimmed_crv(self):
        return TrimmedCurve(basis_curve=self.ref_line_segment,
                            limit1=Point(0.2, 0, 0), limit2=Point(0.8, 0, 0), color="red", line_thickness=2)

# ------------- Chamfered / filleted


class ChamferedFilletedCurves(Base):

    @Part
    def rectangular_wire(self):
        return Rectangle(width=2, length=1, hidden=True)

    @Part
    def chamfered_wire(self):
        return ChamferedWire(built_from=self.rectangular_wire, distance=0.1, color="blue")

    @Part
    def filleted_wire(self):
        return FilletedWire(built_from=self.rectangular_wire, radius=0.1, color="red")

    @Attribute
    def polygon(self):
        return Polygon(points=[Point(0, 0, 0), Point(1, 0, 0), Point(1, 1, 0)])


if __name__ == '__main__':
    from parapy.gui import display
    obj = Curves(label="ParaPy_curves")
    display(obj)
