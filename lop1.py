starting_value=int(input("Enter your starting value: "))
ending_value=int(input("Enter your ending value: "))
for j in range(starting_value,ending_value+1):
    prime=True
    for i in range(2,j):
        if (j % i==0):
            prime=False
            break
    if prime==True:
        print(j,end=" ")