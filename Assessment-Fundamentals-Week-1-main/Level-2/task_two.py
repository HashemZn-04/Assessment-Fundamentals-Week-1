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
    counts = {}
    for item in basket:
        if item['name'] in counts:
            counts[(item['name'], item['price'])] += 1
        else:
            counts[(item['name'], item['price'])] = 1
    return counts


def generate_receipt(basket: list) -> str:
    """
    returns a receipt after processing a basket list of dictionary of items
    with product name and price information and a total.
    """
    receipt = ""
    total = 0.0
    for name, info in count_items(basket).items():
        if info[1] != 0:
            receipt += f"{name} x {info[0]} - £{info[1]:.2f}\n"
            total += info[1]
        elif info[1] == 0:
            receipt += f"{name} x {info[0]}- Free\n"

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
