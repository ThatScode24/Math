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



def spl(root):
    foundSolution = False
    primes = [4, 6]
    nums = []
    start ,end = 0, 1000
    for i in range(start, end + 1):
        if (i**(.5)==  int(i**(.5))):
            nums.append(i)
    for num in range(start, end + 1):
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                primes.append(num)
    for num in nums:
        if root == num:
            return str(int(sqrt(num)))
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
                            return str(f"{mod_s}√{prime}")
                            foundSolution = True

