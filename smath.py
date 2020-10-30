__author__ = "miha_focsa"

from math import sqrt
                                                 
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

def spl(*root):
    foundSolution = False
    primes = []
    nums = []
    start, end = 0, 100000
    sep = root[0].split('!')
    if sep[0] == '':
        root = sep[1]
        multp = None
    else:
        root = sep[1]
        multp = sep[0]
    for i in range(start, end + 1):
        if (i**(.5) == int(i**(.5))):
            nums.append(i)
    else:
        for i in range(100000):
            primes.append(i)
        else:
            for num in nums:
                if root == num:
                    foundSolution = True
                    return str(int(sqrt(num)))
                else:
                    pass
            else:
                for prime in primes:
                    if prime != 0:
                        if int(root) % int(prime) == 0:
                            r = int(root) / prime
                            s = sqrt(r)
                            items = str(s).split(".")
                            if foundSolution == True:
                                pass
                            else:
                                if len(str(float(items[1]))) > 3:
                                    pass
                                else:
                                    if multp == None:
                                        if str(float(items[1])) == '0.0':
                                            foundSolution = True
                                            mod_s = int(s)
                                            if mod_s == 1:
                                                foundSolution = True
                                                return str(f"√{prime}")
                                            else:
                                                foundSolution = True
                                                return str(f"{mod_s}√{prime}")
                                    else:
                                        if str(float(items[1])) == '0.0':
                                            foundSolution = True
                                            mod_s = int(s) * int(multp)
                                            return str(f"{mod_s}√{prime}")

                    else:
                        foundSolution = False
