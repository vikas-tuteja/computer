available_denom = [1,5,10,25]
available_denom.reverse()


def change(num):
    coins = 0
    global available_denom
    for a in available_denom:
        if num >= a:
            coins += num // a
            num = num % a

    return coins

print change(105)
