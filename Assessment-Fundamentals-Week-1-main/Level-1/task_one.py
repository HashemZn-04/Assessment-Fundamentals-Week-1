
"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []


def add_product() -> str:
    """Returns a string of the product the user inputs"""
    return input("What product would you like to add? ")


def add_price(product: str) -> float:
    product = add_product()
    return input(f"What is the price of {product}? ")


def check_valid_price(price: float) -> bool:
    product = add_product()
    price = None

    while not isinstance(price, float) or isinstance(price, int):
        print("You must enter a valid number for the price!")
        price = add_price(product)
    return True


def create_item(product: str, price: float) -> dict:
    item = {}

    return item


def add_to_basket(item: dict) -> list:
    basket.append(item)
    return basket


def generate_receipt(basket: list) -> str:
    receipt = ""
    return receipt  # return the receipt string


if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
    add_to_basket({
        "name": "Milk",
        "price": 0.80
    })
    add_to_basket({
        "name": "Butter",
        "price": 1.20
    })
    print(generate_receipt(basket))
