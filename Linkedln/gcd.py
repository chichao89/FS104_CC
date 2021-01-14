#Eucidln Algorithm
# where 2 integers a and b where a > b, divide A by b , if the remainder r, 0, then stop:GCD is b, 
# otherwise set a to b, b to r , and repeat until r is 0 

def gcd(a,b):
    while(b!=0):
      temp = a
      a = b
      b = temp % b

    return a

print(gcd(20,8))
print(gcd(96,12))