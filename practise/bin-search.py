def search(l, key):
    found = False
    length = len(l)
    if length >= 1 and not found:
        if length == 1:
            if l[0] != key:
                found = False
                return found
        half=length/2
        if l[half-1] == key:
            found = True
            return found

        elif l[half-1] < key and not found:
            found = search(l[half:], key)

        elif l[half-1] > key and not found:
            found = search(l[:half], key)
        
        else:
            found = False

    return found 


print search([1,2,3,4,5,6], 40)
