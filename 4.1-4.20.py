#4.1
a=float(input())
b=float(input())
if a>b:
    print(a,'больше',b,'меньше')
else:
    print(b,'больше',a,'меньше')

#4.2
import math
x=float(input())
if x>0:
    y=math.sin(x)**2
else:
    y=(1-2*math.sin(x**2))
print(y)

#4.3
import math
x=float(input())
if x>0:
    y=math.sin(x**2)
else:
    y=1+2*math.sin(x)**2
print(y)

#4.4
x=float(input())
y=float(input())
if x>4 and y>0:
    print('vo vtoruyu')
elif x<4 and y>0:
    print('v pervuyu')
else:
    print('ni v odnu iz nix')

#4.5
x=float(input())
y=float(input())
if x>0 and y>3:
    print('v pervuyu')
elif x>0 and y<3:
    print('vo vtoruyu')
else:
    print('ni v odnu iz nix')


#4.7
import math
x=float(input())
a=math.sin(x)
if a>0:
    k=x**2
else:
    k=abs(x)
if k<x:
    f=k*x
else:
    f=k+x
print(f)

#4.8
import math
x=float(input())
a=math.sin(x)
if a<0:
    k=abs(x)
else:
    k=x**2
if x<k:
    f=abs(x)
else:
    f=k*x
print(f)

#4.9
a,b=map(float,input(),split())
if a>b:
    print(a,'maks',b,'min')
else:
    print(b,'maks',a,'min')

#4.10
km=float(input())
funt=float(inpit())
km_1=funt*0,3048
if km>km_1:
    print('v km mense')
elif km_1>km:
    print('v funtax mense')
else:
    print('oni ravni')

#4.11
v1=float(input())   
v2=float(input())
v1=v1*(5/18)
if v1>v2:
    print('v km/c bolse')
elif v2>v1:
    print('v m/s bolse')
else:
    print('oni ravni')

#4.12
import math
r=float(input())
a=float(input())
s_kv=a**2
s_kr=math.pi*r*r
if s_kv>s_kr:
    print('s kvadrata bolse')
else:
    print('s kruga bolse')


#4.13
m1=float(input())
m2=float(input())
v1=float(input())
v2=float(input())
p1=m1/v1
p2=m2/v2
if p1>p2:
    print('p1 bolse')
else:
    print('p2 bolse')

#4.15-4.16
a,b,c=map(int,input().split())
d=b**2-4*a*c
if d>0:
    print('imeet')
    x1=((-b)+(d**(1/2)))/(2*a)
    x2=((-b)-(d**(1/2)))/(2*a)
    print(x1,x2)
elif d=0:
    x=((-b)+(d**(1/2)))/(2*a)
else:
    print('ne imeet')

#4.17
god_roj=int(input())
mes_roj=int(input())
god=int(input())
mes=int(input())
if mes_roj<mes:
    print(god-god_roj)
else:
    print(god-god_roj-1)

#4.18
import math
s_kv=float(input())
s_kr=float(input())
a=s_kv**(1/2)
r=(s_kr/math.pi)(1/2)
if r<a/2:
    print('круг уместится внутри квадрата.квадрат внутри круга нет')
else:
    print('круг не уместится внутри квадрата.квадрат внутри круга уместится')

#4.19
import math
s_tr=float(input())
s_kr=float(input())
r=(s_kr/math.pi)(1/2)
a=((4 * S_tr)/math.sqrt(3))(1/2)
r_vpis=(a*(3**(1/2))/6
r_opis=(a*(3**(1/2))/3
if r<=r_vpis:
    print('круг уместится в треугольнике')
else:
    print('круг не уместится в треугольнике)

if r_opis<=r:
    print('треугольник уместится в круге')
else:
    print('треугольник не уместится в круге')

#4.20




#4.99(a)
a,b=map(float,input().split())
if a>b:
    print('a bolse b')
if b>a:
    print('b bolse a')
#b??
a,b=map(float,input().split())
if a>b:
    print('a bolse b')

#4.100
a,b=map(float,input().split())
if a>b:
    print('a naib,b naim')
if b>a:
    print('b naib,a naim')

#4.101(a)
a,b,c=map(float,input().split())
if a>b and a>c:
          print('a naib')
if b>a and b>c:
          print('b naib')
if c>a and c>b:
          print('c naib')

#4.101(b)
a,b,c=map(float,input().split())
if a<b and a<c:
          print('a naim')
if b<a and b<c:
          print('b naim')
if c<a and c<b:
          print('c naim')

#4.102(a)
a,b,c,d=map(float,input().split())
if a>b and a>c and a>d:
          print('a naib')
if b>a and b>c and b>d:
          print('b naib')
if c>a and c>b and c>d:
        print('c naib')
if d>a and d>b and d>c:
          print('d naib')

#4.102(b)
a,b,c,d=map(float,input().split())
if a<b and a<c and a<d:
        print('a naim')
if b<a and b<c and b<d:
        print('b naim')
if c<a and c<b and c<d:
        print('c naim')
if d<a and d<b and d<c:
        print('d naim')
#4.103
x=float(input())
print((x*2)*(1/2))

#4.104
a,b=map(float,input().split())
a=(a*2)*(1/2)
b=(b*2)*(1/2)
print((a+b)/2)
print((a*b)(1/2))

#4.105
a,b=map(int,input().split())
if abs(a)>abs(b):
    a=a/2
print(a)

#4.106
a,b=map(int,input().split())
if b**(1/2)<a:
    b=b*5
print(b)

#4.107
a,b,c=map(int,input().split())
if a%2==0:
    print(a)
if b%2==0:
    print(b)
if c%2==0:
    print(c)


#4.108
a,b,c=map(float,input().split())
if a>0:
    print(a**2)
if b>0:
    print(b**2)
if c>0:
    print(c**2)

#4.109
a,b,c=map(float,input().split())
if a>1,6 and a<3,8:
    print(a)
if b>1,6 and b<3,8:
    print(b)
if c>1,6 and c<3,8:
    print(c)
          

 #4.110
a,b,c=map(float,input().split())
k=0
if a<0:
    k=k+1
if b<0:
    k=k+1
if c<0:
    k=k+1
print(k)



        
























          
                
                
