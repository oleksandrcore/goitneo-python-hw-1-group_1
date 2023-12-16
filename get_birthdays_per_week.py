from datetime import datetime, timedelta
from collections import defaultdict

WEEKEND_DAYS = {5, 6}


def get_birthdays_per_week(users):
    birthdays_dict = defaultdict(list)
    today = datetime.today().date()

    for user in users:
        birthday = user["birthday"].date().replace(year=today.year)

        if birthday < today:
            birthday = birthday.replace(year=birthday.year + 1)

        delta_days = (birthday - today).days

        if delta_days > 7 or delta_days == 0:
            continue

        if birthday.weekday() in WEEKEND_DAYS:
            days_until_next_monday = (7 - birthday.weekday()) % 7
            birthday = birthday + timedelta(days=days_until_next_monday)

        birthdays_dict[birthday].append(user["name"])

    for date, names in sorted(birthdays_dict.items()):
        print(f"{date.strftime('%A')}: {', '.join(names)}")
