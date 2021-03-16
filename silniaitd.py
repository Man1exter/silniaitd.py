def silnia(x):
    if x <= 1:
        return 1
    else:
        return x * silnia(x - 1)
        
print("Silnia 1: ",silnia(1))
print("Silnia 2: ",silnia(2))
print("Silnia 4: ",silnia(4))
print("Silnia 8: ",silnia(8))
print("Silnia 10: ",silnia(10))