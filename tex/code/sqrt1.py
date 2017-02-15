def NewtonRaphson(関数式, x, *args):
    F = sp.Function('F')
    NR = x - F(x) / sp.diff(F(x), x)
    
    差分計算式 = NR.subs(F(x), 関数式).doit()
    差分計算   = sp.lambdify((x, *args),
                             差分計算式)
    
    def newton_raphson(*args, x = 1, ループ回数 = 5):
        for i in range(ループ回数):
            x = 差分計算(x, *args)
        return x

    return newton_raphson
