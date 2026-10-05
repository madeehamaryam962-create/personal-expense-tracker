# Personal Expense Tracker
# Beginner Python Project

print("===================================")
print("       PERSONAL EXPENSE TRACKER")
print("===================================")

# Get user details
name = input("Enter your name: ")
income = float(input("Enter your monthly income: "))

# Get expenses
food = float(input("Enter your food expense: "))
travel = float(input("Enter your travel expense: "))
shopping = float(input("Enter your shopping expense: "))

# Calculate total expense
total_expense = food + travel + shopping

# Calculate savings
savings = income - total_expense

# Calculate saving percentage
saving_percentage = (savings / income) * 100

# Make sure percentage is between 0 and 100
score = max(0, min(100, saving_percentage))

# Display report
print("\n===================================")
print("        MONTHLY EXPENSE REPORT")
print("===================================")

print("Name:", name)
print("Monthly Income: ₹", income)
print("Food Expense: ₹", food)
print("Travel Expense: ₹", travel)
print("Shopping Expense: ₹", shopping)

print("-----------------------------------")
print("Total Expense: ₹", total_expense)
print("Remaining Savings: ₹", savings)

# Budget warning
if total_expense > income * 0.5:
    print("⚠️ Warning: Your expenses are high!")
else:
    print("✅ You are within your budget.")

# Find highest expense
if food >= travel and food >= shopping:
    print("Highest Expense: Food")
    print("Amount: ₹", food)

elif travel >= food and travel >= shopping:
    print("Highest Expense: Travel")
    print("Amount: ₹", travel)

else:
    print("Highest Expense: Shopping")
    print("Amount: ₹", shopping)

# Saving percentage
print("Saving Percentage:", round(saving_percentage, 2), "%")

# Financial health score
print("Financial Health Score:", round(score, 2), "/ 100")

# Final advice
if saving_percentage >= 30:
    print("💚 Excellent financial health!")
elif saving_percentage >= 20:
    print("👍 Good financial health.")
elif saving_percentage >= 10:
    print("⚠️ Try to increase your savings.")
else:
    print("🔴 Your savings are low. Review your expenses.")

print("===================================")
print("        Thank you for using it!")
print("===================================")