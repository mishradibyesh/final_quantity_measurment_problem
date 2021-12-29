"""
@author: Dibyesh Mishra
@date: 29-12-2021 12:06
"""
from custom_exception import UnitErrorException


class QuantMeasurment:
    def __init__(self, length , unit):
        self.length = length
        self.unit = unit

    def __eq__(self, other):
        if self.length == other.length and self.unit == other.unit:
            return True
        elif self.length is None:
            raise UnitErrorException("Invalid")
