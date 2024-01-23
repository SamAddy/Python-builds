import math
import time
from calendar import day_name

from datetime import datetime, date

# cart_type = {
#     cart_value: int,
#     delivery_distance: int,
#     number_of_items: int,
#     time: str
# }


new_cart = {
    "cart_value": 790,
    "delivery_distance": 2235,
    "number_of_items": 4,
    "time": "2024-01-15T13:00:00Z"
}


def convert_cents_to_eur(cart_value):
    return cart_value / 100


def calculate_distance_fee(distance: int) -> int:
    base_fee = 2
    additional_fee = 1

    if distance <= 1000:
        return base_fee

    additional_distance = distance - 1000

    if additional_distance <= 500:
        return base_fee + additional_fee

    additional_distance_interval = math.ceil((additional_distance) / 500)

    return base_fee + additional_fee * additional_distance_interval

def calculate_item_surcharge(number_of_items: int, cart_value: int) -> int:
    if number_of_items < 4 and cart_value > 10:
        return 0

    base_surcharge = 0.50
    number_of_items_without_surcharge = 4
    surcharge = (number_of_items - number_of_items_without_surcharge) * base_surcharge
    extra_fee = 0 if number_of_items < 12 else 1.20

    if cart_value < 10:
        surcharge += abs(10 - cart_value)

    return surcharge + extra_fee


def calculate_rush_hour_fee(day: datetime) -> float:
    weekday = day_name[day.weekday()]
    time_ = day.time()
    seconds = (time_.hour * 60 + time_.minute) * 60 + time_.second
    rush_hour_fee = 1.2

    if weekday == "Friday" and seconds in range(54000, 68400):
        return rush_hour_fee
    return 1


def calculate_delivery_fees(cart: dict) -> dict:
    cart["cart_value"] = convert_cents_to_eur(cart["cart_value"])
    print("value converted: ", cart["cart_value"])
    if cart["cart_value"] >= 200:
        return 0

    total_fees = calculate_distance_fee(cart["delivery_distance"])
    total_fees += calculate_item_surcharge(cart["number_of_items"], cart["cart_value"])


    day = datetime.fromisoformat(cart["time"])
    total_fees *= calculate_rush_hour_fees(day)

    return total_fees


def calculate_fees_for_delivery(cart: dict) -> int:
    total_fees_for_delivery = 0
    surcharge = 0

    if cart["cart_value"] >= 200:
        return total_fees_for_delivery

    if cart["cart_value"] < 10:
        surcharge = 10 - cart["cart_value"]
        total_fees_for_delivery += surcharge

    if cart["delivery_distance"] >= 1000:
        base_fee = 2
        additional_distance = cart["delivery_distance"] - 1000

        if additional_distance <= 500:
            base_fee += 1
            total_fees_for_delivery += base_fee

        else:
            surcharge = additional_distance % 500
            base_fee += surcharge
            total_fees_for_delivery += base_fee

    if cart["number_of_items"] >= 5:
        extra_fee = 0
        base_surcharge = 0.50
        number_of_items_without_surcharge = 4

        surcharge = (cart["number_of_items"] - number_of_items_without_surcharge) * base_surcharge

        if cart["number_of_items"] >= 12:
            extra_fee = 1.20

        total_fees_for_delivery += surcharge + extra_fee

    day = datetime.fromisoformat(cart["time"])
    weekday = day_name[day.weekday()]
    time_in_day = day.time()
    seconds = (time_in_day.hour * 60 + time_in_day.minute) * 60 + time_in_day.second
    rush_hour_fee = 1.2

    if day == "Friday" and seconds in range(54000, 68401):
        total_fees_for_delivery *= rush_hour_fee

    return total_fees_for_delivery


print("hey there!")
print(f"delivery fee - first code: {calculate_fees_for_delivery(new_cart)}")
print("=================== second code ====================")
print(f"delivery fee 2: {calculate_delivery_fees(new_cart)}")

print("")
print("=================== testing delivery distance fee ====================")
distances = [401, 999, 1499, 1500, 1501,  1599, 2235]
for d in distances:
    print(f"{d} distance fee: {calculate_distance_fee(d)}")


print("")
print("====================== testing item surcharge fee =====================")
surcharges = [(4, 15), (5, 25), (10, 20), (13, 20), (14, 20)]
for item in surcharges:
    print(f"num_of_items: {item[0]}, cart_value: {item[1]} "
          f"-> surcharge: {calculate_item_surcharge(item[0], item[1])} eur")

print("")
print("================ test rush hour fee ==================================")
times = ["2024-01-15T13:00:00Z", "2024-01-19T15:30:00Z"]
datetimes = []

for t in times:
    datetimes.append(datetime.fromisoformat(t))

for dt in datetimes:
    print(f"rush hour fee: {calculate_rush_hour_fee(dt)}")

