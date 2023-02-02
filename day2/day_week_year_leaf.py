## in this exercise we assume that we can live up to 90 years olds, 1 year = 365 days = 52 weeks = 12 months
currentAge = input("What your current age?")

years_leaf = 90 - int(currentAge)
months_leaf = years_leaf * 12
weeks_leaf = years_leaf * 52
days_leaf = years_leaf * 365

print("Years leaf: "+str(years_leaf) +" , weeks leaf:" + str(weeks_leaf)+" ,day leaf:"+str(days_leaf))