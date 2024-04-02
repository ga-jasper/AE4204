from math import radians, pi
from parapy.core import *
from parapy.geom import *


class Staircase(GeomBase):
    n_step = Input(20)
    w_step = Input(3.0)
    l_step = Input(1.0)
    h_step = Input(0.25)
    type = Input("spiral")  # if not spiral then a straight stair will be generated
    column_radius = Input(.3)  # this is(are) the cylindrical support(s) of the stair
    colors = Input(["red", "green", "blue", "yellow", "orange", "purple", "gray", "brown"])

    @Input
    def elevation(self):  # vertical stagger between steps
        return 3 * self.h_step

    @Input
    def shift(self):  # overlap consecutive steps
        return 0.75 * self.l_step

    @Attribute
    def rotation(self):  # evaluate step rotation such to guarantee same orientation of first and last step
        return 2 * pi/(self.n_step-1)  # in radians

    @Attribute
    def total_height(self):
        return self.h_step+(self.n_step-1)*self.elevation

    @Part
    def step(self):
        return Box(quantify=self.n_step,
                   length=self.l_step,
                   width=self.w_step,
                   height=self.h_step,
                   color=self.colors[child.index % len(self.colors)],
                   position=(
                       translate(rotate(self.position,'z', self.rotation*child.index),
                                 'z', child.index * self.elevation,
                                 'x', self.column_radius,
                                 'y', -0.5 * self.l_step)
                       if self.type == "spiral"
                       else translate(self.position,
                                            'z', child.index * self.elevation,
                                            'y', self.shift * child.index)))

    @Part
    def support(self):
        return Cylinder(quantify=(1 if self.type == "spiral" else 2),  # one support in case of spiral stair, 2 /
                        # in case of straight stair
                        radius=(self.column_radius if self.type == "spiral" else self.column_radius/2),
                        height=(self.elevation * self.n_step) + 5,  # 5 to provide support when on top
                        color="Black",
                        position=translate(self.position,
                                           'z', -self.elevation,
                                           'y', (0 if self.type == "spiral" else self.shift * self.n_step),
                                           'x', (0 if self.type == "spiral" else
                                                 self.column_radius + (child.index * self.w_step - self.column_radius)))
                        # one central for spiral, two at the side for straight
                        )








if __name__ == '__main__':
    from parapy.gui import display
    obj = Staircase(n_step=20, w_step=1.5, l_step=1.0, h_step=0.25,
                    type="spiral", column_radius=0.3)
    display(obj)
