import random
from ps1 import savings_after_36_months

random.seed(123)
lower = 1
upper = 10000

total_cost = 1000000
portion_down_payment = 0.25
tot_to_save = total_cost * portion_down_payment
lower_threshold = tot_to_save - 100
upper_threshold = tot_to_save + 100

if __name__ == '__main__':
    annual_salary = int(input("Enter the starting salary: "))

    if annual_salary < 66150:
        print("It is not possible to pay the down payment in three years.")
    else:
        i = 0
        mid = (lower + upper) / 2  # Set starting value to middle of candidate values
        while True:
            i += 1

            candidate_savings_rates = mid / 10000
            est_savings = savings_after_36_months(annual_salary=annual_salary, portion_saved=candidate_savings_rates)

            if est_savings > upper_threshold:
                print(f"Savings is too high: {candidate_savings_rates}")
                upper = mid-1
            elif est_savings < lower_threshold:
                print(f"Savings is too low: {candidate_savings_rates}")
                lower = mid+1
            else:
                break

            mid = (lower + upper) / 2  # Grab new value for savings rate

        print(f"Best savings rate: {candidate_savings_rates}")
        print(f"Steps in bisection search: {i}")
