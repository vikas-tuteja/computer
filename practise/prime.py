x=range(100)

def prime(nums):
    for n in nums:
        if n<2: continue

        if n > 2 :
            if n%2==0 and n!=2:
                continue
            elif n%3==0 and n!=3:
                continue
            elif n%5==0 and n!=5:
                continue
            elif n%7==0 and n!=7:
                continue
        print n


prime(x)

