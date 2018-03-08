
def moon_weight(X_e, weight_factor):
    for years in range(1, 16):
        X_e = X_e + 1
        X_m = X_e * weight_factor
        print("year {}: your weight on the moon is {}".format(years,X_m))

moon_weight(100, 0.25)