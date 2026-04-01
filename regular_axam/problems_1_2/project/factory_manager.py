from collections import defaultdict

from regular_axam.problems_1_2.project.products.chair import Chair
from regular_axam.problems_1_2.project.products.hobby_horse import HobbyHorse
from regular_axam.problems_1_2.project.stores.furniture_store import FurnitureStore
from regular_axam.problems_1_2.project.stores.toy_store import ToyStore


class FactoryManager:
    VALID_PRODUCTS = {
        "Chair": Chair,
        "HobbyHorse": HobbyHorse
    }

    VALID_STORES = {
        "FurnitureStore": FurnitureStore,
        "ToyStore": ToyStore
    }

    STORE_SUBTYPE_MAP = {
        "FurnitureStore": "Furniture",
        "ToyStore": "Toys"
    }

    def __init__(self, name: str):
        self.name = name
        self.income = 0.0
        self.products = []
        self.stores = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.VALID_PRODUCTS:
            raise Exception("Invalid product type!")

        product = self.VALID_PRODUCTS[product_type](model, price)
        self.products.append(product)
        return f"A product of sub-type {product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.VALID_STORES:
            raise Exception(f"{store_type} is an invalid type of store!")

        store = self.VALID_STORES[store_type](name, location)
        self.stores.append(store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store, *products):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        needed_sub_type = self.STORE_SUBTYPE_MAP[store.store_type]
        valid_products = [p for p in products if p.sub_type == needed_sub_type]

        if not valid_products:
            return "Products do not match in type. Nothing sold."

        for product in valid_products:
            store.products.append(product)
            self.products.remove(product)

        store.capacity -= len(valid_products)
        self.income += sum(p.price for p in valid_products)

        return f"Store {store.name} successfully purchased {len(valid_products)} items."

    def unregister_store(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)

        if store is None:
            raise Exception("No such store!")

        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str):
        discounted = [p for p in self.products if p.model == product_model]

        for product in discounted:
            product.discount()

        return f"Discount applied to {len(discounted)} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = next((s for s in self.stores if s.name == store_name), None)

        if store is None:
            return "There is no store registered under this name!"

        return store.store_stats()

    def statistics(self):
        product_counts = defaultdict(int)

        for product in self.products:
            product_counts[product.model] += 1

        result = [
            f"Factory: {self.name}",
            f"Income: {self.income:.2f}",
            "***Products Statistics***",
            f"Unsold Products: {len(self.products)}. Total net price: {sum(p.price for p in self.products):.2f}"
        ]

        for model in sorted(product_counts):
            result.append(f"{model}: {product_counts[model]}")

        result.append(f"***Partner Stores: {len(self.stores)}***")

        for store in sorted(self.stores, key=lambda s: s.name):
            result.append(store.name)

        return "\n".join(result)