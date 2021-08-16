import threading

from abstract_outlet import Outlet


class HotTea(Outlet):

    def __init__(self, beverage_requirement, total_items_quantity):
        Outlet.__init__(self, total_items_quantity)
        self.beverage_requirement = beverage_requirement
        self._key_lock = threading.Lock()

    def calculate_remaining_quantity(self):
        with self._key_lock:
            print("Your drink is ready. Thank You!!")
            return True
