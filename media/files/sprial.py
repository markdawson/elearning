i = 0
def spiral(a, b):
    global i
    #print('a is ', a)
    #print('b is', b)
    #print()
    if a >= 1000 and b >= 1000:
        return a, b, i
    while a > b:
        b += 1
        #print('a is', a)
        #print('b is', b)
        #print()
    #print('enter loop')
    i += 1
    return spiral(b+1, a)

def spiral_unsafe(a, b):
    while a > b:
        b += 1
    return spiral_unsafe(b+1, a)

def spi(a, b):
    global i
    i = 0
    return spiral(a, b)
    
