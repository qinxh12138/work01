import  time
def zsq(f):
    def fun(*args):

        a=time.time()
        f(*args)
        b=time.time()
        print(b-a)
    return fun
@zsq
def f(a,b,c):
    sum=0
    for i in range(a,b,c):
        sum+=i

f(2,111111111,2)