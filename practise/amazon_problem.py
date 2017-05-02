x= "aabaaabbbbc"
#i="0123456789"
final_dict = {}
previous = None
this = None
key = ''

for i, elem in enumerate(range(0, len(x)+1)):
    if i==0: continue
    previous = x[i-1]
    try:
        this = x[i]
    except:
        this = None

    if not key:
        key = previous

    if previous == this:
        key += this
        continue

    else:
        alphabet = set(key).pop()
        if alphabet in final_dict:
            if len(key) > final_dict[alphabet]:
                final_dict[alphabet] = len(key)
        else:
            final_dict[alphabet] = len(key)
        key = ''

print final_dict
