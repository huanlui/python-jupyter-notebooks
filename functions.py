def max_of_three(a,b,c):
    max = a
    if b > max:
        max = b
    if c > max:
        max = c
    
    print(max)
    
    return max

def max_of_three_version_ma(a,b,c):
    max = a;
    for numero in [b,c]:
        if(numero > max):
            max = numero
    
    print(max)
    return max
