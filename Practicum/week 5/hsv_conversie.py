
def rgb_naar_hsv(rgb):
    r, g, b = rgb

    c_high = max(r,g,b)
    c_low = min(r,g,b)
    c_range = c_high - c_low

    V = round( ( c_high/255 ) * 255 , 1 )
    S = (c_range/c_high) * 255 if (c_high != 0) else 0

    if(c_range != 0):

        RA = (c_high-r)/c_range 
        GA = (c_high-g)/c_range
        BA = (c_high-b)/c_range

        if(r == c_high):
            HA = BA - GA
        if(g == c_high):
            HA = RA - BA + 2
        if(b == c_high):
            HA = GA - RA + 4

        h = (HA) if (HA >= 0) else HA + 6
        H = (1/6)*h*360
    else:
        S = 0.0
        H = 0.0
    
    
    return H, S, V

print(rgb_naar_hsv((18,141,255)))