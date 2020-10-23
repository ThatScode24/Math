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



