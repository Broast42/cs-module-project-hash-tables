# Your code here
#cache to store already computed results
cache = {}

def expensive_seq(x, y, z):
    # Your code here
    if (x,y,z) in cache:
        return cache[(x,y,z)]
    #base case if x is less than or equal to zero
    if x <= 0:
        #return the sum of y and z
        return y + z

    #if x is greter than zero
    if x > 0:
        value = expensive_seq(x-1,y+1,z) + expensive_seq(x-2,y+2,z*2) + expensive_seq(x-3,y+3,z*3)
        cache[(x,y,z)] = value
        return value
    


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    print(expensive_seq(150, 400, 800))
