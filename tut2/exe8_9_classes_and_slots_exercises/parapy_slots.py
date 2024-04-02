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


from parapy.core import Base, Input, Attribute, Part, val, child

# ----------------- example (Wing0) input and attributes ----------------------


class Wing0(Base):
    taper = Input(1)
    c_root = Input(4.0, label="root chord")
    thickness = Input()

    @Input
    def c_tip_as_input(self):
        """This is an input (thus settable via the GUI property grid),
        which is evaluated based on expression
        """
        return self.c_root * self.taper

    @Attribute
    def c_tip_as_attribute(self):
        return self.c_root*self.taper


# ------------------  other example (Wing1) with Part-------------------------
class Airfoil1(Base):
    thickness = Input(0.1)
    chord = Input(1)


class Wing1(Base):
    thickness = Input(0.2)
    chord = Input(2)

    @Part
    def airfoil(self):
        return Airfoil1(pass_down="thickness",
                        chord=self.chord,
                        hidden=self.chord >= 3,  # child is hidden (not visible in GUI product tree)
                        suppress=self.chord >= 4)  # child is not generated at all
# test your self the hidden and suppress
# obj = Wing1()
# print(obj.airfoil.thickness)
# # 0.2
# print(obj.airfoil.chord)
# # 2
# print(obj.airfoil.hidden)
# # False
# obj.chord = 3
# print(obj.airfoil.hidden)
# # True
# obj.chord = 4
# print(obj.airfoil)
# # Undefined

# ------------------------------- other example (Wing) with quantified parts----------------------------


class Airfoil(Base):
    thickness = Input(1)
    chord = Input(1)
    lift_coefficient = Input (0.2)


class Wing(Base):
    n_airfoils = Input(2)

    # raises an error if the thickness value is not <Greater than or Equal to> 0.1
    thickness = Input(0.2, validator=val.GE(0.1))

    def my_method(self):
        return

    @Attribute
    def lift_coefficients(self):
        return [0.5, 0.6, 0.8]

    # @Part[(**kwargs)]
    # def <name>(self):
    #     return <Class>(*args,
    #                    hidden=bool,
    #                    suppress=bool,
    #                    quantify=int,
    #                    pass_down=str,
    #                    map_down=str,
    #                    **kwargs)

    @Part
    def airfoils(self):
        return Airfoil(quantify=self.n_airfoils,
                       pass_down="thickness",  # short-hand notation for thickness=self.thickness
                       map_down="lift_coefficients->lift_coefficient",  # short-hand notation for lift_coefficient=self.lift_coefficients[child.index]
                       chord=0.1*(child.index+1))


# obj = Wing()
# print(obj.airfoils)
# # <Sequence root.airfoils at 0x4b4f2e8>
# print(len(obj.airfoils))
# # 2
# print(obj.airfoils[0].chord)
# # 0.1
# print(obj.airfoils[-1].chord)
# # 0.2
# print([item.chord for item in obj.airfoils])
# # [0.1, 0.2]

if __name__ == '__main__':
    from parapy.gui import display
    obj = Wing0(thickness=0.2, label="wing")
    display(obj)
