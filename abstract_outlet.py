import threading

from abc import ABCMeta, abstractclassmethod


class Outlet(metaclass=ABCMeta):

    def __init__(self, total_items_quantity):
        self.total_items_quantity = total_items_quantity

    @abstractclassmethod
    def calculate_remaining_quantity(self):
        pass
