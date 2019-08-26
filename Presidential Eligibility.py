"""
This code is to tell you whether you are eligible or not to run for U.S.
president.
This code was made by Julian
"""

ageNumber = int(input ("Age:"))
birthPlace = input ("Born in the U.S.? (Yes/No)")
yrsOfResidency = int(input ("Years of Residency:"))
if ageNumber >= 35 and birthPlace == "Yes" and yrsOfResidency >= 14:
    print ("You are eligible to run for president!")
else:
    print ("You are not eligible to run for president.")
