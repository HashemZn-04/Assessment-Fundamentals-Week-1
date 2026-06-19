"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
The only variable you are allowed to use in the global scope is the basket below.
"""

basket = []


def add_to_basket(item: dict) -> list:
    """
    returns a basket list of dictionaries
    after appending a dictionary of item information
    """
    basket.append(item)
    return basket


def count_items(basket: list) -> dict:
    """
    returns a counts dictionary where the name and price from
    the basket list of dictionaries are turned into a tuple, and
    used a key for the value of the count of each item
    """
    counts = {}
    for item in basket:
        key = (item['name'], item['price'])
        if key in counts:
            counts[key] += 1
        else:
            counts[key] = 1
    return counts


def generate_receipt(basket: list) -> str:
    """
    returns a receipt after processing a basket list of dictionary of items
    with product name and price information and a total.
    """
    receipt = ""
    total = 0.0
    for (name, price), count in count_items(basket).items():
        if price != 0:
            receipt += f"{name} x {count} - £{price:.2f}\n"
            total += price
        elif price == 0:
            receipt += f"{name} x {count}- Free\n"

    receipt += f"Total: £{total:.2f}"
    if basket == []:
        receipt = "Basket is empty"

    return receipt  # return the receipt string


if __name__ == "__main__":
    add_to_basket({
        "name": "Bread",
        "price": 1.80
    })
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
