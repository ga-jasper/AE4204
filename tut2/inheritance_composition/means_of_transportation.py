from parapy.core import Base, Input, Attribute, Part, child, setslot
from parapy.geom import GeomBase, translate, Box


class MeansOfTransportation(Base):
    """this is a superclass
    """
    number_of_pax = Input(300)
    speed = Input(500)  # km/h
    cost = Input(1000000)  # $


class Train(MeansOfTransportation, GeomBase):
    """The ParaPy class GeomBase is necessary to use geometry features"""
    number_of_wagons = Input(12)
    speed = Input(200)
    wagon_length = 10  # meters

    @Part
    def wagon(self):
        return Box(quantify=self.number_of_wagons,
                   length=self.wagon_length,
                   height=1,
                   width=1,
                   position=translate(self.position, "y", child.index*(0.5+self.wagon_length)))  # positioning is explained in later tutorial


class TGV(Train):
    diner_car_colour = Input("red")

    @Attribute
    def assign_colour(self):
        return setslot(obj, "wagon[1].color", self.diner_car_colour)  # this sets the attribute of an object


class Aircraft(MeansOfTransportation):
    cruise_altitude = Input(12000)  # meters

    @Attribute
    def mach(self):
        return self.speed / 1062 if self.cruise_altitude == 1200 else "cannot evaluate"  # 1062Km/h = speed of sound at 12000m

    @Part
    def fuselage(self):
        return Fuselage(number_of_pax=self.number_of_pax)

    @Part
    def wing(self):
        return LiftingSurface()

    @Part
    def tail(self):
        return Tail()


class LiftingSurface(Base):
    max_lift_coefficient = Input(1.8)


class Fuselage(Base):
    number_of_pax = Input(80)

    @Attribute
    def fus_length(self):
        return 2 * self.number_of_pax / 4


class Tail(Base):
    @Part
    def vertical_tail(self):
        return LiftingSurface(max_lift_coefficient=1.2)

    @Part
    def horizontal_tail(self):
        return LiftingSurface(max_lift_coefficient=1)


class Fokker100(Aircraft):
    manufacturer = "Fokker"
    engine_number = 2
    operator = Input("KLM")
    livery_color = Input("Blue & White")
    number_of_pax = Input(122)


class Car(MeansOfTransportation):
    gears_number = Input(6)
    number_of_pax = Input(5)


class FlyingCar(Aircraft, Car):
    cruise_altitude = Input(5000)

    @Part
    def wheel(self):
        return Wheel(quantify=4)


class Wheel(Base):
    diameter = Input(0.8)


if __name__ == '__main__':
    from parapy.gui import display
    # obj = MeansOfTransportation(label="means of transportation", number_of_pax=200, cost=10000000)
    # obj = Train(label="train")
    # obj = TGV(label="TGV train")
    # obj = Aircraft(label="aircraft", speed=900)
    # obj = Fokker100(label="Fokker 100", speed=650)
    # obj = Car(label="Fiat 500", number_of_pax=4, gears_number=4)
    obj = FlyingCar(label="Lilium", speed=200, gears_number="automatic")
    display(obj)
