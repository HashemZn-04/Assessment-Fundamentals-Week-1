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
            scaled_nums.append(f"{pair[0]} - £{scaled:.2f}")
    clean_total = products[-1][0].split("£")
    total_num = float(clean_total[1])

    return scaled_nums, total_num


def generate_invoice(receipt_string: str) -> str:
    products = product_split(receipt_string)
    scaled_nums, total_num = sort_nums(products)

    lines = ["VAT RECEIPT", ""]

    if scaled_nums:
        lines += scaled_nums
        lines.append("")

    excl_vat = total_num * 0.8
    vat = total_num * 0.2

    total_line = f"Total: £{excl_vat:.2f}\nVAT: £{vat:.2f}\nTotal inc VAT: £{total_num:.2f}"
    lines.append(total_line)

    return "\n".join(lines)  # return the invoice string


if __name__ == "__main__":
    receipt_string = """Bread x 2 - £3.60
Milk x 1 - £0.80
Butter x 1 - £1.20
Total: £5.60"""
    print(generate_invoice(receipt_string))
