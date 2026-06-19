"""
Note: Do not add ANY variables to the global scope. This WILL break the tests.
"""


def product_split(receipt_string: list) -> list:
    splitted_string = receipt_string.split("\n")
    products = []
    for product in splitted_string:
        products.append(product.split(" - "))
    return products


def isolate_num(products: list) -> list:
    clean_nums = []
    for pair in products:
        clean_num = pair[1].replace("£", "")
        clean_num = float(clean_num)
        clean_num = clean_num * 0.8
        clean_nums.append(clean_num)

    return clean_nums


def generate_invoice(receipt_string: str) -> str:
    products = product_split(receipt_string)

    return products  # return the invoice string


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
