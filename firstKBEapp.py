from prompt_toolkit.input import Input

# hello

class Aircraft():
    v_min = Input(100)
    v_max = Input(400)
    @Attribute
    def weight(self):
        return (self.fuselageWeight + self.tailWeight + self.wingWeight + self.propWeight)
class Wing():
    @Part
    def slat(self):
        return Slat()
    def flap(self):
        return Flap()
class HLD(Aircraft):
    v_min = Aircraft.v_min
    v_max = Aircraft.v_max
    @Part
    def actuator(self):
        return Actuator()
class Actuator():
    powerRequired = 0

class Flap(HLD):
    span = Input()
    chord = Input()

class Slat(HLD):
