"""Basico"""
for i in range(1,151):
    print (i)

"""Multiplo de 5"""
for i in range(5, 1005, 5):
    print (i)

"""Coding - dojo"""
for i in range(1, 101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Dojo")
    else:
        print(i)

"""Super suma"""
suma = 0
for i in range(0, 500001, 2):
    suma += i    
print(suma)
for i in range(2008, 0, -4):
    print(i)

"""Variables"""
lownum = 1
highnum = 400
mult = 5
for i in range(lownum, highnum + 1):                
     if i % mult == 0:
         print(i)


