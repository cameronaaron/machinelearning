#!/usr/bin/env python3

import pandas as pd
#Import file
Exondata = pd.read_csv("publicspreadsheet.csv")
# Extract data
race = Exondata['Race'].value_counts()
sex = Exondata['Sex'].value_counts()
state = Exondata['State'].value_counts()
racetotal = 0
#Find total race
for x in race:
    racetotal = race + x

print(racetotal)

probrace = race / racetotal
# Find total sex
sextotal = 0

for x in sex:
    sextotal = sex + x

print(sextotal)
probsex = sex / sextotal
print(sex / sextotal)
#Find total state
statetotal = 0
for x in state:
    statetotal = state + x

print(statetotal)

probstate = state / statetotal

prob = 1
x = 0
y = 0
z = 0

for a in probrace:
    print("the race" + Exondata.Race[x])
    x = x + 1
    for b in probstate:
        print("state", Exondata.State[y])
        y = y + 1
        for c in probsex:
            print("sex", Exondata.Sex[z])
            z = z = 1

            probofcase = a * b * c
            print(probofcase)
