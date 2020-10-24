__author__ = "miha_focsa"

from math import sqrt

nums = [9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900, 961, 1024, 1089, 1156, 1225, 1296, 1396, 1444, 1521, 1600]
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

def quadr(a, b, c):
    
    
    sqr_b = b * b
    delta = sqr_b - 4*a*c
    refr_b = -(b)
    double_a = 2 * a
    
    if delta > 0:
        
        upper_v1 = refr_b - sqrt(delta) 
        upper_v2 = refr_b + sqrt(delta)
        
        
        fullExpr_v1 = float(upper_v1 / double_a)
        fullExpr_v2 = float(upper_v2 / double_a)

        return f"{fullExpr_v1} and {fullExpr_v2}"

    if delta == 0:
        expr = float(refr_b / double_a)
        
        return expr 

    if delta < 0:
        
        return f"The delta is negative (Δ = {delta} so Δ < 0). Therefore, there are no mathematical solutions possible. S = ø"



def spl(root):
    foundSolution = False
    for num in nums:
        if root == num:
            print(str(int(sqrt(num))))
            foundSolution = True
            break
    else:
        for prime in primes:
            if root % prime == 0:
                r = root / prime
                s = sqrt(r)
                items = str(s).split(".")
                if foundSolution == True:
                    pass
                else:
                    if len(str(float(items[1]))) > 3:
                        pass
                    else:
                        if str(float(items[1])) == '0.0':
                            mod_s = int(s)
                            print(str(f"{mod_s}√{prime}"))
                            foundSolution = True

