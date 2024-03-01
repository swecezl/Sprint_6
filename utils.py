import datetime


def get_date_today():
    return datetime.date.today().strftime('%d.%m.%Y')


def get_date_tomorrow():
    return (datetime.date.today() + datetime.timedelta(days=1)).strftime('%d.%m.%Y')
