import math
def gaborFilter(normalizedImage):
    thetaNot=45
    alpha=40
    beta=40
    omega=25
    rNot=40
    str=""
    str1=""
    for rho in range(0,41):
        for fi in range(0,360):
            real = normalizedImage[rho][fi] * (math.cos(omega * (thetaNot - fi) * 3.14 / 180) * math.cosh((
                (math.pow(((thetaNot - fi) / beta), 2)) - (math.pow(((rNot - rho) / alpha), 2))) * 3.14 / 180) + (
                                                           (math.sin(omega * (thetaNot - fi))) * math.sinh((
                                                       (math.pow(((thetaNot - fi) / beta), 2)) + (
                                                       math.pow(((rNot - rho) / alpha), 2))) * 3.14 / 180)))
            imaginary = normalizedImage[rho][fi] * (math.cos(omega * (thetaNot - fi) * 3.14 / 180) * math.sinh((
                (math.pow(((thetaNot - fi) / beta), 2)) + (math.pow(((rNot - rho) / alpha), 2))) * 3.14 / 180) - (
                                                           (math.sin(omega * (thetaNot - fi))) * math.cosh((
                                                       (math.pow(((thetaNot - fi) / beta), 2)) - (
                                                       math.pow(((rNot - rho) / alpha), 2))) * 3.14 / 180)))
            if(real>=0):
                str1="1"
            else:
                str1="0"
            str=str+str1

            if(imaginary>=0):
                str1="1"
            else:
                str1="0"
            str=str+str1
    print(str)




