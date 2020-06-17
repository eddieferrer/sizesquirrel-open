import re
from backend import app, db
from backend.emails import send_email
from collections import Counter, defaultdict

from backend.models import User

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.dates import date2num


def plot_user_registrations():
    datetimes = User.query.with_entities(
        User.date_created).order_by("date_created").all()
    datetimes = [r for r, in datetimes]

    dates = map(lambda d: d.date(), datetimes)

    # Get some auxilliary values
    min_date = int(date2num(dates[0]))
    max_date = int(date2num(dates[-1]))
    days = int(max_date - min_date + 1)
    # Initialize X and Y axes
    x = np.arange(min_date, max_date + 1)
    y = np.zeros(days)

    # Iterate over dates, increase registration array
    for date in dates:
        index = int(date2num(date) - min_date)
        y[index] += 1
    y_sum = np.cumsum(y)

    # Plot
    plt.plot_date(x, y_sum, xdate=True, ydate=False,
                  ls='-', ms=0, color='#16171E')
    plt.fill_between(x, 0, y_sum, facecolor='#D0F3FF')
    plt.title('Registered Users')
    plt.rc('font', size=8)
    plt.savefig('other/users.png', dpi=200)
