from datetime import datetime as dt
from decimal import Decimal
from random import randint
from random import choice
from custom_module import generate_time_travel_message

current_time = dt.today().year
# Used today().year to retrieve just the current year to be able to use this code in any year, not just 2024.
# print(current_time)

base_cost = Decimal('10.75')
# I set the base_cost to a random cost of 10.75.
current_year = Decimal(current_time)

# print(current_year)

random_year = randint(int(current_year), 10000)
# I generated a random year between the current year and a settled year in the future and used int() to convert
# the variable current_year to an integer since randint requires integers as inputs.

cost_multiplier = abs(random_year - current_year)

time_travel_cost = base_cost * cost_multiplier
# Multiplied base cost and cost multiplier to get a cost proportional to the number of years traveled.

final_cost = round(time_travel_cost, 2)
# I rounded the final cost to two decimals.

destinations = ['France', 'Italy', 'Hawaii', 'Australia', 'Denmark', 'Spain', 'Mars']

random_destination = choice(destinations)

print(generate_time_travel_message(random_year, random_destination, final_cost))
