from collections import defaultdict

from regular_axam.problems_1_2.project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    def __init__(self, name: str, location: str):
        super().__init__(name, location, 100)

    @property
    def store_type(self):
        return "ToyStore"

    def store_stats(self):
        models = defaultdict(list)

        for product in self.products:
            models[product.model].append(product.price)

        result = [
            f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}",
            self.get_estimated_profit(),
            "**Toys for sale:"
        ]

        for model in sorted(models):
            count = len(models[model])
            avg_price = sum(models[model]) / count
            result.append(f"{model}: {count}pcs, average price: {avg_price:.2f}")

        return "\n".join(result)