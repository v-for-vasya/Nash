# Function that solves for pure strategy Nash Equilibria

def nash_eq(payoff_m):
    for x in range(len(payoff_m)):
        row=[]
        column=[]
        for i in range(len(payoff_m[x])):
            column.append(payoff_m[i][x][0])
        print column,'<column || max index at', column.index(max(column)), '|| value >',max(column)
        for i in range(len(payoff_m[x])):
            row.append(payoff_m[column.index(max(column))][i][1])
        print row,'<row || max index at', row.index(max(row)), '|| value >',max(row)
        if(row.index(max(row))==x):
            print 'Nash equilibrium found at coordinates [', column.index(max(column)),',',row.index(max(row)),']' \
            ' with values of (', max(column),',',max(row),')'


#game of chicken
nash_eq([[(0,0),(7,2)],
         [(2,7),(6,6)]])

#prisonner's dilemma
nash_eq([[(2,2),(0,3)],
         [(3,0),(1,1)]])

#stag hunt
nash_eq([[(2,2),(0,1)],
         [(1,0),(1,1)]])

#matching pennies - no pure strategy Nash Eq.
nash_eq([[(1,-1),(-1,1)],
         [(-1,1),(1,-1)]])

