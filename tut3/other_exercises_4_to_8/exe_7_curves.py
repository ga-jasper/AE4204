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


from parapy.geom import *
from parapy.core import *


class BSplineSamples(GeomBase):

    pt_coords_list = Input([(0, 0, 0), (-3, 3, 0), (-11, 3, 0), (-15, 0, 0),
                            (-11, -3, 0), (-3, -3, 0), (0, 0, 0)])



    @Attribute  #(in_tree=True)  # this allows visualizing this attribute /
    # in the product tree, however it breaks laziness!!!
    def pts(self):
        return [Point(*coords) for coords in self.pt_coords_list]

    @Attribute
    def colors(self):
        return ["green", "blue", "red", "yellow", "black", "gray"]

    @Part
    def crv(self):
        return BSplineCurve(control_points=self.pts)

    @Part
    def fitted_crv(self):
        return FittedCurve(points=self.pts)

    @Part
    def crvs(self):
        return BSplineCurve(quantify=len(self.pts) - 1,
                            control_points=self.pts,
                            degree=child.index + 1, # degree max = no.points -1
                            color=self.colors[child.index])

    @Part
    # this won't move the curves! you cannot translate a curve which is built on 3D points
    # setting `position` does not change the curve, only the reference location
    # This can still be useful if you want to e.g. place airfoil curves based on their leading edge points
    def crvs_translated(self):
        return BSplineCurve(quantify=len(self.pts) - 1,
                            control_points=self.pts,
                            degree=child.index + 1,
                            color=self.colors[child.index],
                            position=translate(self.position, "z", 5+child.index))  # this is ineffective, because bspline is built on 3D control points

    @Attribute(in_tree=True)
    def pnt_distrib(self):
        return [crv.equispaced_points(30) for crv in self.crvs]

    @Attribute(in_tree=True)
    def pnt_on_crvs(self):
        return [crv.point_at_length(2) for crv in self.crvs]

    @Attribute(in_tree=True)
    def bsplinecrvs_translated(self):
        return [crv.translated(z=5) for crv in self.crvs]  # this creates "dumb" copies of the curves that are translated

    @Attribute
    def crvs_lengths(self):
        return [crv.length for crv in self.crvs]  # .length returns the length of a curve

    @Input(in_tree=True)
    def point_to_project(self):
        return Point(-10, 0, 0)

    @Attribute(in_tree=True)
    def projected_points(self):
        # return [crv.projected_point(Point(-10, 0, 0))['point'] for /
        # crv in self.crvs]
        return [crv.projected_point(self.point_to_project)['point']  #"point" is to indicate you want to get the /
                # projected point (and not the distance between the point to project and its projection, for example)
                for crv in self.crvs]

    @Attribute
    def distances_from_point(self):
        # return [crv.projected_point(Point(-10, 0, 0))['distance'] /
        # for crv in self.crvs]
        # return a dictionary, with keys distance, u and point
        return [crv.projected_point(self.point_to_project)['distance']
                for crv in self.crvs]

    @Attribute
    def tangent_at_points(self):
        return [crv.tangent_at_point(self.projected_points[crv.index])
                for crv in self.crvs]

    @Part
    def bsplinescrvs_translated_x(self):
        return TranslatedCurve(quantify=len(self.crvs),
                               curve_in=self.crvs[child.index],
                               displacement= Vector(0,0,1+child.index),
                               color=self.colors[child.index])

    @Part
    def bsplinescrvs_transformed(self):
        return TransformedCurve(quantify=len(self.crvs),
                                curve_in=self.crvs[child.index],
                                from_position=self.position,
                                to_position=translate(self.position, "z", -child.index),
                                color=self.colors[child.index])

    @Part
    def weird_loft(self):
        return LoftedSurface(profiles=[crv for crv in self.bsplinescrvs_translated_x])

    @Part
    def circles(self):  # to observe teh quality of the projection operation
        return Circle(quantify=len(self.crvs),
                      position=self.point_to_project,
                      radius=self.distances_from_point[child.index],
                      color=self.colors[child.index])

    @Attribute
    def list_of_c(self):
        return self.circles


if __name__ == '__main__':
    from parapy.gui import display

    obj = BSplineSamples()
    display(obj)
