#DATA makes strings easier to type
Ap,Bp,Op,ABp = "A+","B+","O+","AB+"
An,Bn,On,ABn = "A-","B-","O-","AB-"

#INPUT Blood types x can receive from y
#OUTPUT Boolean
def receiveFrom(x,y):
    #TO DO:IMPLEMENT CODE
    if x == An:
        if y == An or y == On:
            return True
        else:
            return False

    if x == Ap:
        if y == Ap or y == An or y == On or y == Op:
            return True
        else:
            return False

    if x == Bn:
        if y == Bn or y == On:
            return True
        else:
            return False

    if x == Bp:
        if y == Bn or y == Bp or y == On or y == Op:
            return True
        else:
            return False

    if x == ABn:
        if y == An or y == Bn or y == ABn or y == On:
            return True
        else:
            return False

    if x == ABp:
        return True

    if x == On:
        if y == On:
            return True
        else:
            return False

    if x == Op:
        if y == On or y == Op:
            return True
        else:
            return False

#INPUT Blood types x can donate to y
#OUTPUT Boolean
def donateTo(x,y):
    if x == An:
        if y == Ap or y == An or y == ABn or y == ABp:
            return True
        else:
            return False

    if x == Ap:
        if y == Ap or y == Bp:
            return True
        else:
            return False

    if x == Bn:
        if y == Bp or y == Bn or y == ABn or y == ABp:
            return True
        else:
            return False

    if x == Bp:
        if y == Bp or y == ABp:
            return True
        else:
            return False

    if x == ABn:
        if y == ABn or y == ABp:
            return True
        else:
            return False

    if x == ABp:
        if y == ABp:
            return True
        else:
            return False

    if x == On:
        return True

    if x == Op:
        if y == Ap or y == Bp or y == ABp or y == Op:
            return True
        else:
            return False

x = [Ap,Bp,Op,ABp, An,Bn,On,ABn]

for i in x:
    print(i," donate to ",end="")
    for j in x:
        if donateTo(i,j):
            print(j," ",end="")
    print()
print()

for i in x:
    print(i," receive from ", end="")
    for j in x:
        if receiveFrom(i,j):
            print(j, " ", end="")
    print()
__name__ == "__main__"