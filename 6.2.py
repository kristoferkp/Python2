def paarissumma(n):
    
    if n < 0:
        return False
    
    if n % 2 != 0:
        n -= 1
       
    summa = 0
    for i in range(0, n, 2):
        summa += n
        n -= 2
        
    return summa
        
print(paarissumma(100))