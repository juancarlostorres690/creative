import java.util.Scanner;

public


class BirthdayCalculator import java.util.Scanner;

public class BirthdayCalculator {

    // Days in each month for 2025 (non-leap year)
    private static final int[] MONTH_DAYS = {31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Get today's date
        System.out.println("Enter today's date:");
        int todayMonth = getValidInput(scanner, "Month", 1, 12);
        int todayDay = getValidInput(scanner, "Day", 1, getDaysInMonth(todayMonth));

        // Get user's birthday
        System.out.println("Enter your birthday:");
        int birthMonth = getValidInput(scanner, "Month", 1, 12);
        int birthDay = getValidInput(scanner, "Day", 1, getDaysInMonth(birthMonth));

        // Compute values
        int todayDayOfYear = getDayOfYear(todayMonth, todayDay);
        int birthdayDayOfYear = getDayOfYear(birthMonth, birthDay);
        int daysUntil = daysUntilBirthday(todayDayOfYear, birthdayDayOfYear);

        // Output results
        displayResults(todayDayOfYear, birthdayDayOfYear, daysUntil);
        scanner.close();
    }

    /**
     * Returns the absolute day of the year for a given date.
     */
    public static int getDayOfYear(int month, int day) {
        int days = 0;
        for (int i = 0; i < month - 1; i++) {
            days += MONTH_DAYS[i];
        }
        return days + day;
    }

    /**
     * Calculates the number of days until the next birthday.
     */
    public static int daysUntilBirthday(int todayDayOfYear, int birthdayDayOfYear) {
        if (birthdayDayOfYear < todayDayOfYear) {
            return (365 - todayDayOfYear) + birthdayDayOfYear; // Wraps around to next year
        }
        return birthdayDayOfYear - todayDayOfYear;
    }

    /**
     * Ensures user input is within a valid range.
     */
    public static int getValidInput(Scanner scanner, String prompt, int min, int max) {
        int value;
        while (true) {
            System.out.print(prompt + " (" + min + "-" + max + "): ");
            if (scanner.hasNextInt()) {
                value = scanner.nextInt();
                if (value >= min && value <= max) {
                    return value;
                }
            } else {
                scanner.next(); // Clear invalid input
            }
            System.out.println("Invalid input. Please enter a number between " + min + " and " + max + ".");
        }
    }

    /**
     * Returns the number of days in a given month for 2025.
     */
    public static int getDaysInMonth(int month) {
        return MONTH_DAYS[month - 1];
    }

    /**
     * Displays results and birthday countdown message.
     */
    public static void displayResults(int todayDayOfYear, int birthdayDayOfYear, int daysUntil) {
        System.out.println("Today's absolute day of the year: " + todayDayOfYear);
        System.out.println("Your birthday's absolute day of the year: " + birthdayDayOfYear);

        if (daysUntil == 0) {
            System.out.println("🎉 Happy Birthday! 🎉");
        } else if (daysUntil == 1) {
            System.out.println("Your birthday is tomorrow!");
        } else {
            System.out.println("There are " + daysUntil + " days until your next birthday.");
        }

        System.out.println("Did you know that on September 7, 1964, American rapper Eazy-E of N.W.A was born?");
    }
}
return days + day;
}

/ **
*Calculates
the
number
of
days
until
the
next
occurrence
of
the
given
birthday.
* /
public
static
int
daysUntilBirthday(int
todayDayOfYear, int
birthdayDayOfYear) {
if (birthdayDayOfYear < todayDayOfYear) {
return (365 - todayDayOfYear) + birthdayDayOfYear;
}
return birthdayDayOfYear - todayDayOfYear;
}

/ **
*Prompts
the
user
for input and ensures it falls within the valid range.
* /
public static int getValidInput(Scanner scanner, String prompt, int min, int max) {
int
value;
while (true) {
System.out.print(prompt + " (" + min + "-" + max + "): ");
if (scanner.hasNextInt()) {
value = scanner.nextInt();
if (value >= min & & value <= max) {
return value;
}
} else {
    scanner.next(); // Clear
invalid
input
}
System.out.println(
    "Invalid input. Please enter a number between " + min + " and " + max + ".");
}
}

/ **
*Displays
the
results
based
on
the
computed
values.
* /
public
static
void
displayResults(int
todayDayOfYear, int
birthdayDayOfYear, int
daysUntil) {
    System.out.println("Today's absolute day of the year: " + todayDayOfYear);
System.out.println(
    "Your birthday's absolute day of the year: " + birthdayDayOfYear);

if (daysUntil == 0)
{
    System.out.println("Happy Birthday!");
} else if (daysUntil == 1) {
System.out.println("Your birthday is tomorrow!");
} else {
System.out.println("There are " + daysUntil + " days until your next birthday.");
}

System.out.println("Did you know that on September 7, 1964, American rapper Eazy-E of N.W.A was born?");
}
}
