
from typing import Optional
from rich.console import Console
from rich.table import Table
from foodfacts.model import Product

def display_gram_value(value: Optional[float]):
    if value is None:
        return "-"
    return '%.3f' % value +"g"

class DisplayFacts:
    def display(self, product: Product):
        table = Table(title="Data for 100g of product", show_header=False)
        table.add_column()
        table.add_column()

        table.add_row("name", product.name)
        table.add_row("energy", product.energy)
        table.add_row("protein", display_gram_value(product.protein))
        table.add_row("fiber",display_gram_value(product.fiber))
        table.add_row("fat", display_gram_value(product.fat))
        table.add_row("nutriscore", product.nutriscore)

        console = Console()
        console.print(table)


if __name__ == "__main__":
    DisplayFacts().display()
