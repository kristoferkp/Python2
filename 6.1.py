def alla_ules(n):
    if n < 0:
        return False
    arv = n
    for i in range(0, arv, 2):
        print(n)
        n -= 2

        #See ei tee midagi
        alla_ules(-1)
        
    print("Põhi!")

    n += 1
    
    for i in range(0, arv, 2):
        print(n)
        n += 2
       
            
