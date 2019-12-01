print("-----------------------------------------------------------------------------------------------------")
print("\n")
for row in range(6):
    for col in range(7):
        a= col%3
        b= row-col
        c= row+col
        if (row ==0 and a!=0) or (row==1 and a==0) or (b==2) or (c==8):
            print ("*", end=" ")
        
        else:
            print(end="  ")
    print()


print("\n")
print ("I Love you Babe. from Binura ")
print("\n")
print ("© copyright by binura methmal 2019.")
print("\n")
print("-----------------------------------------------------------------------------------------------------")

