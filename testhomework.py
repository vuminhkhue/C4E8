while True:
    clothes = ["jeans","T-shirt","jacket","suit","bra"]
    st = input("welcome, what do you want?")
    st= st.upper()
    if st == "C":
        new_clothes= input("new item:")
        clothes.append(new_clothes)
        for j in range(len(clothes)):
               print(clothes[j]," ",end='')

        
    elif st=="R":
        for i in range(len(clothes)):
            print(clothes[i]," ",end='')

            
    elif st=="U":
        n= int(input("enter index, 0/1/2/3/4:"))
        if n >= 5 :
            print("no infomation")
        else:
           x= input("update?")
           clothes[n]=x
           for c in range(len(clothes)):
                print(clothes[c]," ",end='')

    
    elif st=="D":
        m= int(input("enter index, 0/1/2/3/4:"))
        clothes.remove(clothes[m])
        for p in range(len(clothes)):
                print(clothes[p]," ",end='')
        print()

        
    elif st=="S":
        a= int(input("enter index, 0/1/2/3/4:")) 
        print(clothes[a])
        
