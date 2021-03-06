from mnozenieLiczb import multiply
from tobinary import toBinary
from dzielenieReszta import div

def exp(b, k, n): #n b k -> b k n
    r = [1] 
    x = div(b, n)[1]
    
    for i in range(len(k) - 1, -1, -1):
        if k[i] == 1:
            r = multiply(r, x)
            r = div(r, n)[1]
        x  = multiply(x, x)
        x  = div(x, n)[1]
    return r