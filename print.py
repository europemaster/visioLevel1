water_blood = 0.806 #constant
body_water = 0.58 # male 0.58
body_water_w = 0.49 # female 0.58
metabolic_constant = 0.015 # male 0.015
metabolic_constant_w = 0.017 # female 0.015
to_pm = 10 # converts to permillage
ebac = None

gender = input("Please input gender:")
standard_drink = int(input ("How many drinks?" ))
weight = int(input("Input your weight" ))
drinking_periods = int(input("How long have you beedn drinking?" ))

if gender == 'male':
    ebac=((0.806*standard_drink*1.2)/(body_water*weight)-metabolic_constant*drinking_periods)*to_pm
    print("Your alcohol is "+str(ebac))
elif gender == "female":
    ebac = ((0.806 * standard_drink * 1.2) / (body_water_w * weight) - metabolic_constant_w * drinking_periods) * to_pm
    print("Your alcohol is " + str(ebac))
else:
    print("Not a gender")