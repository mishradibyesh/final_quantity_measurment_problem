"""
@author: Dibyesh Mishra
@date: 29-12-2021 12:06
"""
from custom_exception import UnitErrorException


class QuantMeasurment:
    def __init__(self, length, unit):
        self.length = length
        self.unit = unit

    def return_type(self):
        """
        returning  type of the variables
        """
        return type(self.length)

    def __eq__(self, other):


        if self.length == other.length and self.unit == other.unit:
            return True
        elif other.length is None:
            raise UnitErrorException("Invalid")

        if self.unit == "feet" and other.unit == "inch":
            other.length = other.length / 12
            if self.length == other.length:
                return True
        elif self.unit == "inch" and other.unit == "feet":
            self.length = self.length / 12
            if self.length == other.length:
                return True
        elif self.unit == "feet" and other.unit == "yard":
            other.length = other.length * 3
            if self.length == other.length:
                return True
        elif self.unit == "yard" and other.unit == "feet":
            self.length = self.length * 3
            if self.length == other.length:
                return True
        elif self.unit == "inch" and other.unit == "yard":
            other.length = other.length * 36
            if self.length == other.length:
                return True
        elif self.unit == "yard" and other.unit == "inch":
            self.length = self.length * 36
            if self.length == other.length:
                return True
        elif self.length == 0.0 and other.length == 0.0:
            return True


class Feet:
    FEET = 12.0

    def __init__(self, feet):
        self.feet = feet

    def __eq__(self, other):
        if isinstance(other, Feet):
            if self.feet == other.feet:
                return True
        return False


class Inch:
    INCH = 1.0

    def __init__(self, inch):
        self.inch = inch

    def __eq__(self, other):
        if isinstance(other, Inch):
            if self.inch == other.inch:
                return True
        return False