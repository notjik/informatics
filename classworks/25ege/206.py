######206
##a =[]
##for x1 in range(0,10):
##    for x2 in range(0,10):
##        x='1'+str(x1)+'34567'+str(x2)+'9'
##        x = int(x)
##        if x% 17 ==0:
##            a.append(x)
##a.sort()
##for x in a:
##    print(x,x//17)

######207
##from itertools import product
##a=['']
##for x in range(2):
##    a+= [''.join(y) for y in product('0123456789',repeat = x+1)]
##print(a)
##b=[]
##for x2 in range(0,10):
##    for x1 in a:
##        x = int ('123' + x1 + '567' + str(x2))
##        if x % 169 == 0:
##            b.append(x)
##b.sort()
##
##for g in b:
##    print(g,g//169)
        
######208
##from itertools import product
##b=['']
##for x in range(2):
##    b+=[''.join(y) for y in product('0123456789',repeat = x+1)]
##a=[]
##for x1 in b:
##        for x2 in b:
##            x = int('12'+ x2 + '45'+ x1)
##            if x % 51 ==0 and x < 10**6:
##                a.append(x)
##a.sort()
##for g in a:
##        print(g,g//51)

########211
##from itertools import product
##a=[]
##
##for g1 in range(16):
##    x1 = hex(g1)[2:]
##    for g2 in range(16):
##        x2= hex(g2)[2:]
##        x = int('1' + x1 + 'DED' + x2 +'CED',16)
##        if x % 121 ==0:
##            a.append(x)
##a.sort()
##for g in a:
##    print(g, g // 121)



#######212
##from itertools import product
##b=[]
##for x1 in range(16):
##    for x2 in range(16):
##        x=int('1' + hex(x1)[2:]+ 'DED' + hex(x2)[2:]+'BABA',16 )
##        if x % int('BA',16) ==0:
##            b.append(x)
##b.sort(reverse=True)
##for i in b:
##    print(i,i//int('BA',16))


#257
#123*НЧ56 
##from itertools import product
##l=['']
##for x in range(2):
##    l+=[''.join(y) for y in product('0123456789',repeat = x+1)]
##ch = ['0','2','4','6','8']
##nch = ['1','3','5','7','9']
##a=[]
##for x in ch:
##    for x1 in nch:
##        for x3 in l:
##            y= int('123' + x3 + x1 + x + '56')
##            if y< 10**8 and y % 206==0:
##                a.append(y)
##a.sort()
##for g in a:
##    print(g,g//206)

##258
####1ЧНЧНЧН
##ch = ['0','2','4','6','8']
##nch = ['1','3','5','7','9']
##a=[]
##for x in ch:
##    for x1 in nch:
##        for x2 in ch:
##            for x3 in nch:
##                for x4 in ch:
##                    for x5 in nch:
##                        y = int('1' + x + x1+ x2 + x3 + x4 + x5)
##                        if y < 10**7 and y%4023==0:
##                            a.append(y)
##for g in a:
##    print(g,g//4023)

#20
##def f(x):
##    a=[]
##    i=1
##    while i*i<=x:
##        if i*i ==x:
##            append(i)
##        elif x%i==0:
##            a+=[i,x//i]
##        i+=1
##    a.sort()
##    return a
##d=[]
##for i in range(100806,100951):
##    if len(f(i)) == 6:
##        print (f(i))

#42
##def f(x):
##    a=[]
##    i = 1
##    while i*i<=x:
##        if x % i==x:
##            a.append(i)
##        elif x%i ==0:
##            a+=[i,x//i]
##        i+=1
##    a.sort()
##    return a
##for i in range(4202865,4202924):
##    if len(f(i)) == 2:
##        print (i)

##70
##def f(x):
##    a=[1]
##    i = 2
##    while i*i<=x:
##        if x % i==x:
##            a.append(i)
##        elif x%i ==0:
##            a+=[i,x//i]
##        i+=1
##    a.sort()
##    return a
##for i in range(2,10001):
##    r=f(i)
##    if sum(r) == i:
##        print(sum(r),len(r))


##84
##def f(x):
##    sum1=0
##    a=list(map(int,str(x)))
##    if sum(a) % 14 ==0:
##        return sum(a)
##    else:
##        return False
##def f1(x):
##    sum2=1
##    a=list(map(int,str(x)))
##    for i in range(len(a)):
##        sum2 *= a[i]
##    if sum2 % 18 == 0:
##        return sum2
##    else:
##        return False
##
##for i in range(87921,88188):
##    if f(i) != False and f1(i) != False:
##        print(f(i),f1(i))
##        
        
