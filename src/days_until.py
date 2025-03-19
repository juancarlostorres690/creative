# List of days in each month for 2025 (non-leap year)
MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def get_day_of_year(month, day):
    """Returns the absolute day number of the year for a given date."""
    return sum(MONTH_DAYS[:month - 1]) + day

def days_until_birthday(today_month, today_day, birth_month, birth_day):
    """Calculates the number of days until the next birthday."""
    today_day_of_year = get_day_of_year(today_month, today_day)
    birthday_day_of_year = get_day_of_year(birth_month, birth_day)

    if birthday_day_of_year < today_day_of_year:
        # If birthday has passed, count days until next year's birthday
        return (365 - today_day_of_year) + birthday_day_of_year
    return birthday_day_of_year - today_day_of_year

def get_valid_input(prompt, min_val, max_val):
    """Prompts user for a valid integer input within a given range."""
    while True:
        try:
            value = int(input(f"{prompt} ({min_val}-{max_val}): "))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"Please enter a number between {min_val} and {max_val}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Set the current year to 2025
CURRENT_YEAR = 2025

# Get today's date from user
print("Enter today's date:")
today_month = get_valid_input("Month", 1, 12)
today_day = get_valid_input("Day", 1, MONTH_DAYS[today_month - 1])

# Get user's birthday
print("Enter your birthday:")
birth_month = get_valid_input("Month", 1, 12)
birth_day = get_valid_input("Day", 1, MONTH_DAYS[birth_month - 1])

# Compute values
today_day_of_year = get_day_of_year(today_month, today_day)
birthday_day_of_year = get_day_of_year(birth_month, birth_day)
days_until = days_until_birthday(today_month, today_day, birth_month, birth_day)

# Output results
print(f"Today's absolute day of the year: {today_day_of_year}")
print(f"Your birthday's absolute day of the year: {birthday_day_of_year}")

if days_until == 0:
    print("🎉 Happy Birthday! 🎉")
elif days_until == 1:
    print("Your birthday is tomorrow!")
else:
    print(f"There are {days_until} days until your next birthday.")

print("Did you know that on September 7, 1964, American rapper Eazy-E of N.W.A was born?")
