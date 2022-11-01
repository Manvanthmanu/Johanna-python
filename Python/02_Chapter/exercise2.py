# quetion  1 - calculate simple intrest
# quetion  2 - convert cm to m 
# quetion  3 - calculate the area of a sphere 
# quetion  4 - alculate perimeter of rectangle


# quetion  5 - calculate compound intrest


# step 1 - start

# step 2 - input(P ,r,n ,t)
p = int(input("please enter the principal amount : "))
r = int(input("pleae enter the rate of interest : "))
n = int(input("please enter the number of years "))

# step 3 - A = p(1 + r/n)^(nt)
a = p*(1+ r/100)**n

# step 4 - ci = A - p
ci = a - p

# step 5 - ci , A
print(int(a) , int(ci))

# step 6 - end
