# START

# Functions
# Prompt function
def prompt(message):
    print(f"==> {message}")
# Function for handling invalid number for loan amount, APR, and duration
def invalid_number(number_str):
    try:
        float(number_str)
    except ValueError:
        return True
    return False
# Function for tossing out negative numbers
def pos_number(number_str):
    if float(number_str):
        return True
    return False

prompt("Welcome to Car Loan Calculator!")

while True:
    prompt("Please enter the loan amount in $:")
    loan_amount = input()

    if not invalid_number(loan_amount) and pos_number(loan_amount):
        loan_amount = float(loan_amount)
        break

    prompt("Please enter a positive number without other characters")

while True:
    prompt("Please enter the Annual Percentage Rate as a percentage")
    annual_percent_rate = input()

    if not (invalid_number(annual_percent_rate) and
    pos_number(annual_percent_rate)):
        annual_percent_rate = float(annual_percent_rate)
        break

    prompt("Please enter a positive number without other characters")

while True:
    prompt("Please enter the loan duration in years: ")
    loan_duration_years = input()

    if not (invalid_number(loan_duration_years) and
    pos_number(loan_duration_years)):
        loan_duration_years = float(loan_duration_years)
        break

    prompt("Please enter a positive number without other characters")

monthly_percent_rate = annual_percent_rate/12

loan_duration_months = loan_duration_years*12

if annual_percent_rate == 0:
    monthly_payment = loan_amount/loan_duration_months

else:
    monthly_payment = loan_amount * (
        monthly_percent_rate /
            (1 - (1 + monthly_percent_rate) ** (-loan_duration_months))
    )

print(f"The monthly payment amount is ${monthly_payment:.2f}")
