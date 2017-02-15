def md(*args):
    s = ''
    for x in args:
        if (isinstance(x, sp.Basic)
            or isinstance(x, sp.MutableDenseMatrix)
            or isinstance(x, tuple)):
            s += sp.latex(x)
        elif isinstance(x, np.ndarray):
            s += sp.latex(sp.Matrix(x))
        elif (isinstance(x, str)): s += x
        elif (isinstance(x, int)
            or isinstance(x, float)): s += str(x)
        else: print(type(x))
    markdown(s, raw=True)
