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


class BSplineSurfaceSamples(Base):
    #: Three arrays of tuples
    #: :type: collections.Sequence[collections.Sequence[Tuple]]
    data = Input([[(0, 0, 0), (11, 2, 0),   (15, 0, 0),  (0, 0, 0)],
                  [(0, 0, 10), (3, 2, 10),  (15, 0, 10),  (0, 0, 10)]])


    @Attribute(in_tree=True)
    def points(self):
        """ The tuples in the point data must be converted into arrays of
        Point.

        :rtype: collections.Sequence[collections.Sequence[Point]]
        """
        convertedpoints = []
        for tup in self.data:
            row = []
            for x, y, z in tup:
                pt = Point(x, y, z)
                row.append(pt)
            convertedpoints.append(row)
        return convertedpoints

    @Attribute
    def surf_area(self):
        return self.surf.area  # .area returns the area of the given surface

    @Attribute (in_tree=True)
    def center_of_gravity(self):
        return self.surf.cog  # .cog returns the center of gravity of the given surface or solid

    @Part
    def surf(self):
        return BSplineSurface(control_points=self.points)


if __name__ == '__main__':
    from parapy.gui import display
    point_coords = [[(0, 0, 0),  (3, 2, 0),  (11, 2, 0),  (15, 0, 0),  (11, -1, 0),  (3, -1, 0),  (0, 0, 0)],
                    [(0, 0, 5),  (3, 2, 5),  (13, 2, 5),  (15, 0, 5),  (13, -2, 5),  (3, -2, 5),  (0, 0, 5)],
                    [(0, 0, 10), (3, 2, 10), (11, 2, 10), (15, 0, 10), (11, -1, 10), (3, -1, 10), (0, 0, 10)]]
    obj1 = BSplineSurfaceSamples(data=point_coords)
    display(obj1)