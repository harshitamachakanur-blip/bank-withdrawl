import sys
if(sys.argv)==3:
    script_name=sys.argv[0]
    amount=sys.argv[1]
    withdraw=sys.argv[2]
    print("User given data")
else:
    script_name=sys.argv[0]
    amount=10000
    withdraw=2000
    print("Default values")
balance=amount-withdraw
print("Script_name:",script_name)
print("Amount:",amount)
print("Withdraw:",withdraw)
print("Balance:",balance)