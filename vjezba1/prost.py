def prost_ili_ne(broj):
    i=2
    while i<broj/2:
        if broj%i==0:
         return False
        i=i+1
        return True

print(prost_ili_ne(13))