print("Electricity bill estimator")
#cents_per_kwh = float(input("Enter cents per kWh: "))
TARIFF_11 = 0.244618
TARIFF_31 = 0.136928
tariff = input("Which Tariff? 11 or 31: ")
while tariff == "11" or tariff == "31":
    if tariff == "11":
        cost_per_kwh = TARIFF_11
    else:
        cost_per_kwh = TARIFF_31
else:
    print("Invalid choice.")
    tariff = input("Which Tariff? 11 or 31: ")

daily_kwh = float(input("Enter daily use in kWh: "))
daily_cost_dollars = cost_per_kwh * daily_kwh         #(cents_per_kwh * daily_kwh) / 100
num_days = int(input("Enter number of billing days: "))
estimated_bill = daily_cost_dollars * num_days
print("Estimated bill: ${0:.2f}".format(estimated_bill))
