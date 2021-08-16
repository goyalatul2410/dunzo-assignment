import json
# import multiprocessing
# import random

# from abstract_outlet import Outlet
from hot_coffee import HotCoffee
from hot_tea import HotTea
from black_tea import BlackTea
from green_tea import GreenTea


class BeverageFactory:

    def get_beverage_class(self, beverage_type=None):
        if not beverage_type:
            return None

        if beverage_type == "hot_tea":
            return HotTea
        elif beverage_type == "hot_coffee":
            return HotCoffee
        elif beverage_type == "black_tea":
            return BlackTea
        elif beverage_type == "green_tea":
            return GreenTea


def main(beverage_orders):
    output = []
    f = open('beverage_details.json', )
    beverage_details = json.load(f)

    outlet_number = beverage_details.get("machine").get("outlets").get("count_n")

    total_items_quantity = beverage_details.get("machine").get("total_items_quantity")

    beverages = beverage_details.get("machine").get("beverages")

    for beverage_type in beverage_orders:
        beverage_requirement = beverages.get(beverage_type, None)

        beverage_factory = BeverageFactory()
        beverage_class = beverage_factory.get_beverage_class(beverage_type)
        beverage = beverage_class(beverage_requirement, total_items_quantity)
        output.append(beverage.calculate_remaining_quantity())

    return output


if __name__ == "__main__":
    print(main(["hot_tea", "hot_coffee", "black_tea", "green_tea"]))
    # f = open('beverage_details.json', )s
    # beverage_details = json.load(f)
    #
    # outlet_number = beverage_details.get("machine").get("outlets").get("count_n")
    #
    # total_items_quantity = beverage_details.get("machine").get("total_items_quantity")
    #
    # beverages = beverage_details.get("machine").get("beverages")
    # available_beverages = list(beverages.keys())
    #
    # beverage_orders = available_beverages
    #
    # for beverage_type in beverage_orders:
    #     beverage_requirement = beverages.get(beverage_type, None)
    #
    #     beverage_factory = BeverageFactory()
    #     beverage_class = beverage_factory.get_beverage_class(beverage_type)
    #     beverage = beverage_class(beverage_requirement)
    #     beverage.calculate_remaining_quantity()

    # beverage_requirement = []
    # beverage_type = None
    # for _ in range(outlet_number):
    #     beverage_type = random.choice(available_beverages)
    #     beverage_requirement.append(beverages.get(beverage_type, None))
    #     beverage = beverage_class(beverage_requirement)
    #     beverage.calculate_remaining_quantity()

    # with multiprocessing.Pool(processes=outlet_number) as pool:
    #     # beverage_type = random.choice(available_beverages)
    #     # beverage_requirement = beverages.get(beverage_type, None)
    #
    #     beverage_factory = BeverageFactory()
    #     beverage_class = beverage_factory.get_beverage_class(beverage_type)
    #
    #     beverage = beverage_class(beverage_requirement)
    #
    #     pool.apply(beverage.calculate_remaining_quantity)
    #
    #     # reports = pool.map(beverage.throw_away_function, [])
    #
    #     print(reports)


    # print("A")



