
def xmax(numx):
    large = 0
    for i in range(len(numx)):
        if large> numx[i]:
            large = numx
    pass


print(xmax([1,2,3,4,5]))
