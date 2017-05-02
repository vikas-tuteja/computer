xs=input("enter a string\n")

x=[]
for i in xs:
    x.append(i)

while x:
    if len(x) == 1:
            break

    elif x[0] == x[-1]:
        x.pop()
        x.pop(0)

    else:
        print "not a palidrome"
        exit(1)

print "A palindrome"

