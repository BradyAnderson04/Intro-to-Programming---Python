one = int(input("Do you have adominal pain 1/0: "))
two = int(input("Do you have nausea 1/0: "))
three = int(input("Do you have vomiting 1/0: "))
four = int(input("Do you have fever 1/0: "))
five = int(input("Do you have loss of appetite 1/0: "))
sum = one + two + three + four + five
if(sum >= 3):
    print( 'Appendicitis')
else:
    print('No Appendicitis')