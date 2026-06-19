"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def product_split(receipt_string: list) -> list:
    splitted_string = receipt_string.split("\n")
    products = []
    for product in splitted_string:
        products.append(product.split(" - "))
    return products


def sort_nums(products: list) -> list:
    scaled_nums = []
    for pair in products:
        if len(pair) == 2:
            scaled = pair[1].replace("£", "")
            scaled = float(scaled)
            scaled = scaled * 0.8
            scaled_nums.append(f"{pair[0]} - {scaled}")
    clean_total = products[:-1].split("£")
    scaled_nums.append(clean_total)

    return scaled_nums


def generate_invoice(receipt_string: str) -> str:
    products = product_split(receipt_string)
    products_formatted = sort_nums(products)

    return   # return the invoice string


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
