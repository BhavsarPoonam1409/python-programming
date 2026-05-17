def outer(x):
    def inner(y):
        return x+y
    
    result=inner(x)
    return result

ans=outer(5)
print(ans)