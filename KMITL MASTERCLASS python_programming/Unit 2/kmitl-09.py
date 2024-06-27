# ATM MACHINE PRACTICE

x = int(input("How much would you like to withdraw?: "))

B1000 = x // 1000
remaining_after_1000 = x % 1000

B500 = remaining_after_1000 // 500
remaining_after_500 = remaining_after_1000 % 500

B100 = remaining_after_500 // 100

result = f"You need {B1000} bills of 1000, {B500} bills of 500, and {B100} bills of 100."

print(result)
