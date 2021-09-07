##Future value (FV)
## What would be the FV, if I have $1000 with me now and I will be investing it for 1 year, at an annual return of 5%?

PV = 1000
r = 0.05
n = 1
​
FV = PV * ((1+r) ** n) # Formula for calculating Future Value
​
print (FV)
1050.0
Present value (PV)
What would be the PV, if I have to discount $1050 at a 5% annual rate for a period of 1 year?

FV = 1050
r = 0.05
n = 1
​
PV = FV / ((1 + r) ** n) # Formula for calculating Present Value
​
print (PV)
1000.0
Compounding
Assume that the 5% annual interest rate bond makes semiannual payments. That is, for an investment of $1000, you will get 25 dollars, after the first 6 months and another 25 dollars after 1 year. The annual rate of interest is 5%. What would be the FV, if I hold the bond for 1 year?

PV = 1000
r = 0.05
n = 2 # number of periods = 2 since bond makes semiannual payments
t = 1 # number of years
​
FV = PV * ((1+(r/n)) ** (n*t)) # Formula for compounding
​
print (FV)
1050.625
Annuity payments
What would be the annual periodic saving amount, if you want a lump sum of $9476.96 at the end of 3 years? The rate of return is 10%? (Assuming the first payment is made at the start of each year).

(This is one of the required calculation from 'PDF: TVM Applications' unit)

r = 0.1
n = 3
PV = 0
FV = 9476.96
​
AP = (FV * r) / (((1 + r) ** n - 1)*(1+r)) # Formula for Annuity payments, given Future Value
​
print (AP)
2602.8453721505043
What would be the PV, given a cash outflow of $2500 for a period of 5 years and rate of return being 10%?

(This is one of the required calculation from 'PDF: TVM Applications' unit)

r = 0.1
n = 5
AP = 2500
​
PV = (AP * (1 - ((1 + r) ** -n))) / r # Formula for PV, given Annuity payments
​
print (PV)
9476.966923521126
What would be the PV, given a cash outflow of $30,000 for a period of 45 years and rate of return being 8%?

(This is one of the required calculation from 'PDF: TVM Applications' unit)

r = 0.08
n = 45
AP1 = 30000
​
PV = (AP1 * (1 - ((1 + r) ** -n))) / r # Formula for PV, given Annuity payments
​
print (PV)
363252.0450945144
What would be the annual saving amount (AP), if you want to save a lump sum of $363252.045 in 25 years and rate of return being 15%?

(This is one of the required calculation from 'PDF: TVM Applications' unit)

r = 0.15
n = 25
PV = 0
FV = 363252.045095
​
AP = (FV * r) / (((1 + r) ** n - 1)*(1+r)) # Formula to calculate Annuity Payments, given FV
​
#AP = (r * PV) / (1 - ((1 + r) ** -n)) # Formula to calculate Annuity Payments, given PV
​
print (AP)
1484.4065248166885
