def picalc(n = 4000, REPL_only = False):

    ts = 0.0
    step = 1.0/n

    for i in range(n):
        x = (i - 0.5) * step
        ts += 4.0/(1.0 + x*x)

    p = ts * step
    
    pr = 'Estimated Pi: ' + str(p)
    
# Dump output to the REPL.
    print(pr)
