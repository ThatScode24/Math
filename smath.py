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
    
    if root % 2 == 0:
        
        r = root / 2
        s= sqrt(r)

        items = str(s).split(".")

        if float(items[1]) > 2:
            pass
        else:
            print(str("{}√2 ".format(int(s))))
            foundSolution = True

    if root % 3 == 0:        
        
        r = root / 3
        s = sqrt(r)
        
        items = str(s).split(".")
        
        if float(items[1]) > 2:
            pass
        else:
            print(str("{}√3 ".format(int(s))))
            foundSolution = True
        
    if root % 4 == 0:
        
        r = root / 4
        s = sqrt(r)

        items = str(s).split(".")

        if float(items[1]) > 2:
            pass

        if root == 16:
            print(str(4))
            foundSolution = True
            pass
        else:
            if foundSolution == True:
                pass
            else:
                print(str("{}√4".format(int(s))))
                foundSolution = True

    if root % 5 == 0:

        r = root / 5
        s = sqrt(r)

        items = str(s).split(".")

        if float(items[1]) > 2:
            pass

        if root == 25:
            print(str(5))
            foundSolution = True
            pass
        else:
            if foundSolution == True:
                pass
            else:
                print(str("{}√5".format(int(s))))
                foundSolution = True

    if root % 6 == 0:
        
        r = root / 6

    if root % 7 == 0:
        isDivby7 = True
        print("Div7 True")

    if root % 8 == 0:
        isDivby8 = True
        print("Div8 True")

    if root % 9 == 0:
        isDivby9 = True
        print("Div9 True")    
    
    if root % 10 == 0:
        r = root / 5
        s = sqrt(r)



        
        
