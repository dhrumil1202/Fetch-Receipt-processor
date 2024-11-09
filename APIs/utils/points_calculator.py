from .rules import (
    alphanumeric_points,
    round_dollar_points,
    multiple_of_quarter_points,
    item_pairs_points,
    description_length_points,
    odd_day_points,
    afternoon_purchase_points,
)


def calculate_points(receipt):
    total_points = 0

    total_points += alphanumeric_points(receipt['retailer'])
    total_points += round_dollar_points(receipt['total'])
    total_points += multiple_of_quarter_points(receipt['total'])
    total_points += item_pairs_points(receipt["items"])

    for item in receipt["items"]:
        total_points += description_length_points(item)

    total_points += odd_day_points(receipt["purchaseDate"])
    total_points += afternoon_purchase_points(receipt["purchaseTime"])

    return total_points