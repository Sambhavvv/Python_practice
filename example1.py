



def sum_of_list(n):
    sum=0
    for i in n:
        sum=sum+i
    return sum


def sum_of_odd_numbers(n):
    
    sum_odd=0
    for i in range(0,len(n)):
        if i%2!=0:
            sum_odd=sum_odd+n[i]
    return sum_odd

def sum_of_even_numbers(n):
    
    sum_even=0
    for i in range(0,len(n)):
        if i%2==0:
            sum_even=sum_even+n[i]
    
    return sum_even


def sum_of_even(n):
    sum_even_n=0
    for i in n:
        if i%2==0:
            sum_even_n=sum_even_n+i
    return sum_even_n
def sum_of_odd(n):
    sum_odd_n=0
    for i in n:
        if i%2!=0:
            sum_odd_n=sum_odd_n+i
    return sum_odd_n


n=[1,2,3,66,3423,2311]
a=sum_of_list(n)
b=sum_of_odd_numbers(n)
c=sum_of_even_numbers(n)
d=sum_of_even(n)
e=sum_of_odd(n)
print(a)
print(b)
print(c)
print(d)
print(e)
# def largest_number(n):
#     largest=0
#     for i in range(0,leng())
