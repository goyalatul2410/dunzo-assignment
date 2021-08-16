import threading

from abstract_outlet import Outlet


class GreenTea(Outlet):

    def __init__(self, beverage_requirement, total_items_quantity):
        Outlet.__init__(self, total_items_quantity)
        self.beverage_requirement = beverage_requirement
        self._key_lock = threading.Lock()

    def calculate_remaining_quantity(self):
        with self._key_lock:
            print("Drink cant be served because of insufficient resources!!")
            return False
