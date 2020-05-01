import math

def TSV_to_RGB(couleur, coef):

    R, G, B, A = couleur
    maximum = max(R,G,B)
    minimum = min(R,G,B)

    if maximum == minimum:
        T = 0

    elif maximum == R:
        a = (60*((G-B)/(maximum-minimum))+360)
        T = a - math.floor(a/360)*360

    elif maximum == G:
        T = 60*((B-R)/(maximum-minimum))+120

    elif maximum == B:
        T = 60*((R-G)/(maximum-minimum))+240

    if maximum == 0:
        S = 0

    else:
        S = 1-(minimum/maximum)

    V = maximum - 2.55*coef

    a = math.floor(T/60)
    t = a - math.floor(a/6)*6
    f = T/60 - t
    l = V*(1 - S)
    m = V*(1 - f*S)
    n = V*(1 - (1 - f)*S)

    if t == 0:
        dif = (R-math.floor(V), G-math.floor(n), B-math.floor(l))
        
        R = math.floor(V)
        G = math.floor(n)
        B = math.floor(l)

    elif t == 1:
        dif = (R-math.floor(m), G-math.floor(V), B-math.floor(l))
        
        R = math.floor(m)
        G = math.floor(V)
        B = math.floor(l)

    elif t == 2:
        dif = (R-math.floor(l), G-math.floor(V), B-math.floor(n))
        
        R = math.floor(l)
        G = math.floor(V)
        B = math.floor(n)

    elif t == 3:
        dif = (R-math.floor(l), G-math.floor(m), B-math.floor(V))
        
        R = math.floor(l)
        G = math.floor(m)
        B = math.floor(V)

    elif t == 4:
        dif = (R-math.floor(n), G-math.floor(l), B-math.floor(V))
        R = math.floor(n)
        G = math.floor(l)
        B = math.floor(V)

    elif t == 5:
        dif = (R-math.floor(V), G-math.floor(l), B-math.floor(m))
        R = math.floor(V)
        G = math.floor(l)
        B = math.floor(m)

    return ((R,G,B,A), dif)
