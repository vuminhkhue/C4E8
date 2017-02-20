print("hello, my name is Khue and there are my ship sizes")
list_sheep =[5,7,300,90,24,50,75]
print(list_sheep)
months =3 
for m in range(months):
    max= 0
    for i in range(7):
        if list_sheep[max]< list_sheep[i]:
            max = i
                
    print("now my biggist sheep has",list_sheep[max],"let's shear it")


    list_sheep[max]=8
    print("after shearing, here is my flock")
    print(list_sheep)


    print("months", m+1)
    for  i in range(7):
        list_sheep[i] += 50
    print("one month has passed, now here is my flock")
    print(list_sheep)
total_list_sheep =0
for i in range(7):
    total_list_sheep += list_sheep[i]
print("my flock has size in total", total_list_sheep)
print("i would get", total_list_sheep,"2$= ", total_list_sheep*2)

    
