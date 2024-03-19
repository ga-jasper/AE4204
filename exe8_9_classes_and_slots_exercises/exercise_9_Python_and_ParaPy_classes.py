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

import time


# ---- Python class ----
class Wing:
    taper = 0.2
    c_root = 4

    def get_c_tip(self):
        print("I take 10 minutes to return")
        time.sleep(0)
        return self.c_root * self.taper
        


wing = Wing()
wing.get_c_tip()
# "I take 10 minutes to return"
# 0.8
wing.get_c_tip()
# "I take 10 minutes to return"
# 0.8
wing.taper = 0.3
wing.get_c_tip()
# "I take 10 minutes to return"
# 1.2


# ---- __init__() ----
class Wing:
    """__init__() is a special method, called class constructor or
    initialization method that Python calls when you create a new instance
    of this class
    """

    def __init__(self, taper=0.2, c_root=4):
        self.taper = taper
        self.c_root = c_root
        self.c_tip = self.get_c_tip()

    def getx(self):
        return self.get_c_tip() + 1

    def get_c_tip(self):
        print("I take 10 minutes to return")
        return self.c_root * self.taper


wing = Wing()
# "I take 10 minutes to return"
wing.c_tip
# 0.8
wing.c_tip
# 0.8
wing.taper = 0.3
wing.c_tip
# 0.8
wing.c_tip = wing.get_c_tip()
# "I take 10 minutes to return"
wing.c_tip
# 1.2


# ---- ParaPy class (variant of Exercise 9) -------------------------------------------------
# from parapy.core import *
from parapy.core import Base, Input, Attribute


class Wing(Base):
    """note the specification of the superclass Base. This makes the class
    a ParaPy class and enables lazy evaluation, caching and dependence
    tracking"""
    taper = Input(0.2)
    c_root = Input(4)

    @Attribute
    def c_tip(self):
        print("I take 10 minutes to return")
        return self.c_root * self.taper


wing = Wing()
wing.c_tip
# "I take 10 minutes to return"
# 0.8
wing.c_tip
# 0.8
wing.taper = 0.3
wing.c_tip
# "I take 10 minutes to return"
# 1.2


if __name__ == '__main__':
    from parapy.gui import display
    obj = Wing(label='wing')
    display(obj)