# modules to be used
from matplotlib import pyplot as plt
import numpy as np
import csv

# data
filename  = "IHME_USA_LIFE_EXPECTANCY_1985_2010.csv"

def worst_county(year): 
    # find the worst_county 
    with open('Life/IHME_USA_LIFE_EXPECTANCY_1985_2010.csv') as csvfile:
        spamreader = list(csv.reader(csvfile, delimiter=","))[1:]
        state = ''
        county = ''
        women_worst = 1000
        men_worst = 1000
        for row in spamreader:
            if(eval(row[4]) < women_worst and eval(row[7]) < men_worst and eval(row[3]) == year):
                women_worst = eval(row[4])
                men_worst = eval(row[7])
                county = row[1]
                state = row[0]
        print(state, county, women_worst, men_worst, year)
    return (state,county) 

def plotdata(state,county):
    # Plot data of the worst county
    with open('Life/IHME_USA_LIFE_EXPECTANCY_1985_2010.csv') as csvfile:
        fstate = {}
        fnation = {}
        fcounty = {}
        mstate = {}
        mnation = {}
        mcounty = {}
        spamreader = list(csv.reader(csvfile, delimiter=","))[1:]
        for row in spamreader:
            if(row[0] == state and row[1] == county):
                fstate[eval(row[3])] = eval(row[6])
                fnation[eval(row[3])] = eval(row[5])
                fcounty[eval(row[3])] = eval(row[4])
                mstate[eval(row[3])] = eval(row[9])
                mnation[eval(row[3])] = eval(row[8])
                mcounty[eval(row[3])] = eval(row[7])

        # Matplotlib stuff
        
        # plot data 
        plt.plot(list(fcounty.keys()), list(fcounty.values()), label = 'F-County')
        plt.plot(list(fstate.keys()), list(fstate.values()), label = 'F-State')
        plt.plot(list(fnation.keys()), list(fnation.values()), label = 'F-Nation')
        plt.plot(list(mcounty.keys()), list(mcounty.values()), label = 'M-County')
        plt.plot(list(mstate.keys()), list(mstate.values()), label = 'M-State')
        plt.plot(list(mnation.keys()), list(mnation.values()), label = 'M-Nation')

        # Readability
        plt.title('Men and women Life Expectancy of {0}, {1}'.format(county, state))
        plt.ylabel('Life Expectancy(years)')
        plt.xlabel('Time(year)')

        # Legend Stuff
        plt.legend()

        # Save to PNG
        # plt.savefig('Life/' + state + '_' + county + '.png')
        
        plt.show()

        
    
if __name__ == "__main__": 
    state,county =  worst_county(2010)  
    plotdata(state,county)