"""
@author: Dibyesh Mishra
@date: 29-12-2021 12:12
"""
import pytest

from custom_exception import UnitErrorException
from quantity_measurment import QuantMeasurment


class TestQuantity:

    @pytest.mark.parametrize("length1,length2,unit1,unit2",[(0.0, 0.0, "feet", "feet")])
    def test_zero_feet_and_zero_feet_should_return_equal(self, length1, length2, unit1, unit2):
        test1 = QuantMeasurment(length1, unit1)
        test2 = QuantMeasurment(length2, unit2)
        assert test1 == test2

    @pytest.mark.parametrize("length1,length2,unit1,unit2", [(None,0, "feet", "feet")])
    def test_if_None_should_return_exception(self, length1, unit1, length2, unit2):
            test1 = QuantMeasurment(length1, unit1)
            test2 = QuantMeasurment(length2, unit2)
            with pytest.raises(UnitErrorException) as exception:
                 test1 == test2
            assert exception.value.message == "Invalid"