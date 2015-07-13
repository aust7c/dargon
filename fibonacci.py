__author__ = 'austin'
#print "hehe"
n = int(raw_input("Enter an int what you want"))
if n < 2:
    print ("you must put number over 3")
else:
    a = 1
    b = 2
    for i in range(1,n - 1):
        b = a + b
        a = b - a
        print i,a,b
    print(str(n)  + " fibonacci is " + str(b))