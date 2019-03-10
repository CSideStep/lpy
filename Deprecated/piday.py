from Core.numeric import *

def taylor_helper(p:float,f, steps=1000, iterations=3, offset=0.001):
    fs = [f]
    rtn = []
    for i in range(iterations): #http://math.andrej.com/2009/04/09/pythons-lambda-is-broken/comment-page-1/
        rtn.append(fs[i](p))
        def tmp(x, i=i):
            return approx_diff(fs[i], x, offset=offset)
        fs.append(tmp)
    return rtn

def develop_taylor_series(f, a, iterations=10, offset=0.001):
    th = taylor_helper(a, f, iterations=iterations, offset=offset)
    print(th)
    return lambda x: sum([(th[i]/factorial(i))*(x-a)**i for i in range(iterations)])

def get_taylor_factors(f, a, iterations=10, offset=0.001):
    th = taylor_helper(a, f, iterations=iterations, offset=offset)
    return [(th[i]/factorial(i)) for i in range(iterations)]