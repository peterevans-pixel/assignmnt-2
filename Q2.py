while True:
    try:
        salary = float(input("Enter annual salary: $"))
        if salary < 0:
            print("Salary cannot be negative. Please try again.")
            continue
        break
    except ValueError:
        print("Please enter the salary as a number, such as 65000.")

while True:
    try:
        score = int(input("Enter performance score (0-100): "))
        if 0 <= score <= 100:
            break
        print("Score must be between 0 and 100.")
    except ValueError:
        print("Please enter the score as a whole number, such as 85.")

if score >= 90:
    bonus_percentage = 20
elif score >= 80:
    bonus_percentage = 10
elif score >= 70:
    bonus_percentage = 5
else:
    bonus_percentage = 0

bonus_amount = salary * bonus_percentage / 100

print(f"Performance Bonus: {bonus_percentage}%")
print(f"Bonus Amount: ${bonus_amount:,.2f}")