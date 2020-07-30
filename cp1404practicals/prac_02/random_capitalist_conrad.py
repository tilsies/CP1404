"""
CP1404/CP5632 - Practical
Capitalist Conrad wants a stock price simulator for a volatile stock.
The price starts off at $10.00, and, at the end of every day there is
a 50% chance it increases by 0 to 10%, and
a 50% chance that it decreases by 0 to 5%.
If the price rises above $1000, or falls below $0.01, the program should end.
The price should be displayed to the nearest cent (e.g. $33.59, not $33.5918232901)
"""
import random


MAX_INCREASE = random.uniform(0,0.2)
MAX_DECREASE = random.uniform(0,0.2)
MIN_PRICE = 1.0
MAX_PRICE = 100.0
INITIAL_PRICE = 10.0
OUTPUT_FILE = "random_capitalist_conrad_output.txt"

out_file = open(OUTPUT_FILE, 'w')

price = INITIAL_PRICE
day_num = 0
print("Starting price: ${0:.2f}".format(price), file=out_file)

while price >= MIN_PRICE and price <= MAX_PRICE:
    price_change = 0
    # generate a random integer of 1 or 2
    # if it's 1, the price increases, otherwise it decreases
    if random.randint(1, 2) == 1:
        # generate a random floating-point number
        # between 0 and MAX_INCREASE
        price_change = random.uniform(0, MAX_INCREASE)
    else:
        # generate a random floating-point number
        # between negative MAX_DECREASE and 0
        price_change = random.uniform(-MAX_DECREASE, 0)

    price *= (1 + price_change)
    day_num += 1
    print("On day {0} price is: ${1:.2f}. Change of {2:.2f}%".format(day_num, price, price_change * 100), file=out_file)

out_file.close()
