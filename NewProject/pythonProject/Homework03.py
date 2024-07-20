import random
import re
from datetime import datetime


def get_days_from_today(date):
    try:
        str_date_to_datetime = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        date_difference = (today - str_date_to_datetime).days
        return date_difference
    except ValueError:
        print(f"Invalid date {date}. Try write date format YYYY-MM-DD")


date = "1998-11-01"
print(f"З моменту {date} пройшло - {get_days_from_today(date)}")


def get_numbers_ticket(min, max, quantity):
    numbers_list = set()
    if not (1 <= min < max <= 1000) or max - min < quantity - 1:
        return list(numbers_list)
    for i in range(quantity ** 2):
        numb = random.randint(min, max)
        if not len(numbers_list) == quantity:
            numbers_list.add(numb)
        else:
            break
    return sorted(list(numbers_list))


print("Ваш щасливий квиток: ", get_numbers_ticket(101, 106, 6))


def normalize_phone(phone_number: str):
    pattern_without_numb = r"\D"
    pattern_start_numb_zero = r"^0"
    normalize_phone_numb = re.sub(pattern_without_numb, "", phone_number)
    if re.match(pattern_start_numb_zero, normalize_phone_numb):
        return f"+38{normalize_phone_numb}"
    else:
        return f"+{normalize_phone_numb}"


raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
