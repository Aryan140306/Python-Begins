import math
def quadratic(a,b,c):
    d=b**2-4*a*c
    if d<0:
        print('no real roots')
    elif d==0:
        root=-b/2*a
        return root
    else:
        root1=(-b+math.sqrt(d))/(2*a)
        root2=(-b-math.sqrt(d))/(2*a)
        print('root1 is=',root1,'root2 is=',root2)  
     
a=int(input('enter no.'))
b=int(input('enter no.'))
c=int(input('enter no.'))
quadratic(a,b,c)


