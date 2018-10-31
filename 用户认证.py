import  time
def zsq(f):
    def fun(*args):
        a=time.time()
        f(*args)
        b=time.time()
        print(b-a)
    return fun