import astronomy as astr

def F(m):
    def lbToKg(pnds):
        return pnds * 0.45359237

    myWeight = lbToKg(m)
    print(myWeight)
    #TODO 4
    return (astr.gravitationalConstant * myWeight * astr.earthMass) / ((astr.earthDiameter/2)**2)
    
print("{0:.2f} Newtons.".format(F(143.3)))