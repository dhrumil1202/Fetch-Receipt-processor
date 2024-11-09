from math import ceil
from datetime import datetime

def alphanumeric_points(retailer):
    """Calculate points based on alphanumeric characters in retailer name."""
    return sum(char.isalnum() for char in retailer)

def round_dollar_points(total):
    """50 points if the total is a round dollar amount with no cents."""
    return 50 if float(total).is_integer() else 0

def multiple_of_quarter_points(total):
    """25 points if the total is a multiple of 0.25."""
    return 25 if (float(total) * 100) % 25 == 0 else 0

def item_pairs_points(items):
    """5 points for every two items on the receipt."""
    return (len(items) // 2) * 5

def description_length_points(item):
    """If item description length is a multiple of 3, award points based on price * 0.2, rounded up to nearest integer."""
    desc_len = len(item["shortDescription"].strip())
    if desc_len % 3 == 0:
        return ceil(float(item["price"]) * 0.2)
    return 0

def odd_day_points(purchase_date):
    """6 points if the day in the purchase date is odd."""
    day = int(purchase_date.split('-')[2])
    return 6 if day % 2 != 0 else 0

def afternoon_purchase_points(purchase_time):
    """10 points if the time of purchase is between 2:00pm and 4:00pm."""
    time = datetime.strptime(purchase_time, "%H:%M")
    return 10 if time.hour == 14 or (time.hour == 15 and time.minute <= 59) else 0
