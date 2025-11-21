import sys

if len(sys.argv) == 3:
    script_name = sys.argv[0]
    amount = float(sys.argv[1])
    withdraw = float(sys.argv[2])
    print("User provided salary:")
else:
    script_name = sys.argv[0]
    amount=20000
    withdraw=10000
    print("No input given - using default salary:")
balance=amount-withdraw
print("Script_name:",script_name)
print("Amount:",amount)
print("Withdraw:",withdraw)
print("Balance:",balance)

