def savings_after_36_months(annual_salary,
                   portion_saved,
                   semi_annual_raise=0.07,
                   r=0.04):

    current_savings = 0

    monthly_savings = annual_salary / 12 * portion_saved

    for i in range(1,37):
        if i % 6 == 1 and i != 1:
            annual_salary *= (1 + semi_annual_raise)
            monthly_savings = annual_salary / 12 * portion_saved

        current_savings += monthly_savings + current_savings * r / 12

    return current_savings