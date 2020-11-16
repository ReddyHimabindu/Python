n1=float(input('enter the number: '))
n2=float(input('enter another number: '))
op=input('enter the any character from the given list "+,-,*,/,%"' )
if op=="+":
    sum=n1+n2
    print('sum=',sum)              
elif op=="-":
    if n1>n2:                  
        sub=n1+n2
        print( 'sub =',sub)
    else:
        sub=n2-n1
        print('sub=',sub)
elif op=="*":
    m=n1*n2
    print('multiply=',m)
elif op=="/":
    if n1==0:
        print("we can't divide a number with zero")
    else:
        d=n1/n2
        print("division =",d)
elif op=="%":
    mo=n1%n2
    print("modulus=",mo)
else:
    print("plz enter the character given in the list ")