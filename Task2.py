def collatzmaxlength(m, collatzmax):
     
    if m in collatzmax:
        return collatzmax[m]
     
    if(m == 1):
        collatzmax[m] = 1
 
    elif(m % 2 == 0):
        collatzmax[m] \
        = 1 \
           + collatzmaxlength(m//2, collatzmax)
 

    else:
        collatzmax[m] \
        = 1 \
          + collatzmaxlength(3 * m + 1, collatzmax)
     
    return collatzmax[m]
 
def collatzmax(m):
    
    collatzmax = {}
     
    collatzmaxlength(m, collatzmax)
 
    
    num, l =-1, 0
     
    for k in range(1, m):
         
        
        if k not in collatzmax:
            collatzmaxlength(k, collatzmax)
         
        max_value = collatzmax[k]
        if l < max_value:
            l = max_value
            num = k
     
    
    return (num, l)
 
print (collatzmax(10))
