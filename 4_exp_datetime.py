#%% 
from datetime import datetime, date, timedelta

#%% Define the date of your birthday
my_birthday = date(1990, 4, 1)

#%% getting the month and day of my birthday
day_birthday = my_birthday.strftime("%A")
print(f"I was born on a {day_birthday}")

# %% days until my birthday
next_birthday = date(2024, 4, 1)
current_date = date.today()
days_difference = next_birthday - current_date
number_of_days = days_difference.days
print(f"Only {number_of_days} days until my next birthday.")

# %% from string to date
date_str =  "2023-05-25"
date_date = datetime.strptime(date_str, "%Y-%m-%d")
date_date

# %%
