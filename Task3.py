def maxValue(m):
    highest = 0
    value = None
    for i in range(1, m+1):
        k = i
        sequence=list()
        while k!=1:
            if k%2==0:
                sequence.append(int(k))
                k = k//2
            else:
                sequence.append(int(k))
                k=3*k+1
        if len(sequence):
            if max(sequence)>highest:
                highest = max(sequence)
                value = i
    return f'{value} has the highest value as {highest}.'
