def insertionSort(alist):
    for idx, elem in enumerate(alist[1:]):
        for j in range(0, len(alist[0:idx+1])):
            if alist[j] > elem:
                temp = alist[j]
                alist[j] = alist[idx+1]
                alist[idx+1] = temp

    return alist


alist = [54,26,93,17,77,31,44,55,20]
#print insertionSort(alist)



def insertionSort2(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

alist = [54,26,93,17,77,31,44,55,20]
import pdb; pdb.set_trace()
insertionSort2(alist)
print(alist)

