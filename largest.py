def largest(n):
    greatest=n[0]
    for i in n:
        if i>greatest:
            greatest=i
    return greatest

def smallest(n):
    smallest=n[0]
    secondsmallest=n[0]
    for i in n:
        if i<smallest:
            smallest=i
            

    return smallest


numbers=[1,2,3,4,5]
print(largest(numbers))
print(smallest(numbers))


a=100
b=200

a,b=b,a
print(a,b)
'SWAP USING 3rd variable'
c=a
a=b
b=c
print(a,b)

