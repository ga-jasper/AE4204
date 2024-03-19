# --------------- very pragmatic, bare-bones code - don't use!
class Wing0:

    b = 10.0
    c_root = 3.0
    c_tip = 2
    s = (c_root + c_tip) * b * 0.5  # this is the wing planform area

    def get_taper(self):
        print("calculating taper...")
        return self.c_tip / self.c_root

    def get_ar(self):
        print("calculating aspect ratio..")
        return self.b**2 / self.s


#  --------------- proper initialisation

class Wing1:

    def __init__(self, b: float, c_root: float, c_tip: float) -> object:
        self.b = b
        self.c_root = c_root
        self.c_tip = c_tip
        self.s = (c_root + c_tip) * b * 0. # This will be non-lazily evaluated at \
        # initialization. Also no dep. tracking

    def get_taper(self):
        print("calculating taper...")
        return self.c_tip / self.c_root

    def get_ar(self):
        print("calculating aspect ratio..")
        return self.b**2 / self.get_s()

mywing1 = Wing1(b=10.0, c_root=3.0, c_tip=2)
# try changing wingspan and see what happens!
mywing1.b = 1  # <- Never assign to other objects' attributes!
mywing1.s      # <- because most of them can't handle it!


#  ---------------------- defining the surface in initialization -------------
class Wing2:

    # using proper type hinting and docstring ...
    def __init__(self, b: float, c_root: float, c_tip:float) -> object:
        """Represents the planform of a rectangular wing

        Parameters
        ------
        ``b``: float
            Wing span in meters
        ``c_root``: float
            root chord in meters
        ``c_tip``: float
            tip chord in meters

        Provides taper ratio, aspect ratio and surface area.
        """
        self.b = b
        self.c_root = c_root
        self.c_tip = c_tip
        self.s = self.get_s()  # This will be non-lazily evaluated at \
        # initialization. Also no dep. tracking

    def get_taper(self):
        print("calculating taper...")
        return self.c_tip / self.c_root

    def get_ar(self):
        print("calculating aspect ratio..")
        return self.b**2 / self.s

    def get_s(self):  # this method can be used to evaluate the planform area\
        # using obj = Wing1() and obj.get_s()
        print("calculating planform area")
        return (self.c_root + self.c_tip) * self.b * 0.5


mywing2 = Wing2(b=10.0, c_root=3.0, c_tip=2)
s = mywing2.s
print(f'mywing2 area is {s:0.3g}m²')
# great, but we can't easily update anything about the wing now...

mywing2.b = 13  # this is still dangerous!
actual_s = mywing2.get_s() # even though we can re-compute s
print(f'modified mywing2 area is {actual_s:0.3g}m²')
s = mywing2.s   # ...because the other attributes are not recomputed
print(f'...but here it says that mywing2 area is still {s:0.3g}m²?!')




#  ------- use of @property to define attributes out of methods --------------
class Wing3:
    def __init__(self, b, c_root, c_tip):
        self.b = b
        self.c_root = c_root
        self.c_tip = c_tip

    def update_b(self, newb):
        self.b = newb
        #...and any other consequences because b has changed

    @property
    def s(self):  # s can be now evaluated as a normal attribute. \
        # I.e. obj = Wing3() and obj.s Values are NOT cached
        print("calculating planform area")
        return (self.c_root + self.c_tip) * self.b * 0.5

    def get_taper(self):
        print("calculating taper...")
        return self.c_tip / self.c_root

    def get_ar(self):
        print("calculating aspect ratio..")
        return self.b**2 / self.s

mywing3 = Wing3(b=10.0, c_root=3.0, c_tip=2)
print(f'mywing3 area is {mywing3.s:0.3g}m²')
# now we can safely update wingspan, and compute the new wing area
newb = 13.7
mywing3.update_b(newb)
print(f'mywing3 area with b={newb:0.3g}m is {mywing3.s:0.3g}m²')
# ...but s is recalculated every time..
print(f'mywing3 area with b={newb:0.3g}m is {mywing3.s:0.3g}m²')


#  ------- inheritance Class Tail inherits from Class Wing3 --------------
class Tail(Wing3):
    pass




