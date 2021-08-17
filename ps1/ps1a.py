r = 0.04
current_savings = 0
portion_down_payment = 0.25  # Portion of house to be saved

if __name__ == '__main__':
    annual_salary = int(input("Enter your annual salary: "))
    portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
    total_cost = int(input("Enter the cost of your dream home: "))

    amount_to_save = total_cost * portion_down_payment
    monthly_savings = annual_salary / 12 * portion_saved

    i = 0
    while current_savings < amount_to_save:
        i += 1
        current_savings += monthly_savings + current_savings * r / 12

    print(f"Number of months: {i}")