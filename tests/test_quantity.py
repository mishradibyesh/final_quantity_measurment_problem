"""
@author: Dibyesh Mishra
@date: 29-12-2021 12:12
"""
import pytest

from custom_exception import UnitErrorException
from quantity_measurment import QuantMeasurment, Feet, Inch


class TestQuantity:

    @pytest.mark.parametrize("length1,length2,unit1,unit2",[(0.0, 0.0, "feet", "feet")])
    def test_zero_feet_and_zero_feet_should_return_equal(self, length1, length2, unit1, unit2):
        test1 = QuantMeasurment(length1, unit1)
        test2 = QuantMeasurment(length2, unit2)
        assert test1 == test2

    @pytest.mark.parametrize("length1,length2,unit1,unit2", [(0, None, "feet", "feet")])
    def test_if_none_should_return_exception(self, length1, unit1, length2, unit2):
            test1 = QuantMeasurment(length1, unit1)
            test2 = QuantMeasurment(length2, unit2)
            with pytest.raises(UnitErrorException) as exception:
                test1 == test2
            assert exception.value.message == "Invalid"

    @pytest.mark.parametrize("first_length", [2.0])
    def test_compare_two_same_feet_objects(self, first_length):

        first_obj = Feet(first_length)
        second_obj = first_obj
        assert first_obj == second_obj

    @pytest.mark.parametrize("first_length", [5.0])
    def test_compare_two_same_inch_objects(self, first_length):
        first_obj = Inch(first_length)
        second_obj = first_obj
        assert first_obj == second_obj

    @pytest.mark.parametrize('length, unit',[(2 , "feet")])
    def test_compare_two_having_different_units(self, length, unit):
        first_obj = QuantMeasurment(length, unit)
        assert first_obj.return_type() is int

    @pytest.mark.parametrize('len1,unit1,len2,unit2', [(2.0, "feet", 2.0, "feet"), (2.0, "inch", 2.0, "inch")])
    def test_whether_type_is_equal(self, len1, unit1, len2, unit2):
        test1 = QuantMeasurment(len1, unit1)
        test2 = QuantMeasurment(len2, unit2)
        assert test1 == test2

    @pytest.mark.parametrize('len1,unit1,len2,unit2', [(1.0, "feet", 1.0, "inch"), (1.0, "inch", 1.0, "feet"),
                                                       (1.0, "feet", 1.0, "yard"), (1.0, "inch", 1.0, "yard")])
    def test_whether_values_are_not_equal(self, len1, unit1, len2, unit2):
        test1 = QuantMeasurment(len1, unit1)
        test2 = QuantMeasurment(len2, unit2)
        assert test1 != test2

    @pytest.mark.parametrize('len1,unit1,len2,unit2', [(2.0, "feet", 2.0, "feet"), (2.0, "inch", 2.0, "inch"),
                                                       (1.0, "feet", 12.0, "inch"), (12.0, "inch", 1.0, "feet"),
                                                       (3.0, "feet", 1.0, "yard"), (1.0, "yard", 3.0, "feet"),
                                                       (1.0, "yard", 36.0, "inch"), (36.0, "inch", 1.0, "yard")])
    def test_whether_value_is_equal(self, len1, unit1, len2, unit2):
        test1 = QuantMeasurment(len1, unit1)
        test2 = QuantMeasurment(len2, unit2)
        assert test1 == test2