def sec_smallest(n):
    sm=0
    ssm=0
    for i in n:
        if i<=sm:
            sm,ssm=i,sm
        elif i<ssm:
            ssm=i
    return ssm




numbers=[1,1,2,2,33,34,5,6,6,-1,0,-3]
print(sec_smallest(numbers))
