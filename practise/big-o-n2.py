x=[90,11,10,20,-5,-30,-6]
sorted_x = []

def compare(x):
    while x:
        minval = x[0]
        for nextv in x[1:]:
            if nextv < minval:
                minval = nextv
        sorted_x.append(minval)
        x.pop(x.index(minval))
        
            
    return sorted_x[0]

print compare(x)
