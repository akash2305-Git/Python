x = int(input('Enter a number'))
y = int(input('Enter a number'))
z = int(input('Enter a number'))
n = int(input('Enter a number'))
for a in range(0,x):
    print(a,0,0)
    for b in range(0,y):
        print([0,b+1,0])
        for c in range(0,z):
            print([0,0,c+1])
            if a+b+c !=n:
                print([a+1,b+1,c+1])
            else:
                print()
            

            
            
           