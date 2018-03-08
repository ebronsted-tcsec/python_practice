import sys

# def moon_weight(initial_weight, weight_factor, years):
#     for years in range(1, years + 1):
#         initial_weight = initial_weight + 1
#         X_m = initial_weight * weight_factor
#         print("year {}: your weight on the moon is {}".format(years,X_m))

# moon_weight(90, 0.25, 5)

def moon_weight():
    initial_weight = int(input("Please enter your current Earth weight"))
    weight_factor = input("PLease enter the amount your weight might increase each year")
    years = int(input("Please enter the number of years"))
    for year in range(1, years + 1):
        initial_weight = initial_weight + 1
        X_m = initial_weight * weight_factor
        print("year {}: your weight on the moon is {}".format(year,X_m))
moon_weight()
