# Generators are iterators, but you can only iterate over them once.
# It’s because they do not store all the values in memory, they generate the values on the fly

# it returns an iterator
def generator_function():
    for i in range(10):
        yield i


for item in generator_function():
    print(item)



# Fibonaci seq

def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b    

#for item in fibon(5):
#    print(item)

val = fibon(5)
print(next(val))
print(next(val))


