def unmarriedTax(income):
#TO DO: IMPLEMENT FUNCTION
	if(income < 9701):
		return income * .10
	elif(income >= 9701 and income < 39476):
		return income * .12
	elif(income >= 39476 and income < 84201):
		return income * .22
	elif(income >= 84201 and income < 160276):
		return income * .24
	elif(income >= 160276 and income < 204101):
		return income * .32
	elif(income >= 204101 and income < 510301):
		return income * .35
	else:
		return income * .37


# Finish this function
# Calculates the taxes a married person owes for 2019
# Input Parameters: amount of income in USD income
# Return Value: amount taxes owed (USD)
def marriedTax(income):
#TO DO: IMPLMEMENT FUNCTION
	if(income < 19401):
		return income * .10
	elif(income >= 19401 and income < 78951):
		return income * .12
	elif(income >= 78951 and income < 168401):
		return income * .22
	elif(income >= 168401 and income < 321451):
		return income * .24
	elif(income >= 321451 and income < 408201):
		return income * .32
	elif(income >= 408201 and income < 612351):
		return income * .35
	else:
		return income * .37

# Calculates the taxes an individual owes for 2019
# Input Parameters: amount of income in USD income and marital status Boolean maritalStatus
# Return Value: amount taxes owed (USD)
def tax(income, maritalStatus):
	if(maritalStatus):
		return marriedTax(income)
	else:
		return unmarriedTax(income)
		
############################
#   DATA
############################
UrsalaIncome,UrsalaMarried = 160726, True
KaiserIncome, KaiserMarried = 501000, True
ShilahIncome, ShilahMarried = 20, True

############################
#   TESTS
############################
print("Ursala owes ", tax(UrsalaIncome, UrsalaMarried))
print("Kaiser owes ", tax(KaiserIncome, KaiserMarried))
print("Shilah owes ", tax(ShilahIncome, ShilahMarried))

print()
############################
#   DATA
############################
UrsalaIncome,UrsalaMarried = 204099, False
KaiserIncome, KaiserMarried = 510310, False
ShilahIncome, ShilahMarried = 9400, False

############################
#   TESTS
############################
print("Ursala owes ", tax(UrsalaIncome, UrsalaMarried))
print("Kaiser owes ", tax(KaiserIncome, KaiserMarried))
print("Shilah owes ", tax(ShilahIncome, ShilahMarried))

__name__ == "__main__"
