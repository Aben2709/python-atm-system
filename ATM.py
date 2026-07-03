#----------- Account ATM ------------#

account = 100000
withdraw = 0
transfer = 0

#---- Check------#
while True:
	print("1. Check Bank Balance")
	print("2. Withdraw Amount")
	print("3. Check Remaining Balance")
	print("4. Transfer Amount")
	print("5. Exit")
	
	choice = int(input("Enter choice (1-5):"))
	
	if choice == 1:
		print(account)
		
	elif choice == 2:
		 withdraw = int(input("Enter Amount to withdraw:"))
		 if withdraw > account:
		 	print("Insufficient Balance!")
		 elif withdraw > 40000:
		 	print("Maximum Amount to withdraw should be less than 40,000 ")
		 elif 40000 > withdraw > 0:
		 	account -= withdraw
		 	print("Amount Withdrawn Successfully")
		 else:
		 	print("Invalid! Enter Numerical Amount Only!")
	
	elif choice == 3:
		print("remaining amount:", account)
		
	elif choice == 4:
		transfer = int(input("Enter Amount to Transfer:"))
		
		if transfer > account:
			print("Invalid! Please Enter Amount remaning in savings")
		elif transfer > 40000:
			print("Maximum Amount to Transfer Should be less than 40000")
		elif 40000 > transfer > 0:
			account -= transfer
			print("Amount Transferred Successfully")
		else:
			print("Invalid! Please Enter Numerical Amount Only")
	
	elif choice == 5:
		print("Exiting ATM! Have A nice day")
		
		break
		
	else:
		print("Invalid Choice! please enter choice (1-5):")

