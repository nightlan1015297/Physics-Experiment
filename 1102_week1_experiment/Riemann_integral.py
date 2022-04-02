# implement a function that perform integration using Riemann integral

def integrate(f, a, b, n):
    """
    integrate the function f from a to b using n rectangles
    """
    h = (b - a) / n
    I = 0.0
    for i in range(n):
        I += f(a + i * h)
    return h * I