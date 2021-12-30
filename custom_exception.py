"""
@author: Dibyesh Mishra
@date: 29-12-2021 19:54
"""

class UnitErrorException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message