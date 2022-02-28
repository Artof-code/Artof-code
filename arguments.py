#Positional Arguments
def sub(a,b):
 print(a-b)
sub(100,200)

#Keyword Arguments
def wish(name,msg):
 print("hellow",name,msg)
wish(name="ashwin",msg="Good Morining")

#Default Arguments
def wish(name="guest"):
  print("hellow",name,"Good Morining")
wish("Ashwin")
wish()

#Variable Arguments
def sum(*n):
    total=00
    for n1 in n:
        total=total+1
    print("the sum=",total)
sum()
sum(10,20)

#--------------*Arg---------------

def arg_printer(a,b,*args):
    print(f'a is {a}')
    print(f'b is {b}')
    print(f'Arg is {args}')
arg_printer(3,4,10.5,3,6)# after a & b is pack all reaming arg in to a tuple

#---------------**kwarg--------------

def arg_printer(a,b,**kwarg):
    print(f'a is {a}')
    print(f'b is {b}')
    print(f'kwarg is {kwarg}')
arg_printer(3,4,parm1=5)

def display(**kwargs):
  for k,v in kwargs.items():
   print(k,"=",v)
display(n1=10,n2=20,n3=30)
display(rno=100,name="Durga",marks=70,subject="Java")





