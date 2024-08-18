"""Write a program in Python that asks the user to enter their name, the amount of their monthly salary and the amount of the bonus they received.
The program should then print a message greeting the user by name and informing the amount of the bonus salary compared to the bonus received"""

const_bonus = 1000

# 1) The program should start by asking the user to enter their name.
name = input("Welcome! Please, insert your name: ")

# 2) Next, the program should ask the user to enter the amount of their salary. Consider that this value can be a decimal number.
sal = float(input("Please, insert your salary (monthly): "))

# 3) Then, the program should ask for the percentage of the bonus received by the user, which can also be a decimal number.
bonus = float(input("Please, insert % of your bonus received: "))

# 4) The calculation of the 2024 bonus KPI is 1000 + salary * bonus
kpi = const_bonus + (sal * bonus)

# 5) Finally, the program should print a message in the following format: "Hello [name], your bonus amount was [kpi]."
print(f"Hello {name}, your bonus amount was {kpi}.")
