# Author: Jake Trissel
# Github Username: trisselj
# Date: 06/26/2024
# Description: Outputs how many of each type of coin would represent that amount with the fewest total number of coins.

# Giving values to change
Quarter = 25
Dime = 10
Nickel = 5
Penny = 1

# Initial input
ChangeString = input("Enter the amount of change you have so long as it is less than a dollar")

#From String to Float
Change = float(ChangeString)

# Calculating
num_quarters = Change // Quarter
Change %= Quarter
num_dimes = Change // Dime
Change %= Dime
num_nickels = Change // Nickel
Change %= Nickel
num_pennies = Change

#Printing of amounts
print("Your change in coins will be:")
print("Quarters: " + str(num_quarters))
print("Dimes: " + str(num_dimes))
print("Nickels: " + str(num_nickels))
print("Pennies: " + str(num_pennies))